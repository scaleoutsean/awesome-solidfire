#!/usr/bin/env pwsh

###############################################################################
# Synopsis:                                                                   #
# Script for parallel Backup of SolidFire volumes to S3 compatible storage    #
#                                                                             #
# NOTES:                                                                      #
# - In SolidFire 12.3 per-node maximum for bulk volume jobs is 8,             #
#   so 10 jobs should rarely hit the maximum on any single node               #
#   If you want to run more jobs in parallel, consider to resubmit failed jobs#
# - Backup array $backup contains Volume IDs to backup; any order will do     #
# - For added security sign your script, move creds out and run from a secure #
#   Windows workstation connected to SolidFire Management Network             #
# - More:                                                                     #
#   https://scaleoutsean.github.io/2021/04/21/solidfire-backup-to-s3.html     #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

# Install-Module SolidFire.Core # for PowerShell 7; just "SolidFire" for 5.1

$p           = 4
$useLastSnap = $False
$backup      = @(148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167)

$backup | ForEach-Object -Parallel {
    Import-Module SolidFire.Core
    $null   = Connect-SFCluster 192.168.1.30 -Username admin -Password admin
    $prefix =  ((Get-SFClusterInfo).Name) + "-" + ((Get-SFClusterInfo).UniqueID) + "/" + ((Get-SFVolume -VolumeID "$_").Name) + "-" + "$_"
    if ($useLastSnap -eq $True) { 
        Write-Host "Using last snapshot for Volume if any..."
        $snapshotID = (Get-SFSnapshot -VolumeID "$_" | Sort-Object -Descending -Property CreateTime | Select-Object -First 1).snapshotID
    } else { $snapshotID = 0 }
    $b   = Invoke-SFApi -Method StartBulkVolumeRead -Params @{ "volumeID"= "$_"; "snapshotID" = $snapshotID.snapshotID ; "format" = "native"; "script" = "bv_internal.py"; "scriptParameters" = @{ "write" = @{ "awsAccess KeyID" = "AAAAAAAAAAAA"; "awsSecretAccessKey" = "BBBBBBBBBBB"; "bucket"= "backup"; "endpoint" = "s3"; "hostname" = "1.2.3.4:443" ; "prefix" = $prefix}}}
    $vid = (Get-SFASyncResult -KeepResult:$True -ASyncResultID $b.asyncHandle).details.volumeID
    Write-Host "Bulk job running on VolumeID:" $vid
    while ($status -ne "complete"){
        $gar = (Get-SFASyncResult -KeepResult:$True -ASyncResultID $b.asyncHandle)
        $vid = $gar.details.volumeID
        $status = $gar.status
        if ($status -eq "failed") {
            Write-Error -Message "Job failure (Volume ID, Time, Msg):" $vid, $gar.lastUpdateTime, $gar.details.message
        } else {
        Write-Host "Volume ID"`t $vid `t (Get-Date -f u) `t  $status
        Start-Sleep 15
        }
    }
} -ThrottleLimit $p
