#!/usr/bin/env pwsh
###############################################################################
# Demonstrates how to connect to NetApp Hybrid Cloud Control (HCC)            #
#   and get a list of compute assets (nodes) known to HCC                     #
#                                                                             #
# Requirement: PowerShell 7 (Win, Lin)                                        #
#                                                                             #
# Author: @scaleoutSean                                                       #
# https://github.com/scaleoutsean/awesome-solidfire                           #
# scaleoutsean.github.io/2021/12/21/netapp-solidfire-hci-hcc-powershell.html  #
# License: the BSD License 3.0                                                #
###############################################################################

$multipartContent = [System.Net.Http.MultipartFormDataContent]::new()
$stringHeader = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new("form-data")
$stringHeader.Name = "client_id"
$StringContent = [System.Net.Http.StringContent]::new("mnode-client")
$StringContent.Headers.ContentDisposition = $stringHeader
$multipartContent.Add($stringContent)

$stringHeader = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new("form-data")
$stringHeader.Name = "username"
# replace 'administrator' with your own mNode user name
$StringContent = [System.Net.Http.StringContent]::new("administrator")
$StringContent.Headers.ContentDisposition = $stringHeader
$multipartContent.Add($stringContent)

$stringHeader = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new("form-data")
$stringHeader.Name = "password"
# replace 'NetApp123' with your own mNode admin's password
$StringContent = [System.Net.Http.StringContent]::new("NetApp123")
$StringContent.Headers.ContentDisposition = $stringHeader
$multipartContent.Add($stringContent)

$stringHeader = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new("form-data")
$stringHeader.Name = "grant_type"
$StringContent = [System.Net.Http.StringContent]::new("password")
$StringContent.Headers.ContentDisposition = $stringHeader
$multipartContent.Add($stringContent)

$body = $multipartContent

# replace hcc.add.r.ess with IP or FQDN and if you have FQDN and a good TLS cert, use SkipCertificateCheck:$False
$response = Invoke-RestMethod 'https://hcc.add.r.es/token' -Method 'POST' -Headers $headers -Body $body -SkipCertificateCheck:$True
$token    = $response.access_token

$headers = @{
    Authorization="Bearer $token"
}

# replace hcc.add.r.ess with IP or FQDN and if you have FQDN and a good TLS cert, use SkipCertificateCheck:$False
$allassets= (Invoke-WebRequest 'https://hcc.add.r.es/mnode/assets' -Method 'GET' -Headers $headers -SkipCertificateCheck:$True).Content | ConvertFrom-Json

foreach ($c in $allassets.compute) {
    Write-Host "Host:", $c.host_name, "IP:", $c.ip
}
