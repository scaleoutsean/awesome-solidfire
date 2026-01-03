#!/usr/bin/env python3
# License: Apache License 2.0
# Copyright 2026 scaleoutSean (github.com/scaleoutsean)
#
# Note: I no longer have access to a multi-node SolidFire cluster for testing, but worst case this should work after minor tweaks.
#


"""Parallel SolidFire native backups to S3-compatible storage."""

from __future__ import annotations

import argparse
import json
import logging
import re
import threading
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from getpass import getpass
from pathlib import Path
from typing import Deque, Dict, Iterable, List, Optional, Tuple

from solidfire import common
from solidfire.common import ApiServerError, SdkOperationError
from solidfire.factory import ElementFactory

common.setLogLevel(logging.ERROR)


@dataclass
class BackupJob:
    """Represents a single SolidFire volume backup job."""

    volume_id: int
    node_id: int
    volume_name: str
    prefix: str
    snapshot_id: int = 0
    async_handle: Optional[int] = None
    bulk_volume_id: Optional[int] = None
    status: str = "pending"
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    def duration(self) -> Optional[float]:
        if self.started_at and self.completed_at:
            return (self.completed_at - self.started_at).total_seconds()
        return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dispatch SolidFire bulk volume backups per node while respecting concurrency limits."
    )
    parser.add_argument("--mvip", required=True, help="SolidFire cluster management IP or FQDN")
    parser.add_argument("--user", required=True, help="SolidFire cluster admin username")
    parser.add_argument("--password", help="SolidFire cluster admin password; prompted when omitted")
    parser.add_argument("--port", type=int, default=443, help="SolidFire HTTPS port (default: 443)")
    parser.add_argument("--insecure", action="store_true", help="Disable SSL validation")

    parser.add_argument("--volume", "-v", type=int, action="append", dest="volume_ids",
                        help="Volume ID to include. May be supplied multiple times.")
    parser.add_argument("--volume-file", type=Path,
                        help="File with volume IDs (JSON array or comma/line separated integers)")

    parser.add_argument("--per-node-limit", type=int, default=6,
                        help="Maximum concurrent jobs per storage node (default: 6)")
    parser.add_argument("--global-limit", type=int, default=0,
                        help="Maximum concurrent jobs cluster-wide; 0 derives from node limits")
    parser.add_argument("--poll-interval", type=int, default=10,
                        help="Seconds between async job status polls (default: 10)")

    parser.add_argument("--use-last-snapshot", action="store_true",
                        help="Use the latest snapshot named --snapshot-name instead of creating a temp one")
    parser.add_argument("--snapshot-name", default="backup-to-s3",
                        help="Snapshot name to reuse when --use-last-snapshot is set")

    parser.add_argument("--s3-access-key", required=True, help="S3 access key")
    parser.add_argument("--s3-secret-key", required=True, help="S3 secret key")
    parser.add_argument("--s3-bucket", required=True, help="Destination bucket")
    parser.add_argument("--s3-host", "--s3-endpoint", dest="s3_host", required=True,
                        help="S3-compatible hostname (optionally host:port)")
    parser.add_argument("--s3-endpoint-type", default="s3",
                        help="Endpoint name expected by SolidFire bulk volume script (default: s3)")

    parser.add_argument("--dry-run", action="store_true",
                        help="Show the planned dispatch order without starting backups")
    parser.add_argument("--log-level", default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Console log level (default: INFO)")
    return parser.parse_args()


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )


def _parse_volume_file(path: Path) -> List[int]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    try:
        raw = json.loads(text)
    except json.JSONDecodeError:
        tokens = [tok for tok in re.split(r"[\s,]+", text) if tok]
        return [int(tok) for tok in tokens]
    else:
        if isinstance(raw, dict):
            for key in ("volumes", "volume_ids", "volumeIDs"):
                if key in raw:
                    raw = raw[key]
                    break
        if isinstance(raw, list):
            return [int(item) for item in raw]
        raise ValueError("Volume file must contain a JSON array or a dictionary with volume IDs.")


def load_volume_ids(args: argparse.Namespace) -> List[int]:
    ordered: List[int] = []
    seen = set()
    cli_values = args.volume_ids or []
    for vid in cli_values:
        if vid not in seen:
            ordered.append(vid)
            seen.add(vid)
    if args.volume_file:
        for vid in _parse_volume_file(args.volume_file):
            if vid not in seen:
                ordered.append(vid)
                seen.add(vid)
    if not ordered:
        raise ValueError("Provide at least one volume ID via --volume or --volume-file")
    return ordered


