#!/usr/bin/env pwsh
######################################################################################
# Synopsis:                                                                          #
# Gathers SolidFire volume properties and performance stats in the InfluxDB format   # 
# and prepares for pickup by Telegraf.                                               #
#                                                                                    #
# More:                                                                              #
# https://github.com/influxdata/telegraf/blob/master/plugins/inputs/exec/README.md   #
# More:                                                                              #
# https://scaleoutsean.github.io/2024/05/20/netapp-solidfire-input-for-telegraf.html #
#                                                                                    #
# Author: @scaleoutSean                                                              #
# https://github.com/scaleoutsean/awesome-solidfire                                  #
# License: the BSD License 3.0                                                       #
######################################################################################


# Change module name to SolidFire for PowerShell 5.1
if ($null -eq (Get-Module -Name SolidFire.Core -ListAvailable)) {
    try {
        Install-Module -Name SolidFire.Core -Force -Scope CurrentUser
    }
    catch {
        exit 1    
    }

} else {
    Import-Module -Name SolidFire.Core
} 

# Use the following for PowerShell 5.1
# Import-Module SolidFire
$conn = Connect-SFCluster -Target 192.168.1.30 -Username admin -Password xxxx

$vol = Get-SFVolume -ExcludeVVOLs -VolumeStatus active

$volPropsPayload = $null
foreach ($v in $vol) {
    $volTags = "volumeProps,volumeId=" + $v.VolumeID.ToString() + ",volumeName=" + $v.Name.ToString() + ",accountId=" + $v.AccountID.ToString() + ",scsiNaaDeviceId=" + $v.ScsiNAADeviceID + " "
    if ($null -eq $v.QosPolicyID) {
        $volFields = "qosPolicyId=0i"
    }
    else {
        $volFields = "qosPolicyId=" + $v.QosPolicyID.ToString() + "i"
    }
    $volFields = $volFields + ",volumeSize=" + $v.TotalSize.ToString() + "i,volumeBlockSize=" + $v.BlockSize.ToString() + "i" + ",fifoSize=" + $v.FifoSize.ToString() + "i" + ",minFifoSize=" + $v.MinFifoSize.ToString() + "i" + " `n"
    $volPropsPayload = $volPropsPayload + $volTags + $volFields
}

Write-Host $volPropsPayload

# If outputting to file:
# $volPropsPayload | Out-File -FilePath /tmp/telegrafVolPropsPayload.out

$volStatsPayload = ""
foreach ($volId in ($vol.VolumeID)) {
    $volTags = ""; $volFields = ""; $volName = ""
    $jobResp = Get-SFVolumeStats -VolumeID $volId -SFConnection $conn
    if ($vol.VolumeID -contains $jobResp.VolumeID) {
        $volName = $vol | Where-Object { $_.VolumeID -eq $jobResp.VolumeID } | Select-Object -ExpandProperty Name
    }
    else {
        Write-Host "Volumename unknown for volume ID", $jobResp.VolumeID
    }
    $volTags = "volumeStats,volumeId=" + ($jobResp.volumeID).ToString() + ",accountId=" + $jobResp.AccountID.ToString() + ",volumeName=" + $volName.ToString() + " " 
    $volFields = "latencyUSec=" + $jobResp.LatencyUSec.ToString() + ",throttle=" + $jobResp.Throttle.ToSTring() + ",volUtilPct=" + $jobResp.VolumeUtilization.ToSTring() + ",actualIOPS=" + $jobResp.ActualIOPS.ToString() + ",averageIOpSize=" + $jobResp.AverageIOPSize.ToString() +",volumeUtil=" + $jobResp.VolumeUtilization.ToString() + ",readLatencyUSec=" + $jobResp.ReadLatencyUSec.ToString() + ",writeLatencyUSec=" + $jobResp.WriteLatencyUSec.ToString() + ",zeroBlocks=" + $jobResp.ZeroBlocks.ToString() + "`n"
    $volStatsPayload = $volStatsPayload + $volTags + $volFields
}

Write-Host $volStatsPayload

# If outputting to file:
# $volStatsPayload| Out-File -FilePath /tmp/telegrafVolStatsPayload.out
# Change ownership on all .out files in /tmp/*.out to allow Telegraf to read them
# chown telegraf:telegraf /tmp/*.out

