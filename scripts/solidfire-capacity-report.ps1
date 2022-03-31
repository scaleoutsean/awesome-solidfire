#!/usr/bin/env pwsh
###############################################################################
# Synopsis:                                                                   #
# ./solidfire-capacity-report.ps1                                             #
#                                                                             #
# Version: 0.14                                                               #
#                                                                             #
# Blog post:                                                                  #
# scaleoutsean.github.io/2022/03/30/solidfire-capacity-report-html5.html      #
#                                                                             #
# NOTES:                                                                      #
# Before acting on info from this report, double-check with SF UI and HCC     #
# Thin Provisioning is not considered. Virtual Volumes are not listed         #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
#                                                                             #
# License:                                                                    #
#  -the GPL License 3.0 for HTML-related stuff                                #
#  -unknown license code that calculates capacity and efficiency (@kpapreck)  #
#  -the BSD License 3.0 for the rest                                          #
###############################################################################

Import-Module SolidFire.Core

# Required for HTML report
# Source code:
# https://github.com/qschweitzer/Powershell-HTML5-Reporting/
# Update and download a newer version if you decide to use it
Import-Module POSHTML5 -RequiredVersion 0.0.7

# If on Windows, use a Windows path instead
$outFile = '/tmp/report.html' # Linux
# $outFile = "C:\Windows\Temp\report.html" # Windows

# Security-wise it's better to not hard-code credentials
# Connect-SFCluster 192.168.1.34 -Username admin -Password admin 
$creds = Get-Credential
$conn = Connect-SFCluster -Credential $creds

# If you want to hide Volume and Account Names in the browser, set this to $True
# Casual inspection (cat report.html | grep string) shows no volume or account names with $True
$noName = $False

# You probably don't need to edit anything below

# Adopted and style-modified (formulae are the same) by scaleoutSean from:
# https://github.com/kpapreck/test-plan/blob/master/sf-efficiency.ps1

#GET CLUSTER NAME
$cluster_cap = Get-SFClusterCapacity
$cluster_info = Get-SFClusterInfo

# REQUIRED INPUTS
$nonZeroBlocks = $cluster_cap | Select-Object nonZeroBlocks -ExpandProperty nonZeroBlocks
$zeroBlocks = $cluster_cap | Select-Object zeroBlocks -ExpandProperty zeroBlocks
$uniqueBlocks = $cluster_cap | Select-Object uniqueBlocks -ExpandProperty uniqueBlocks
$uniqueBlocksUsedSpace = $cluster_cap | Select-Object uniqueBlocksUsedSpace -ExpandProperty uniqueBlocksUsedSpace
$snapshotNonZeroBlocks = $cluster_cap | Select-Object snapshotNonZeroBlocks -ExpandProperty snapshotNonZeroBlocks

# EFFICIENCY CALCULATIONS
[single]$thinProvisioningFactor = (($nonZeroBlocks + $zeroBlocks) / $nonZeroBlocks)
[single]$deDuplicationFactor = (($nonZeroBlocks + $snapshotNonZeroBlocks) / $uniqueBlocks)
[single]$compressionFactor = (($uniqueBlocks * 4096) / ($uniqueBlocksUsedSpace * .93))

# FOR DEBUGGING
#Write-Host $thinProvisioningFactor
#Write-Host $deDuplicationFactor
#Write-Host $compressionFactor

# CALCULATE EFFICIENCY FACTOR FOR COMPRESSION + DEDUPLICATION ONLY
$efficiencyFactor = ($deDuplicationFactor * $compressionFactor)

#CALCULATE FULL EFFICIENCY FACTOR FOR COMPRESSION + DEDUPLICATION + THIN PROVISIONING
$efficiencyFullFactor = ($deDuplicationFactor * $compressionFactor * $thinProvisioningFactor)

#GET THE CLUSTER ERROR THRESHOLD BYTES
$cluster_full_threshold = Get-SFClusterFullThreshold
$errorThreshold = $cluster_full_threshold | Select-Object stage4BlockThresholdBytes -ExpandProperty Stage4BlockThresholdBytes
$errorThresholdTB = ($errorThreshold / 1000 / 1000 / 1000 / 1000)

#GET THE TOTAL USED RAW CAPACITY
$sumUsedCapacity = $cluster_full_threshold | Select-Object sumUsedClusterBytes -ExpandProperty sumUsedClusterBytes
$sumUsed = ($sumUsedCapacity / 1000 / 1000 / 1000 / 1000)

#DETERMINE THE RAW SPACE AVAILABLE ON THE CLUSTER UNTIL ERROR THRESHOLD
$rawSpaceAvailableTB = (($errorThreshold - $sumUsedCapacity) / (1000 * 1000 * 1000 * 1000))