def connect(args: argparse.Namespace):
    password = args.password or getpass("SolidFire password: ")
    return ElementFactory.create(
        args.mvip,
        args.user,
        password,
        port=args.port,
        verify_ssl=not args.insecure,
    )


def fetch_cluster_identity(sfe) -> Tuple[str, str]:
    info = sfe.get_cluster_info().to_json()
    return info.get("name", "cluster"), info.get("uniqueID", "unknown")


def fetch_volume_metadata(sfe, volume_ids: Iterable[int]) -> Dict[int, Dict[str, object]]:
    response = sfe.list_volumes(volume_ids=list(volume_ids)).to_json()
    metadata = {}
    for volume in response.get("volumes", []):
        vid = volume.get("volumeID")
        if vid is None:
            continue
        metadata[vid] = volume
    return metadata


def build_volume_node_map(sfe, volume_ids: Iterable[int]) -> Dict[int, int]:
    report = sfe.get_report(report_name="slices.json").to_json()
    services = {svc.get("serviceID"): svc.get("nodeID") for svc in report.get("services", [])}
    mapping: Dict[int, int] = {}
    wanted = set(volume_ids)
    for slc in report.get("slices", []):
        vid = slc.get("volumeID")
        if vid not in wanted:
            continue
        primary = slc.get("primary")
        node_id = services.get(primary)
        if node_id is not None:
            mapping[vid] = node_id
    return mapping


def validate_inputs(volume_ids: List[int], node_map: Dict[int, int], metadata: Dict[int, Dict[str, object]]) -> None:
    missing_nodes = sorted(set(volume_ids) - set(node_map))
    if missing_nodes:
        raise ValueError(f"Missing node information for volumes: {missing_nodes}")
    missing_meta = sorted(set(volume_ids) - set(metadata))
    if missing_meta:
        raise ValueError(f"Volumes not found via ListVolumes: {missing_meta}")


def prepare_job_queues(volume_ids: List[int], node_map: Dict[int, int],
                       metadata: Dict[int, Dict[str, object]],
                       cluster_name: str, cluster_uid: str) -> Dict[int, Deque[BackupJob]]:
    queues: Dict[int, Deque[BackupJob]] = defaultdict(deque)
    for volume_id in volume_ids:
        volume = metadata[volume_id]
        volume_name = volume.get("name", f"volume-{volume_id}")
        prefix = f"{cluster_name}-{cluster_uid}/{volume_name}-{volume_id}"
        job = BackupJob(
            volume_id=volume_id,
            node_id=node_map[volume_id],
            volume_name=volume_name,
            prefix=prefix,
        )
        queues[job.node_id].append(job)
    return queues


def resolve_snapshot_id(sfe, volume_id: int, snapshot_name: str) -> int:
    response = sfe.list_snapshots(volume_id=volume_id).to_json()
    snapshots = [snap for snap in response.get("snapshots", []) if snap.get("name") == snapshot_name]
    if not snapshots:
        return 0
    snapshots.sort(key=lambda snap: snap.get("createTime", ""), reverse=True)
    snap_id = snapshots[0].get("snapshotID")
    return int(snap_id) if snap_id is not None else 0


def start_backup_job(sfe, job: BackupJob, args: argparse.Namespace) -> BackupJob:
    job.started_at = datetime.now(timezone.utc)
    if args.use_last_snapshot and args.snapshot_name:
        job.snapshot_id = resolve_snapshot_id(sfe, job.volume_id, args.snapshot_name)
        logging.debug("Volume %s snapshot id resolved to %s", job.volume_id, job.snapshot_id)
    params = {
        "volumeID": job.volume_id,
        "format": "native",
        "script": "bv_internal.py",
        "snapshot_id": job.snapshot_id,
        "script_parameters": {
            "write": {
                "awsAccessKeyID": args.s3_access_key,
                "awsSecretAccessKey": args.s3_secret_key,
                "bucket": args.s3_bucket,
                "prefix": job.prefix,
                "endpoint": args.s3_endpoint_type,
                "hostname": args.s3_host,
            }
        },
    }
    logging.info("Starting backup for volume %s on node %s", job.volume_id, job.node_id)
    result = sfe.start_bulk_volume_read(**params)
    payload = result.to_json()
    job.async_handle = payload.get("asyncHandle")
    job.bulk_volume_id = payload.get("bulkVolumeID") or payload.get("bulk_volume_id")
    job.status = "running"
    wait_for_async_completion(sfe, job, args.poll_interval)
    return job


