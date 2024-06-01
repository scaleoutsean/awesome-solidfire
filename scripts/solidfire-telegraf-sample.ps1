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
$conn = Connect-SFCluster -Target 192.168.1.30 -Username monitor -Password xxxxxxxxxxxxxxxx

$vol = Get-SFVolume -ExcludeVVOLs -VolumeStatus active

$volPropsPayload = $null
foreach ($v in $vol) {
    $volTags = ''; $volFields = ''
    $volTags = "volumeProps,accountId=" + $v.AccountID.ToString() + ",scsiNaaDeviceId=" + $v.ScsiNAADeviceID + ",volumeId=" + $v.VolumeID.ToString() + ",volumeName=" + $v.Name.ToString() + " "   
    $volFields = $volFields + "fifoSize=" + $v.FifoSize.ToString() + "i,minFifoSize=" + $v.MinFifoSize.ToString() + "i"
    if ($null -eq $v.QosPolicyID) {
        $volFields = $volFields + "i,qosPolicyId=0i"
    }
    else {
        $volFields = $volFields + "i,qosPolicyId=" + $v.QosPolicyID.ToString() + "i"
    }
    $volFields = $volFields + "volumeBlockSize=" + $v.BlockSize.ToString() + "i,volumeSize=" + $v.TotalSize.ToString() + "i" + " `n"
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
        Write-Host "Volume name unknown for volume ID", $jobResp.VolumeID
    }
    # $jobResp.Throttle and $jobResp.VolumeUtilization are floats; the rest are int, convert float to string
            
    $volTags = "volumeStats,accountId=" + $jobResp.AccountID.ToString() + ",volumeId=" + ($jobResp.volumeID).ToString() + ",volumeName=" + $volName.ToString() + " " 
    $volFields = "actualIOPS=" + $jobResp.ActualIOPS.ToString() + "i,averageIOpSize=" + $jobResp.AverageIOPSize.ToString() + "i,latencyUSec=" + $jobResp.LatencyUSec.ToString() + "i,readLatencyUSec=" + $jobResp.ReadLatencyUSec.ToString() + "i,throttle=" + $jobResp.Throttle.ToSTring() + ",volUtilPct=" + $jobResp.VolumeUtilization.ToSTring() + ",writeLatencyUSec=" + $jobResp.WriteLatencyUSec.ToString() + "i,zeroBlocks=" + $jobResp.ZeroBlocks.ToString() + "i" + "`n"
    $volStatsPayload = $volStatsPayload + $volTags + $volFields
}

Write-Host $volStatsPayload

# If outputting to file:
# $volStatsPayload| Out-File -FilePath /tmp/telegrafVolStatsPayload.out
# Change ownership on all .out files in /tmp/*.out to allow Telegraf to read them
# chown telegraf:telegraf /tmp/*.out

# check out https://scaleoutsean.github.io/sfc - ready-to-go SolidFire Collector (SFC) for Telegraf written in Python 3