#DETERMINE THE RAW SPACE AVAILABLE ON THE CLUSTER UNTIL 100% FULL
$stage5BlockThresholdBytes = $cluster_full_threshold | Select-Object stage5BlockThresholdBytes -ExpandProperty stage5BlockThresholdBytes
$rawSpaceAvailable100TB = (($stage5BlockThresholdBytes - $sumUsedCapacity) / (1000 * 1000 * 1000 * 1000))

#GET TOTAL CLUSTER CAPCITY
$sumTotalClusterBytes = $cluster_full_threshold | Select-Object sumTotalClusterBytes -ExpandProperty sumTotalClusterBytes
$sumTotalClusterBytes = ($sumTotalClusterBytes / 1000 / 1000 / 1000 / 1000)

#GET CLUSTER FULL EFFECTIVE
$sumClusterFulldc = ($sumTotalClusterBytes * $efficiencyFactor) / 2
$sumClusterFulldct = ($sumTotalClusterBytes * $efficiencyFullFactor) / 2

#GET THE EFFECTIVE CAPACITY REMAINING OF COMPRESSION + DEDUPLICATION UNTIL ERROR THRESHOLD
$effectiveCapacityRemaining = ($rawSpaceAvailableTB * $efficiencyFactor) / 2

#GET THE EFFECTIVE CAPACITY OF COMPRESSION + DEDUPLICATION + THIN PROVISIONING UNTIL ERROR THRESHOLD
$effectiveFullCapacityRemaining = ($rawSpaceAvailableTB * $efficiencyFullFactor) / 2

#GET THE EFFECTIVE CAPACITY REMAINING OF COMPRESSION + DEDUPLICATION UNTIL 100% FULL
$effectiveCapacityRemaining100 = ((($stage5BlockThresholdBytes - $sumUsedCapacity) * $efficiencyFactor) / (1000 * 1000 * 1000 * 1000)) / 2

#FORMAT TO 2 DECIMALS
$efficiencyFactor = '{0:N2}' -f $efficiencyFactor
$efficiencyFullFactor = '{0:N2}' -f $efficiencyFullFactor
$rawSpaceAvailableTB = '{0:N2}' -f $rawSpaceAvailableTB
$effectiveCapacity = '{0:N2}' -f $effectiveCapacity
$sumTotalClusterBytes = '{0:N2}' -f $sumTotalClusterBytes
$effectiveCapacityRemaining = '{0:N2}' -f $effectiveCapacityRemaining
$sumClusterFulldc = '{0:N2}' -f $sumClusterFulldc
$sumClusterFulldct = '{0:N2}' -f $sumClusterFulldct
$effectiveCapacityRemaining100 = '{0:N2}' -f $effectiveCapacityRemaining100
$sumUsed = '{0:N2}' -f $sumUsed
$errorThresholdTB = '{0:N2}' -f $errorThresholdTB
$compressionFactor = '{0:N2}' -f $compressionFactor
$deDuplicationFactor = '{0:N2}' -f $deDuplicationFactor
$thinProvisioningFactor = '{0:N2}' -f $thinProvisioningFactor
$rawSpaceAvailable100TB = '{0:N2}' -f $rawSpaceAvailable100TB
$effectiveFullCapacityRemaining = '{0:N2}' -f $effectiveFullCapacityRemaining

Write-Host '--------------------------------------------------------------------------------------------------------------'
Write-Host "SolidFire Cluster: $($cluster_info.Name)-$($cluster_info.UniqueID)"
Write-Host "SolidFire Cluster MVIP: $($cluster_info.Mvip)"
Write-Host ''
Write-Host "Cluster RAW Capacity: $sumTotalClusterBytes TB"
Write-Host "Cluster RAW Capacity Error Stage: $errorThresholdTB TB"
Write-Host "Cluster RAW Capacity Used: $sumUsed"
Write-Host "Cluster Error Stage RAW TB Remaining Available: $rawSpaceAvailableTB TB"
Write-Host "Cluster 100% Full RAW TB Remaining Available: $rawSpaceAvailable100TB TB"

