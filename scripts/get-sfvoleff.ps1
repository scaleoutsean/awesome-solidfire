###############################################################################
# Synopsis:                                                                   #
# Find low-efficiency volumes on NetApp HCI, SolidFire and eSDS storage       #
# NOTE: Thin Provisioning is not considered. Virtual Volumes are not suported #
#                                                                             #
# Get-SFVolEff $EfficiencyFactor $SortProperty                                #
#  - where                                                                    #
#    - EfficiencyFactor is positive number greater than 1 (default: 2)        #
#    - SortProperty is one of the following strings:                          #
#         id, name, full, compress, dedupe, eff (total efficiency; default)   #
#                                                                             #
# Examples:                                                                   #
# Get-SFVolEff.ps1 -CutOff 3                                                  #
# - Include volumes with Compr x Dedupe factor <= 3, sort by total efficiency #
# Get-SFVolEff.ps1 -SortBy name                                               #
# - Include volumes with total efficiency below 2.00x and sort by volume name #
# Get-SFVolEff.ps1 -OutFile eff.csv                                           #
# - Export list of volumes with total efficiency below 2.00x to eff.csv       #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

# Import-Module SolidFire # PS 5.1
# Import-Module SolidFire.Core # PS 7.x
# Connect-SFCluster 192.168.1.30 -Username admin -Password xxxx

param (
    [Parameter(
        Mandatory = $false,
        HelpMessage = 'Total efficiency ratio cut-off factor (e.g. 2)')]
    [decimal]$CutOff = 2,

    [Parameter(
        Mandatory = $false,
        HelpMessage = 'One of the following strings: id, name, full, compress, dedupe, eff (default)')]
    [string]$SortBy = "eff",

    [Parameter(
        Mandatory = $false,
        HelpMessage = 'Optionally output to specified CSV file name (e.g. "eff.csv")')]
    [string]$OutFile = $null
)

if ($null -eq $CutOff) {
    $CutOff = 2
    Write-Host -ForegroundColor Cyan "Cut-off efficiency factor: 2 (default)"
} else {
    # $CutOff = $args[0]
    Write-host "# Excluding volumes with total efficiency factor above", $CutOff, "and sorting by", $SortBy
}

switch ($SortBy) {
    "id" { $sortBy = "volumeID" }
    "name" { $sortBy = "volumeName" }
    "full" { $sortBy = "fullness" }
    "eff" { $sortBy = "volumeEffTotal" }
    "compress" { $sortBy = "volumeEffCompr" }
    "dedupe" { $sortBy = "volumeEffDedupe" }
    default { $sortBy = "volumeEffTotal" }
}

$vs = (Get-SFVolume -ExcludeVVOLs)
$vols = @()
foreach ($v in $vs) { 
    # Write-Host "v:", $v
    $volNZB     = ((Get-SFVolumeStats -VolumeID $v.volumeID).nonZeroBlocks)
    $volZB      = ((Get-SFVolumeStats -VolumeID $v.volumeID).ZeroBlocks)
    $volPctFull = ([MATH]::Round(($volNZB*100/($volZB+$volNZB)),3))
    $r = (Get-SFVolumeEfficiency -VolumeID $v.VolumeID | Select-Object -Property Compression,Deduplication)
    # Write-Host "r:", $r
    $SfVolC = ([MATH]::Round($r.Compression,2)) ; $SfVolD = ([MATH]::Round($r.Deduplication,2))
    $SfVolT = ([MATH]::Round(($SfVolC * $SfVolD),2))
    if ($SfVolT -lt $CutOff) {
        $vol = [PSCustomObject]@{
            volumeID = $v.volumeID
            volumeName = $v.name
            fullness = $volPctFull
            volumeEffCompr = $SfVolC
            volumeEffDedupe = $SfVolD
            volumeEffTotal = $SfVolT
        }
        $vols += $vol
    }    
}

$vols | Sort-Object -Property $sortBy | Format-Table -AutoSize
if ($OutFile) {
    $vols | Export-Csv -Path $OutFile
    Write-Host "Output saved to", $OutFile
}