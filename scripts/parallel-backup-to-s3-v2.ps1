#!/usr/bin/env pwsh

###############################################################################
# Synopsis:                                                                   #
# Script for parallel Backup of SolidFire volumes to S3-compatible storage:   #
# Unlike v1 which parallelizes per cluster, this one parallelizes per each    #
# SolidFire storage node, making it possible to backup at full throttle       #
#                                                                             #
# NOTES:                                                                      #
# - In SolidFire 12.3 per-node maximum for bulk volume jobs is 8,             #
#   but if you expect to restore or perform on-demand backups while the script#
#   is running, limit parallel jobs to 7 or 6 jobs per SolidFire storage node #
# - Backup array $backup contains Volume IDs to backup; any order will do     #
# - Note that SolidFire volume "flip" events (automated adjustments)          # 
#     that occure periodically can change volumes' "home" node and job queues # 
#     will then be messed up. In that case you can resubmit failed jobs, or   # 
#     modify the script to update slice report every 30 or 60 minutes so that #
#     we learn the volumes' new locations before next 1-2 backup jobs go off  #
# - If you can take a quiesced snapshot before backup, set useLastSnap to     #
#     $True to get app-consistent (rather than crash-consistent) backup in S3 #
# - For added security sign your script, move creds out and run from a secure #
#   Windows workstation connected only to SolidFire Management Network        #
# - More (please manually reassemble the URL or use a search engine):         #
#   https://scaleoutsean.github.io/2021/06/22/solidfire-backup-and-cloning-   #
#   with-per-storage-node-queues.html                                         # 
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

# Install-Module SolidFire.Core and use PowerShell 7

Import-Module SolidFire.Core

# Edit connection details
$null = Connect-SFCluster 192.168.1.30 -Username admin -Password admin

# With NetApp StorageGRID, you could create a WORMILM policy to 
# auto-expire old backups (SolidFire has no awareness how many there are) 
# but also to prevent deletion of existing backups

$s3AccessKey = "AAAAAAAAAA"
$s3SecretKey = "BBBBBBBBBB"
$s3Bucket    = "solidfire-native-backup"
$s3Endpoint  = "storagegrid.netapp.com:18443"

# Parallel backups per cluster (supported maximum is 8)
#   You may want to leave an empty slot or two for ad-hoc backup or restore jobs
[int]$parallel = 6 

# List of volumes to backup (by SolidFire Volume ID)
$backup        = @(150,151,152,153,154,155,156,157,158,159)

# Automatically use last snapshot (if available) instead of a temporary,
#     just-in-time snapshot, if this set to $True.
#     - Consider creating app-consistent $snapString-named snaps with (say) 6 hour
#     retention, or modify the script to find your snapshots without a mistake
#     - If you set this to $True and have stale snapshots, your backups will be old
#
$useLastSnap = $False

# If $useLastSnap=$True, we'll consider only SolidFire snapshots for the volume
#     named $snapString.
#     - Snapshots that exist for the volume but aren't named like that would be ignored
$snapString  = "backup-to-s3"

## Below this line you should not need to edit anything
## (You may edit anything you want, but you shouldn't need to)

$eventFrom = ((Get-SFEvent | Select-Object -First 1).EventID + 1)

$res = Invoke-SFApi -Method "GetReport" -Params @{"reportName"="slices.json"}

$vid2nid = [ordered]@{}
$service = @{}

function global:getutcdate {
    return [Xml.XmlConvert]::ToString((get-date),[Xml.XmlDateTimeSerializationMode]::Utc)
}

foreach ($p2n in $res.services) {$service.Add($p2n.serviceID,$p2n.nodeID)}

foreach ($v in $res.slices) {
    foreach ($k in $service.Keys) {
        $vn = @{}
        if ($v.primary -eq $k) {
            $v.nodeID    = $service[$k]
            [PSCustomObject]$vn = @{
                volumeID = $v.volumeID
                nodeID   = $v.nodeID
            }
            $vid2nid.Add($v.volumeID,$v.nodeID)
            }
    }
}

$nodeId   = ($vid2nid.Values | Select-Object -Unique)
Write-Host $(getutcdate), "we have", $nodeId.Count, "storage nodes and", $backup.Count, "volumes to process"

Write-Host $(getutcdate), "volume id job list:", $backup

$BackupQueue = @{}
foreach ($v in $backup) {
    if ($vid2nid.Keys -contains $v) {
        $kv = $vid2nid.GetEnumerator() | Where-Object {$_.key -eq $v}
        Write-Host $(getutcdate), "checking for volume id:", $kv.key
        Write-Host $(getutcdate), "node id value for this volume:", $kv.value
        $nodeId = $kv.value
        Write-Host $(getutcdate),"current jobs on this node id:", $BackupQueue.$nodeId
        Write-Host $(getutcdate), "volume", $v, "to be processed by node", $nodeId
        $BackupJobsPerNode = $BackupQueue.$nodeId
        $BackupJobsPerNode += ,$v
        $BackupQueue.$nodeId = $BackupJobsPerNode
    }
}

$set = [ordered]@{}

foreach ($n in $BackupQueue.Keys) {
    $jobstack = New-Object System.Collections.Generic.Stack[String]
    foreach ($vid in $BackupQueue[$n]) {
        Write-Host $(getutcdate), "adding volume id", $vid -ForegroundColor Yellow
        $jobstack.Push($vid)
        Write-Host $(getutcdate), "number of jobs for the node", $jobstack.Count
    }
    $set.Add($n, $jobstack)
}