Write-Host ''
Write-Host 'Cluster Efficiencies'
Write-Host "Thin Provisioning Ratio: $thinProvisioningFactor"
Write-Host "Deduplication Ratio: $deDuplicationFactor"
Write-Host "Compression Ratio: $compressionFactor"
Write-Host "Cluster Deduplication/Compression Efficiency: $efficiencyFactor"
Write-Host "Cluster Deduplication/Compression/Thin Provisioning Efficiency: $efficiencyFullFactor"
Write-Host ''
Write-Host 'Cluster Capacity'
Write-Host "Cluster Effective Capacity @ 100% Full with Dedup/Comp: $sumClusterFulldc TB"
Write-Host "Cluster Effective Capacity @ 100% Full with Dedup/Comp/Thin: $sumClusterFulldct TB"
Write-Host "Effective Capacity Remaining until 100% Full with Dedup/Comp: $effectiveCapacityRemaining100 TB"
Write-Host "Effective Capacity Remaining until Error Threshold with Dedup/Comp: $effectiveCapacityRemaining TB"
Write-Host "Effective Capacity Remaining until Error Threshold with Dedup/Comp/Thin: $effectiveFullCapacityRemaining TB"
Write-Host '--------------------------------------------------------------------------------------------------------------'

# end of script adopted from @kpapreck

# this is a modified (current) version of Get-SfVolEff script
# https://github.com/scaleoutsean/awesome-solidfire/blob/master/scripts/get-sfvoleff.ps1
$CutOff = $args[0]
$SfVolEff = @()
$vs = (Get-SFVolume -ExcludeVVOLs)
if ($noName -eq $False) {
    $resourceProperty = 'Name'
}
else {
    $resourceProperty = 'VolumeID'
}
ForEach ($v in $vs) {
    $vol = @()
    $SfVolName = $v.Name; $SfVolId = $v.VolumeID
    $r = (Get-SFVolumeEfficiency -VolumeID $SfVolId | Select-Object -Property Compression, Deduplication)
    $SfVolC = ([MATH]::Round($r.Compression, 2)) ; $SfVolD = ([MATH]::Round($r.Deduplication, 2))
    $SfVolT = ([MATH]::Round(($SfVolC * $SfVolD), 2))
    $vol = ($SfVolName, $SfVolT)
    $VolEff = [PSCustomObject]@{
        'Name'       = $v.$resourceProperty
        'Size'       = $([MATH]::Round($v.TotalSize / (1024 * 1024 * 1024), 2))
        'Efficiency' = $SfVolT
    }
    $SfVolEff += $VolEff
}


# this section is from @kpapreck

