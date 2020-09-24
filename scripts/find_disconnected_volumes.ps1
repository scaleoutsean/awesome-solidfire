###############################################################################
#                                                                             #
# Find volumes without active connections (possible junk)                     #
# NOTE: SolidFire volumes are distinguished by unique Volume ID               #
#       Volume Names can be duplicate. Decimate wisely!                       #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# License: the BSD License 3.0                                                #
###############################################################################

$SolidFireClusterIp = Read-Host -Prompt "Enter the SolidFire Management IP/FQDN" 
$SolidFireConnection = Connect-SFCluster $SolidFireClusterIp -Credential (Get-Credential)
$accList = (Get-SFAccount) ; $volList = @()
ForEach ($acc in $accList) { 
  $vols = Get-SFVolume -AccountID $acc.AccountID
  ForEach ($v in $vols) { $volList = $volList + $v.VolumeID }}
$volActiveList = @(); $Sessions = Get-SfIscsiSession
ForEach ($s in $Sessions) { $volActiveList = $volActiveList + $s.VolumeID }
$volIdleList = ($volList | ? { $volActiveList -notcontains $_})
ForEach ($v in $volIdleList){ Write-Host (Get-SFVolume -VolumeID $v).Name }