function GetCurrentJob {
    $currentJob = [ordered]@{}
    foreach ($n in ($vid2nid.Values | Select-Object -Unique | Sort-Object)) {$currentJob[$n] = 0}
    $SfBulkVolumeJob = Get-SFBulkVolumeJob
    if ($null -eq $SfBulkVolumeJob) {
        Write-Host $(getutcdate), "no backup jobs running at this time, perhaps this script is just starting..."
    } else {
        [array]$vols = @()
        foreach ($bj in $SfBulkVolumeJob) { $vols += ($bj.SrcVolumeID)}
        Write-Host $(getutcdate), "volumes being currently backed up:", $vols
        foreach ($v in $vols) {
            if ($vid2nid.Keys -contains $v) {
                $kv  = $vid2nid.GetEnumerator() | Where-Object {$_.key -eq $v}
                $nodeId = $kv.Value
                $currentJob[$nodeId] = ($currentJob[$nodeId] + 1)
            } else {
                Write-Error -Message "volume cannot be found - check if it exists on SolidFire"
            }
        }
    }
    return $currentJob
}

$jobRemaining = 0
foreach ($kv in $set.GetEnumerator()) { $jobRemaining = $jobRemaining + $set[$kv.Key].Count}

while ($jobRemaining -gt 0) {
    $currentJob = GetCurrentJob
    foreach ($n in $set.Keys | Sort-Object) {
        if ($set[$n].Count -gt 0) {
            if ($currentJob[$n] -lt $parallel) {
                Write-Host $(getutcdate), "number of current jobs is less than the parallel job setting" -ForegroundColor Green
                $nextJob = $set[$n].Pop()
                Write-Host $(getutcdate), "volume id to be scheduled next:", $nextJob
                if ($useLastSnap -eq $True) {
                    Write-Host $(getutcdate), "finding last snapshot for the volume named $snapString (if any)"
                    $snapshotID = (Get-SFSnapshot -VolumeID $nextJob | Where-Object {$_.Name -eq "$snapstring"} | `
                        Sort-Object -Descending -Property CreateTime | Select-Object -First 1).snapshotID
                    Write-Host $(getutcdate), "found matching snapshot for volume", $nextJob, ": snapshot ID", $snapshotID
                } else { $snapshotID = 0 }
                $prefix = ((Get-SFClusterInfo).Name) + "-" + ((Get-SFClusterInfo).UniqueID) + "/" + `
                    ((Get-SFVolume -VolumeID $nextJob).Name) + "-" + "$nextJob"
                Write-Host $(getutcdate), "invoking backup to S3 with prefix:", $prefix -ForegroundColor Yellow
                Invoke-SFApi -Method StartBulkVolumeRead -Params @{ "volumeID"= "$nextJob"; "format" = "native"; `
                "script" = "bv_internal.py"; "snapshot_id" = "$snapshotID"; "scriptParameters" = @{ "write" = @{ "awsAccessKeyID" = "$s3AccessKey"; `
                "awsSecretAccessKey" = "$s3SecretKey"; "bucket"= "$s3Bucket"; "prefix"= "$prefix"; `
                "endpoint"= "s3"; "hostname"= "$s3Endpoint" }}} | Out-Null
            } else {
                Write-Host $(getutcdate), "number of current jobs is NOT less than the parallel job setting" -ForegroundColor Yellow
                Write-Host $(getutcdate), "queue full for node", $n -ForegroundColor Yellow
                Write-Host $(getutcdate), "current and max jobs:", $currentJob[$n], $parallel -ForegroundColor Blue
                Start-Sleep 1
            }
        } else {
            Write-Host $(getutcdate), "there are no jobs for this node", $n -ForegroundColor Blue
        }
    }
    $jobRemaining = 0
    foreach ($kv in $set.GetEnumerator()) { $jobRemaining = $jobRemaining + $set[$kv.Key].Count}
    Write-Host $(getutcdate), "number of jobs left across all storage cluster nodes:", $jobRemaining -ForegroundColor Cyan
    Start-Sleep 2
}

$eventTo = (Get-SFEvent | Select-Object -First 1).EventID
$eventBulk = (Get-SFEvent -StartEventID $eventFrom -EndEventID $eventTo)
Write-Host $(getutcdate), "all jobs dispatched - checking SolidFire events between start and end event id:", $eventFrom, $eventTo
$backupdone = @()

foreach ($e in ($eventBulk | Sort-Object -Property TimeOfPublish)) {
    if ($e.EventInfoType -eq "bulkOpEvent" -and $e.Message -eq "Bulk volume operation succeeded") {
        Write-Host $(getutcdate), "success:", $e.TimeOfPublish "(UTC) for volume id", $e.Details.volumeID, `
            $e.Details.result -ForegroundColor Green
        $backupdone += $e.Details.volumeID
    } elseif ($e.EventInfoType -eq "bulkOpEvent" -and $e.Message -eq "Bulk volume operation failed") {
        Write-Host $(getutcdate), "result:", $e.TimeOfPublish "(UTC) for volume id", $e.Details.volumeID, `
            $e.Details.result -ForegroundColor Red
    } else {}
}

Write-Host $(getutcdate), "backup successfully completed for volumes:", $backupdone -ForegroundColor Green
Write-Host $(getutcdate), "backup still ongoing for volumes:", ((Get-SFBulkVolumeJob).SrcVolumeID) -ForegroundColor DarkYellow