$report = New-PWFPage -Title "SolidFire Capacity and Utilization Report for $($cluster_info.Name) (Cluster Unique ID: $($cluster_info.UniqueID))" -Content {
    New-PWFTabContainer -Tabs {
        New-PWFTab -Name 'Cluster Information' -Content {
            New-PWFCardHeader -BackgroundColor '#fff' -Center -Content {
                New-PWFTitles -TitleText "Cluster $($cluster_info.Name)-$($cluster_info.UniqueID)" -Size 1 -Center
            }
            New-PWFRow -Content {
                New-PWFColumn -Content {
                    New-PWFCard -BackgroundColor '#4f99f9' -Content {
                        New-PWFTitles -Size 3 -TitleText 'Effective capacity, TB (TiB)' -Center
                        New-PWFText -YourText "Dedup/Comp @ 100% Full: $sumClusterFulldc ($($sumClusterFulldc*0.9094947))"
                        New-PWFText -YourText "Dedup/Comp/Thin @ 100% Full: $sumClusterFulldct ($($sumClusterFulldct*0.9094947))"
                        New-PWFText -YourText "Dedup/Comp Cap until 100% Full: $effectiveCapacityRemaining100 ($($effectiveCapacityRemaining100*0.9094947))"
                        New-PWFText -YourText "Dedup/Comp Cap until Error: $effectiveCapacityRemaining ($($effectiveCapacityRemaining*0.9094947))"
                        New-PWFText -YourText "Dedup/Comp/Thin until Error: $effectiveFullCapacityRemaining ($($effectiveFullCapacityRemaining*0.9094947))"
                    }
                }
                New-PWFColumn -Content {
                    New-PWFCard -BackgroundColor '#4f99f9' -Content {
                        New-PWFTitles -Size 3 -TitleText 'Raw capacity, TB (TiB)' -Center
                        New-PWFText -YourText "Raw Capacity: $sumTotalClusterBytes ($($sumTotalClusterBytes*0.9094947))"
                        New-PWFText -YourText "Raw Capacity Error Level: $errorThresholdTB ($($errorThresholdTB*0.9094947))"
                        New-PWFText -YourText "Raw Capacity Used: $sumUsed ($($sumUsed*0.9094947))"
                        New-PWFText -YourText "Error Level Raw Remaining: $rawSpaceAvailableTB ($($rawSpaceAvailableTB*0.9094947))"
                        New-PWFText -YourText "100% Full Raw Remaining: $rawSpaceAvailable100TB ($($rawSpaceAvailable100TB*0.9094947))"
                    }
                }
                New-PWFColumn -Content {
                    New-PWFCard -BackgroundColor '#4f99f9' -Content {
                        New-PWFTitles -Size 3 -TitleText 'Efficiency' -Center
                        New-PWFText -YourText "Thin Provisioning: $thinProvisioningFactor x"
                        New-PWFText -YourText "Deduplication: $deDuplicationFactor x"
                        New-PWFText -YourText "Compression: $compressionFactor x"
                        New-PWFText -YourText "Dedupe/Compr: $efficiencyFactor x"
                        New-PWFText -YourText "Dedupe/Compr/Thin: $efficiencyFullFactor x"
                    }
                }
            }
            New-PWFRow -Content {
                New-PWFColumn -Content {
                    New-PWFCard -BackgroundColor '#19314f' -Content {
                        New-PWFTitles -Size 3 -TitleText 'Top volumes by size' -Center -LightMode
                        if ($noName -eq $False) {
                            $resourceProperty = 'Name'
                        }
                        else {
                            $resourceProperty = 'VolumeID'
                        }
                        $Chart2Dataset = Get-SFVolume | `
                            Select-Object -Property @{Name = 'TotalSize'; expression = { [math]::Round($_.TotalSize / (1024 * 1024 * 1024), 2) } }, $resourceProperty | `
                            Sort-Object Size -Descending | Select-Object -First 10
                        New-PWFChart -ChartTitle 'Volume Size (GiB)' -ChartType 'bar' -ChartLabels $($Chart2Dataset.$resourceProperty) -ChartValues ($Chart2Dataset | Select-Object -ExpandProperty TotalSize) -LightMode
                    }
                }
                New-PWFColumn -Content {
                    New-PWFCard -BackgroundColor '#a43465' -Content {
                        New-PWFTitles -Size 3 -TitleText 'Low efficiency (Dedup*Comp) volumes (GiB)' -Center -LightMode
                        New-PWFTable -ToTable ($SfVolEff | Sort-Object -Property Efficiency) -SortByColumn -Small
                    }
                }
            }
        }
        New-PWFTab -Name 'Accounts and Volumes' -Content {
            New-PWFRow -Content {
                New-PWFColumn -Content {
                    New-PWFCard -BackgroundColor '#4f99f9' -Content {
                        New-PWFTitles -Size 3 -TitleText 'Storage (Tenant) Accounts'
                        New-PWFText -YourText 'View, filter, search and export accounts.'
                        if ($noName -eq $False) {
                            New-PWFTable -ToTable (Get-SFAccount | `
                                    Select-Object -Property AccountID, Username, @{Name = 'Volumes'; expression = { ($_.Volumes.Count) } } | `
                                    Sort-Object -Property Username -Stable) `
                                -Pagination -DetailsOnClick -SortByColumn -ShowTooltip -EnableSearch -Exportbuttons -ContextualColor dark -Striped
                        }
                        else {
                            New-PWFTable -ToTable (Get-SFAccount | `
                                    Select-Object -Property AccountID, @{Name = 'Volumes'; expression = { ($_.Volumes.Count) } } | `
                                    Sort-Object -Property AccountID -Stable) `
                                -Pagination -DetailsOnClick -SortByColumn -ShowTooltip -EnableSearch -Exportbuttons -ContextualColor dark -Striped                            
                        }
                    }
                }
                New-PWFColumn -Content {
                    New-PWFCard -BackgroundColor '#4f99f9' -Content {
                        New-PWFTitles -Size 3 -TitleText 'Volumes' -Center
                        New-PWFText -YourText 'View, filter, search and export volumes. vVols are not listed. Size unit: GiB.'
                        if ($noName -eq $False) {
                            New-PWFTable -ToTable (Get-SFVolume -ExcludeVVOLs | Select-Object -Property VolumeID, Name, @{Name = 'TotalSize'; expression = { [math]::Round($_.TotalSize / (1024 * 1024 * 1024), 2) } }, `
                                    AccountID | Sort-Object -Property Name -Stable) `
                                -Pagination -DetailsOnClick -SortByColumn -ShowTooltip -EnableSearch -Exportbuttons -ContextualColor dark -Striped
                        }
                        else {
                            New-PWFTable -ToTable (Get-SFVolume -ExcludeVVOLs | Select-Object -Property VolumeID, @{Name = 'TotalSize'; expression = { [math]::Round($_.TotalSize / (1024 * 1024 * 1024), 2) } }, `
                                    AccountID | Sort-Object -Property VolumeID -Stable) `
                                -Pagination -DetailsOnClick -SortByColumn -ShowTooltip -EnableSearch -Exportbuttons -ContextualColor dark -Striped
                        }
                    }
                }
            }
        }
    }
}

$report | Out-File -Encoding UTF8 -FilePath $outFile
