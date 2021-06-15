#!/usr/bin/env pwsh

###############################################################################
# Synopsis:                                                                   #
# Script for parallel Backup of SolidFire volumes to S3-compatible storage    #
#                                                                             #
# NOTES:                                                                      #
# - Note there are two places where SF connection is defined. Why? See:       #
#   get-help about_Scopes                                                     #
# - In SolidFire 12.3 per-node maximum for bulk volume jobs is 8,             #
#   so 10 cluster-wide jobs should rarely hit the maximum on any single node  #
#   If you want to run more jobs in parallel, consider to resubmit failed jobs#
# - Backup array $backup contains Volume IDs to backup; any order will do     #
# - If you can take quiesced snapshot before backup, set useLastSnap to $True #
#   to have app-consistent (rather than crash-consistent) backup in S3        #
# - For added security sign your script, move creds out and run from a secure #
#   Windows workstation connected to SolidFire Management Network             #
# - More:                                                                     #
#   https://scaleoutsean.github.io/2021/04/21/solidfire-backup-to-s3.html     #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

# Install-Module SolidFire.Core # for PowerShell 7; PowerShell 7.1.3+ required 

Import-Module SolidFire.Core

# Edit connection details both below and also inside of the loop (~L55-ish)
$null = Connect-SFCluster 192.168.1.30 -Username admin -Password admin
# Parallel backups per cluster (per-node is not controlled - that depends on 
#     the location of each individual volume on SolidFire storage nodes)
$p           = 4
# List of volumes to backup (by volume ID)
$backup      = @(355,356,357)
# Automatically use last snapshot (if available) instead of temporary,
#     just-in-time snapshot.
#     Consider creating app-consistent $snapString-named snaps with 6 hour 
#     retention, or modify the script to find your snapshots without a mistake
#     
$useLastSnap = $False
# If $useLastSnap=$True, we'll consider only snapshots called $snapString
#     Snapshots that exist but aren't named the same will be ignored
$snapString  = "backup-to-s3"

## Below this line you must edit ONLY SolidFire and S3 credentials
## (You may edit anything you want, but for the script to work just those two)

$eventFrom = ((Get-SFEvent | Select-Object -First 1).EventID + 1)

function global:getutcdate {
    return [Xml.XmlConvert]::ToString((get-date),[Xml.XmlDateTimeSerializationMode]::Utc)
}

$backup | ForEach-Object -Parallel {
    Import-Module SolidFire.Core
    # Edit scope-related credentials to be consistent with earlier credentials
    $null = Connect-SFCluster 192.168.1.30 -Username admin -Password admin
    # Edit scope-related S3 backup destination details
    $s3AccessKey = "AAAAAAAAAAAAAAA"
    $s3SecretKey = "BBBBBBBBBBBBBBB"
    $s3Bucket    = "solidfire-native-backup"
    $s3Endpoint  = "s3.netapp.com:443"
    function getutcdate {
        return [Xml.XmlConvert]::ToString((get-date),[Xml.XmlDateTimeSerializationMode]::Utc)
    }
    if ($useLastSnap -eq $True) { 
        Write-Host $(getutcdate), "finding last snapshot for the volume named $snapString (if any)"
        $snapshotID = (Get-SFSnapshot -VolumeID "$_" | Where-Object {$_.Name -eq "$snapstring"} | `
            Sort-Object -Descending -Property CreateTime | Select-Object -First 1).snapshotID
        Write-Host $(getutcdate), "found matching snapshot for volume", "$_", "- snapshot ID", $snapshotID
    } else { $snapshotID = 0 }
    $prefix = ((Get-SFClusterInfo).Name) + "-" + ((Get-SFClusterInfo).UniqueID) + "/" + `
        ((Get-SFVolume -VolumeID "$_").Name) + "-" + "$_"
    Write-Host $(getutcdate), "invoking backup to S3 with prefix:", $prefix -ForegroundColor Yellow
    $b = Invoke-SFApi -Method StartBulkVolumeRead -Params @{ "volumeID"= "$_"; "format" = "native"; `
        "script" = "bv_internal.py"; "scriptParameters" = @{ "write" = @{ "awsAccessKeyID" = "$s3AccessKey"; `
        "awsSecretAccessKey" = "$s3SecretKey"; "bucket"= "$s3Bucket"; "prefix"= "$prefix"; `
        "endpoint"= "s3"; "hostname"= "$s3Endpoint" }}}
    $vid = (Get-SFASyncResult -KeepResult:$True -ASyncResultID $b.asyncHandle).details.volumeID
    Write-Host $(getutcdate), "bulk volume job running on volume ID:", $vid
    while ($status -ne "complete"){
        $gar = (Get-SFASyncResult -KeepResult:$True -ASyncResultID $b.asyncHandle)
        $vid = $gar.details.volumeID
        $status = $gar.status
        if ($status -eq "failed") {
            Write-Error -Message "Job failure (Volume ID, Time, Msg, Error):" $vid, $gar.lastUpdateTime, `
                $gar.error.message, $gar.error.name -ForegroundColor Red
        } elseif ($status -eq "running") {
            try { 
                $bvj = Get-SFBulkVolumeJob -VolumeID $vid 
	        Write-Host $(getutcdate), "bulk volume job percent complete for volume ID", $gar.details.volumeID, `
                ":", $bvj.PercentComplete
	    }
	    catch {
            Write-Host $(getutcdate), "volume ID", $gar.srcVolumeID, $status, "at (local time)", (Get-Date -f u)
            }
        } else {
            Write-Host $(getutcdate), "volume ID", $gar.result.volumeID, $status, "at (local time)", (Get-Date -f u)
	}
        Start-Sleep 15
    }
} -ThrottleLimit $p

$eventTo = (Get-SFEvent | Select-Object -First 1).EventID
$eventBulk = (Get-SFEvent -StartEventID $eventFrom -EndEventID $eventTo)
Write-Host $(getutcdate), "checking SolidFire events between start and end event ID:", $eventFrom, $eventTo
$backupdone = @()

foreach ($e in ($eventBulk | Sort-Object -Property TimeOfPublish)) {
    if ($e.EventInfoType -eq "bulkOpEvent" -and $e.Message -eq "Bulk volume operation succeeded") {
        Write-Host $(getutcdate), "success:", $e.TimeOfPublish "(UTC) for volume ID", $e.Details.volumeID, `
            $e.Details.result -ForegroundColor Green
	$backupdone += $e.Details.volumeID
    } elseif ($e.EventInfoType -eq "bulkOpEvent" -and $e.Message -eq "Bulk volume operation failed") {
        Write-Host $(getutcdate), "result:", $e.TimeOfPublish "(UTC) for volume ID", $e.Details.volumeID, `
            $e.Details.result -ForegroundColor Red 
    } else {}
}

Write-Host $(getutcdate), "backup successfully completed for volumes:", $backupdone
