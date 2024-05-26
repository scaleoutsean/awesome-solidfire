#!/usr/bin/env pwsh
# Requires -Version 7.0
###############################################################################
# Synopsis:                                                                   #
# Get serial numbers, node and drive IDs, chassis slot of SolidFire SSD drives#
#                                                                             #
# Get-SFDiskInventory                                                         #
# Get-SFDiskInventory -sortBy serial                                          #
# Get-SFDiskInventory -sortBy node -outFile drives-by-node.csv                #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

param (
    [string]$mvip,
    [string]$outFile,
    [string]$sortBy = 'driveId'
)
    
switch ($SortBy) {
    "node" { $sortBy = "nodeId" }
    "serial" { $sortBy = "serial" }
    "type" { $sortBy = "type" }
    default { $sortBy = "driveID" }
}

# Import-Module SolidFire # PS 5.1
Import-Module SolidFire.Core # PS 7.x

$null = Connect-SFCluster -Target $mvip

Get-SFClusterInfo | Select-Object -Property Name,Mvip,UniqueID,Uuid

$sfDrives = @()
$sfDrive = @(Get-SFDrive)

foreach ($i in $sfDrive) {
    $drive = [PSCustomObject]@{
        driveId = $i.driveID
        nodeId = $i.NodeID
        serial = $i.Serial
        slot = $i.Slot
        size = $i.Capacity
        status = $i.Status
        type = $i.Type
    }
    $sfDrives += $drive
}

$sfDrives | Sort-Object -Property $sortBy | Format-Table -AutoSize
if ($OutFile) {
    $sfDrives | Export-Csv -Path $OutFile
    Write-Host "Output saved to", $OutFile
}