def wait_for_async_completion(sfe, job: BackupJob, poll_interval: int) -> None:
    if job.async_handle is None:
        job.status = "failed"
        job.error = "Missing async handle"
        job.completed_at = datetime.now(timezone.utc)
        return
    while True:
        try:
            result = sfe.get_async_result(async_result_id=job.async_handle, keep_result=True)
        except (ApiServerError, SdkOperationError) as exc:
            job.status = "failed"
            job.error = str(exc)
            job.completed_at = datetime.now(timezone.utc)
            return
        payload = result.to_json()
        status = payload.get("status", "")
        if status.lower() == "running":
            time.sleep(max(1, poll_interval))
            continue
        job.completed_at = datetime.now(timezone.utc)
        if status.lower() in {"complete", "completed", "success"}:
            job.status = "success"
        else:
            job.status = status or "failed"
            job.error = payload.get("error") or payload.get("details")
        break


def dispatch_jobs(sfe, queues: Dict[int, Deque[BackupJob]], args: argparse.Namespace) -> List[BackupJob]:
    pending = sum(len(q) for q in queues.values())
    if pending == 0:
        return []
    global_limit = args.global_limit or (args.per_node_limit * max(len(queues), 1))
    max_workers = max(1, min(global_limit, pending))
    semaphore = threading.BoundedSemaphore(max_workers)
    node_counts: Counter = Counter()
    completed: List[BackupJob] = []
    inflight: Dict[object, Tuple[BackupJob, int]] = {}

    from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait

    logging.info(
        "Dispatching %s jobs across %s nodes (per-node limit %s, cluster limit %s)",
        pending,
        len(queues),
        args.per_node_limit,
        max_workers,
    )

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while any(queues.values()) or inflight:
            made_progress = False
            for node_id in sorted(queues):
                node_queue = queues[node_id]
                if not node_queue:
                    continue
                if node_counts[node_id] >= args.per_node_limit:
                    continue
                if not semaphore.acquire(blocking=False):
                    break
                job = node_queue.popleft()
                future = executor.submit(start_backup_job, sfe, job, args)
                inflight[future] = (job, node_id)
                node_counts[node_id] += 1
                made_progress = True
            if not inflight:
                break
            if not made_progress:
                done, _ = wait(list(inflight.keys()), timeout=1, return_when=FIRST_COMPLETED)
            else:
                done, _ = wait(list(inflight.keys()), timeout=0, return_when=FIRST_COMPLETED)
            for future in done:
                job, node_id = inflight.pop(future)
                node_counts[node_id] -= 1
                semaphore.release()
                try:
                    completed_job = future.result()
                except Exception as exc:  # pylint: disable=broad-except
                    job.status = "failed"
                    job.error = str(exc)
                    job.completed_at = datetime.now(timezone.utc)
                    completed_job = job
                completed.append(completed_job)
    return completed


def print_plan(queues: Dict[int, Deque[BackupJob]]) -> None:
    for node_id in sorted(queues):
        jobs = list(queues[node_id])
        if not jobs:
            continue
        logging.info("Node %s -> volumes %s", node_id, [job.volume_id for job in jobs])


def summarize(jobs: List[BackupJob], started: datetime) -> None:
    total = len(jobs)
    success = [job for job in jobs if job.status == "success"]
    failed = [job for job in jobs if job.status != "success"]
    logging.info("Completed %s jobs in %s", total, datetime.now(timezone.utc) - started)
    logging.info("Successful: %s | Failed: %s", len(success), len(failed))
    for job in failed:
        logging.error("Volume %s failed (%s): %s", job.volume_id, job.status, job.error)


def main() -> None:
    args = parse_args()
    configure_logging(args.log_level)
    volume_ids = load_volume_ids(args)
    sfe = connect(args)
    cluster_name, cluster_uid = fetch_cluster_identity(sfe)
    metadata = fetch_volume_metadata(sfe, volume_ids)
    node_map = build_volume_node_map(sfe, volume_ids)
    validate_inputs(volume_ids, node_map, metadata)
    queues = prepare_job_queues(volume_ids, node_map, metadata, cluster_name, cluster_uid)

    if args.dry_run:
        print_plan(queues)
        return

    start_ts = datetime.now(timezone.utc)
    jobs = dispatch_jobs(sfe, queues, args)
    summarize(jobs, start_ts)


if __name__ == "__main__":
    main()
