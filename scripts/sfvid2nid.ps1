#!/usr/bin/env pwsh
###############################################################################
# Script name:                                                                #
# sfvid2pid.ps1                                                               #
#                                                                             #
# Synopsis:                                                                   #
# Maps SolidFire volume IDs to storage node IDs                               #
# Can be useful for optimizing parallel execution of backup and clone jobs    #
#                                                                             #
# NOTE: uses non-public report API which is may be deprecated without notice  #
#       and should not be frequently executed (once every 5-10 minutes is OK?)#
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

# Import-Module SolidFire

Import-Module SolidFire.Core
$null = Connect-SFCluster 192.168.1.30 -Username admin -Password admin

$res = Invoke-SFApi -Method "GetReport" -Params @{"reportName"="slices.json"}

$vid2nid = @{}
$service = @{}

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

Write-Host "By volume ID:"
$vid2nid.GetEnumerator() | Sort-Object -Property Name 

Write-Host "By node ID:"
$vid2nid.GetEnumerator() | Sort-Object -Property @{Expression = "Value"; Descending = $False}, @{Expression = "Name"; Descending = $False}
