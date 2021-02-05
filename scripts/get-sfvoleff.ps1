###############################################################################
# Synopsis:                                                                   #
# Find low-efficiency volumes on NetApp HCI, SolidFire and eSDS storage       #
# NOTE: Thin Provisioning is not considered. Virtual Volumes are not suported #
#                                                                             #
# Get-SFVolEff $EfficiencyFactor                                              #
#  - where EfficiencyFactor is positive number greater than 1                 #
#                                                                             #
# Examples:                                                                   #
# Get-SFVolEff.ps1 3                                                          #
# - Highlight volume IDs and names with with Compr x Dedupe factor <= 3       #
# Get-SFVolEff.ps1                                                            #
# - Highlight volume IDs and names with with Compr x Dedupe factor <= 2       #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

# Import-Module SolidFire
# Connect-SFCluster

$CutOff = $args[0]
$SfVolEff = @{}
$vs = (Get-SFVolume -ExcludeVVOLs)
if ($null -eq $CutOff) {
    $CutOff = 2
    Write-Host -ForegroundColor Cyan "Cut-off efficiency factor: 2 (default)"
} else {
    $CutOff = $args[0]
    Write-host "Cut-off efficiency factor:" $CutOff
}
Write-Host "==== OVERVIEW: VOLUMES' EFFICIENCY (Volume ID, Name, Efficiency Factor) ===="
ForEach ($v in $vs) {
    $vol = @{}
    $d = New-Object 'system.collections.generic.dictionary[string,string]'
    $SfVolName = $v.Name; $SfVolId = $v.VolumeID
    $r = (Get-SFVolumeEfficiency -VolumeID $SfVolId | Select-Object -Property Compression,Deduplication)
    $SfVolC = ([MATH]::Round($r.Compression,2)) ; $SfVolD = ([MATH]::Round($r.Deduplication,2))
    $SfVolT = ([MATH]::Round(($SfVolC * $SfVolD),2))
    if ( $SfVolT -le $CutOff) {
        Write-Host -ForegroundColor Red ($SfVolId, $SfVolName, $SfVolT)
    } else {
        Write-Host -ForegroundColor Green ($SfVolId, $SfVolName, $SfVolT)
    }
    $vol = @{
        id = $SfVolId
        name = $SfVolName
        compression = $SfVolC
        deduplication = $SfVolD
        total = $SfVolT
    }
    $SfVolEff.add($vol.id,$vol)
}

Write-Host "==== SUMMARY: LOW EFFICIENCY VOLUMES (Volume ID, Name, Efficiency Factor) ===="
ForEach ($k in $SfVolEff.keys) {
    ForEach ($kv in $SfVolEff[$k]) {
        if ($SfVolEff[$k]['total'] -le $CutOff) {
            Write-Host -ForegroundColor Red $SfVolEff[$k]['id'], $SfVolEff[$k]['name'], $SfVolEff[$k]['total']
        }
    }
}
