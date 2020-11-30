<#
    .SYNOPSIS
        Set exceptional (or restore previous) storage QoS policy on a volume.

    .DESCRIPTION
        This module applies or restores a storage QoS policy to 
        SolidFire volume uniquely identified by Name or ID. Use cases include
        pre- & post-backup scripts and similar temporary QoS assignments.

        Volumes Name must be 5 alphanumeric characters or longer and unique in 
        the SolidFire cluster. 
        Volume ID must be 4 or fewer numeric characters.
        Volumes without QoS Policy are rejected for simplicity and robustness.

        If SFQosPolicyId is not provided, Set-SFQosException restores QoS Policy ID 
        stored in the Volume's Attributes using the value from the "SfQosId" key. 
        
        The SfQosId key and value areadded to Volume Attributes when SFQosPolicyId 
        is used, unless SFQosPolicyId is the same as existing SfQosId in which case 
        Set-SFQoSException exists with error.
        Use Set-SFQosException without passing SFQosPolicyId to reset Volume's QoS to 
        SfQosId.
        
        Set-SFQosException cannot track change to QoS policy by other programs. In 
        order to prevent SFQoSId get out of sync with QoS settings for the volume, 
        refrain from modifying Volume QoS Policy before SFQosId is used to reset volume.
        
        If Volume QoS Policy ID is independently changed, leaving SfQosId out of sync, 
        cmdlet will be unable to run with SFQosPolicyId value equal to SfQosId because 
        they're identical (although the Volume QoS Policy value is different).
        Run cmdlet with SFQosPolicyId set to current Volume QoS Policy ID to "recover." 
        That will set the SfQosId Attribute value to the same value as current 
        Volume QoS Policy ID.

        VVOLs are not supported. Custom QoS settings are currently also not supported.
    
    .INPUTS
    	VolumeNameOrId, SFQosPolicyId

    .OUTPUTS
        None

    .PARAMETER VolumeNameOrID 
        VolumeNameOrID to work on

    .PARAMETER SFQosPolicyId
        Storage QoS Policy ID to apply on the volume

    .EXAMPLE
        Set-SFQosException -VolumeNameOrID ora -SFQosPolicyId 3
        
        Set temporary SolidFire QoS Policy ID 3 to a volume uniquely identified by 
        the name "ora". Current SF Storage QoS Policy ID is saved to the volume attributes.

        Set-SFQosException -VolumeNameOrID 77

        Restore storage QoS Policy from the value of the key "SfQosId" in Volume Attributes for
        Volume ID 77. If SFQosId attribute does not exist or has no value, exit with error.
    
    .NOTES
        FunctionName: Set-SFQosException
        Created by  : scaleoutSean (github.com/scaleoutsean)
        Date        : 2020/11/28
        License     : The BSD 3.0 License

    .LINK
        https://github.com/scaleoutsean/awesome-solidfire

#>

function Set-SFQosException {
    [CmdletBinding()]
    Param(
        [Parameter(Mandatory=$true, ValueFromPipeline=$true)]
        [ValidateNotNullOrEmpty()]
        [String]
        $VolumeNameOrId,

        [Parameter(Mandatory=$false)]
        [String]
        $SFQosPolicyId
    )

    Begin {
        $ErrorActionPreference = "Stop"

        function IfUniqueVolNameExists {
            param (
                [String]$VolumeNameorId
            )
            $VolList = (Get-SFVolume -Name $VolumeNameOrId -ExcludeVVOLs)
            if ((($VolList.Length) -gt 1) -or (($VolList.Length) -eq 0)) {
                Write-Host "Volume Name found:" $VolList 
                Write-Error -Message "ERROR: Volume Name provided does not exist or is not unique"
            } else {
                $SFVolumeId = ($VolList[0].VolumeID)
                return $SFVolumeId
            }
        }

        function IfVolumeIdExists {
            param (
                [String]$VolumeNameOrId
            )
            try {
                $SFVolumeID = (Get-SFVolume -VolumeID $VolumeNameOrId -ExcludeVVOLs).VolumeID
            } catch {
                Write-Error -Message "ERROR: VolumeNameOrId has 4 or less numeric characters but cannot be found by ID"
            }
            return $SFVolumeID
        }

        function SetAction {
            param (
                [String]$SFQosPolicyId
            )
            try {
                $QosId = (Get-SFQoSPolicy -QoSPolicyID $SFQosPolicyId).QoSPolicyID
            } catch {
                Write-Error -Message "ERROR: Unable to find target SFQosPolicyId:" $SFQosPolicyId
                break
            }
            if ($QoSId) {
                return $true
            }
        }
                
        if ($VolumeNameOrId.length -gt 4 -or $VolumeNameOrId -match '[a-zA-Z-]') {
            $SFVolumeId = (IfUniqueVolNameExists -VolumeNameorId $VolumeNameorId)
        } else {
            $SFVolumeId = (IfVolumeIdExists -VolumeNameOrId $VolumeNameOrId)
        }

        if ($SFQosPolicyId.length -eq 0) {
            $SetQoSAction = $false
        } else {
            $SetQoSAction = (SetAction -SFQosPolicyId $SFQosPolicyId)
        }

        $SFVolumeQosId = (Get-SFVolume -VolumeID $SFVolumeId).QoSPolicyID
        if ($null -eq $SFVolumeQosId) {
            Write-Error -Message "ERROR: volume must have existing QoS Policy ID to apply a new QoS Policy ID"
            break
        }

    }
  
    Process {
        
        $SFVolumeAttrs = (Get-SFVolume -VolumeID $SFVolumeId).Attributes
        if ($SFVolumeAttrs.SfQosId -eq $SFQosPolicyId) {
            Write-Host "WARNING: New and existing QoS Policy ID are identical to SfQosId" -ForegroundColor DarkYellow
            Write-Error -Message "ERROR: To reset the Volume QoS to SfQosId value, run this cmdlet without SFQosPolicyId parameter"
        }
        
        if ($SetQoSAction -eq $true) {
            $SFVolumeQosKv = @{}
            if ($null -eq $SFVolumeAttrs.SfQosId) {
                $SFVolumeQosKv.Add("SfQosId",$SFVolumeQosId)
                $SFVolumeAttrs = $SFVolumeAttrs + $SFVolumeQosKv
            } else {
                $SFVolumeAttrs.SfQosId = $SFVolumeQosId
            }
            Set-SFVolume -VolumeID $SFVolumeId -QoSPolicyID $SFQosPolicyId -Attributes $SFVolumeAttrs -Confirm:$false | out-null
        } else {
            Write-Host "Resetting QoS for Volume ID:" $SFVolumeID
            if ($SFVolumeAttrs.SfQosId -match '^\d$' -and $SFVolumeAttrs.SfQosId -ne $SFVolumeQosId) {
                Set-SFVolume -VolumeID $SFVolumeId -QoSPolicyId $SFVolumeAttrs.SfQosId -Confirm:$false | out-null
            } else {
                Write-Host "WARNING: No valid SfQosId volume attribute found or QoS Policy unchanged for Volume ID:" $SFVolumeID -ForegroundColor DarkYellow
            }
        }
    }

    End { }

}
