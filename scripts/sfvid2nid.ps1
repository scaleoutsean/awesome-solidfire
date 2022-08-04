#!/usr/bin/env pwsh
###############################################################################
# Script name:                                                                #
# sfvid2nid.ps1                                                               #
#                                                                             #
# Synopsis:                                                                   #
# Maps SolidFire volume IDs to storage node IDs and calculates MinIOPS/Node   #
#                                                                             #
# NOTE: uses non-public report API which is may be deprecated without notice  #
#       and should not be frequently executed (once every 5-10 minutes is OK) #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

# Import SolidFire module for older PowerShell 5.1
# Import-Module SolidFire

Import-Module SolidFire.Core
$null = Connect-SFCluster 192.168.1.30 -Username admin -Password admin

$res = Invoke-SFApi -Method 'GetReport' -Params @{'reportName' = 'slices.json' }

$vid2nid = @{}
$service = @{}
$nodeGuarantee = @{}

foreach ($p2n in $res.services) { $service.Add($p2n.serviceID, $p2n.nodeID) }

foreach ($n in $service.Values) { $nodeGuarantee.Add($n, 0) }

foreach ($v in $res.slices) {
    foreach ($k in $service.Keys) {
        $vn = @{}
        $vMin = 0
        if ($v.primary -eq $k) {
            $v.nodeID = $service[$k]
            $vMin = (Get-SFVolume -VolumeID $v.volumeID).Qos.MinIOPS
            [PSCustomObject]$vn = @{
                volumeID = $v.volumeID
                nodeID   = $v.nodeID
            }
            $nodeGuarantee[$v.nodeID] = $nodeGuarantee[$v.nodeID] + $vMin
            $vid2nid.Add($v.volumeID, $v.nodeID)
        }
    }
}

Write-Host 'Min IOPS by node ID:'
$nodeGuarantee | Format-Table 

Write-Host 'Volume-Node pairings by volume ID:'
$vid2nid | Sort-Object -Property Name | Format-Table

Write-Host 'Volume-Node pairings by node ID:'
$vid2nid | Sort-Object -Property @{Expression = 'Value'; Descending = $False }, @{Expression = 'Name'; Descending = $False } | Format-Table

<#

SAMPLE OUTPUT FROM SOLIDFIRE 12.5 CLUSTER WITH 5 NODES
===============================================================

Min IOPS by node ID:

Name                           Value
----                           -----
13                             43900
10                             43900
4                              43950
2                              43900
1                              51000

Volume-Node pairings by volume ID:

Name                           Value
----                           -----
262                            2
261                            2
260                            2
259                            10
258                            10
...

Volume-Node pairings by node ID:

Name                           Value
----                           -----
92                             1
93                             1
122                            1
135                            1
255                            1
3                              2
4                              2
51                             2
54                             2
...

#>