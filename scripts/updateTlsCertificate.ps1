#!/usr/bin/env pwsh 

# This script prompts the user to paste TLS certificate and private key in the usual, stupid format and uploads them to SolidFire MVIP.
# 1) You don't need this for properly formatted 1-line PEM files. Although you can reference the CLI line that should suffice in your case.
#    One may want to repurpose this for TLS cert expiration checking, for example.
# 2) EC private keys are not supported by SolidFire API (at least not in 12.5?), so you need to get RSA certificate.
# 3) SolidFire PowerShell Tools is require here. Install it from the PowerShell Gallery with: Install-Module -Name SolidFire -Scope CurrentUser -Force

# Usage: .\updateTlsCertificate.ps1 -mvip <MVIP> -username <Username> -password <Password> -certificateFile <CertificateFile> -privateKeyFile <PrivateKeyFile>

# License: MIT License 2.0
# (c) 2025, @scaleoutSean

param(
    [string]$mvip,
    [string]$username,
    [string]$password,
    [string]$certificateFile,
    [string]$privateKeyFile
)

# Require version PowerShell 5.1
if ($PSVersionTable.PSVersion.Major -lt 5 -or ($PSVersionTable.PSVersion.Major -eq 5 -and $PSVersionTable.PSVersion.Minor -lt 1)) {
    Write-Host "This script requires PowerShell version 5.1. SolidFire PowerShell Tools don't seem to work with PS 7.5 on Windows Server 2025." -ForegroundColor Red
    exit 1
}

# try to import SolidFire PowerShell Tools module
try {
    Import-Module -Name "SolidFire" -ErrorAction Stop
} catch {
    Write-Host "SolidFire PowerShell Tools module not found. Please install it using: Install-Module -Name SolidFire -Scope CurrentUser" -ForegroundColor Red
    exit 1
}

# Check if required parameters are provided
if (-not $mvip -or -not $username -or -not $password -or -not $certificateFile -or -not $privateKeyFile) {
    Write-Host "Usage: .\updateTlsCertificate.ps1 -mvip <MVIP> -username <Username> -password <Password> -certificateFile <CertificateFile> -privateKeyFile <PrivateKeyFile>" -ForegroundColor Red
    exit 1
}

# Example: Convert a PEM file with the usual stupid line breaks and endings to single-line suitable for SolidFire API
function Unfuck-PemFile {
    param (
        [string]$FilePath
    )
    $lines = Get-Content -Path $FilePath | Where-Object { $_.Trim() -ne "" }
    $header = $lines[0]
    $footer = $lines[-1]
    $pemBlocks = @()
    $currentBlock = @()
    foreach ($line in $lines) {
        if ($line -match '^-----BEGIN ') {
            if ($currentBlock.Count -gt 0) {
                $pemBlocks += ,$currentBlock
                $currentBlock = @()
            }
        }
        $currentBlock += $line
        if ($line -match '^-----END ') {
            $pemBlocks += ,$currentBlock
            $currentBlock = @()
        }
    }
    # Convert each block (Cert + IA) to single line with \n between header, body, and footer
    $result = $pemBlocks | ForEach-Object {
        $block = $_
        $header = $block[0]
        $footer = $block[-1]
        $body = ($block[1..($block.Count-2)] -join "") # join body lines with no separator
        "$header`n$body`n$footer"
    }
    return ($result -join "`n")
}


# Main script execution
$global:conn = Connect-SFCluster $mvip -Username $username -Password $password

if (-not $global:conn) {
    Write-Host "Failed to connect to SolidFire cluster at $mvip." -ForegroundColor Red
    exit 1
}

try {
    
    # Read certificate and key from user input
    if (-not (Test-Path -Path $certificateFile)) {
        Write-Host "Certificate file not found: $certificateFile" -ForegroundColor Red
        exit 1
    }

    if (-not (Test-Path -Path $privateKeyFile)) {
        Write-Host "Private key file not found: $privateKeyFile" -ForegroundColor Red
        exit 1
    }

    $certificate = Unfuck-PemFile -FilePath $certificateFile
    $privateKey = Unfuck-PemFile -FilePath $privateKeyFile

    Set-SFSSLCertificate -Certificate $certificate -PrivateKey $privateKey -Confirm:$false
    
    if ($?) {
        Write-Host "TLS certificate and private key updated successfully." -ForegroundColor Green        
    } else {
        Write-Host "Failed to update TLS certificate and private key." -ForegroundColor Red
        exit 1
    }
    
    # Get the cert to see what we have done

    $cert= Get-SFSSLCertificate -ErrorAction Stop
    $certJson = $cert | ConvertTo-Json -Depth 3
    $certObj = $cert | ConvertTo-Json -Depth 3 | ConvertFrom-Json
    $certDates = @()    
    
    $notBeforeRaw = $certObj.Details.notBefore
    $notBefore = [DateTime]::Parse($notBeforeRaw)
    $certSDateBefore = [PSCustomObject]@{
        Validity   = "NotBefore"
        Subject    = $certObj.Details.subject
        DateTime   = $notBefore
    }
    $certDates += $certSDateBefore
    $notAfterRaw = $certObj.Details.notAfter
    $notAfter = [DateTime]::Parse($notAfterRaw)
    $certSDateAfter = [PSCustomObject]@{
        Validity   = "NotAfter"
        Subject    = $certObj.Details.subject
        DateTime   = $notAfter
    }
    $certDates += $certSDateAfter
    # Print nice table with $certDates
    $certDates | Format-Table -AutoSize -Property Validity, DateTime, Subject

    Write-Host "Full TLS certificate details:" -ForegroundColor Yellow 
    Write-Host $certJson -ForegroundColor Cyan

    $password = $null  # Clear the password variable

} catch {
    Write-Host "An error occurred: $_" -ForegroundColor Red
    $password = $null  # Clear the password variable
    exit 1
}


