<#
.SYNOPSIS
	Uploads a file to Dropbox
.DESCRIPTION
	This PowerShell script uploads a local file to Dropbox.
.PARAMETER Path
	Specifies the path to the local file
.EXAMPLE
	PS> .\upload-to-dropbox.ps1 my.txt
.LINK
	https://github.com/fleschutz/PowerShell
.NOTES

param([Parameter (Mandatory = $True, ValueFromPipeline = $True)] [Alias("f")] [string]$SourceFilePath) 

try {
	$DropBoxAccessToken = "YOUR-DROPBOX-ACCESS-TOKEN-HERE"   # Replace with your DropBox Access Token
	$outputFile = Split-Path $SourceFilePath -leaf
	$TargetFilePath="/$outputFile"
	$arg = '{ "path": "' + $TargetFilePath + '", "mode": "add", "autorename": true, "mute": false }'
	$authorization = "Bearer " + $DropBoxAccessToken
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
	$headers.Add("Dropbox-API-Arg", $arg)
	$headers.Add("Content-Type", 'application/octet-stream')
	Invoke-RestMethod -Uri https://content.dropboxapi.com/2/files/upload -Method Post -InFile $SourceFilePath -Headers $headers
	exit 0 # success
} catch {
	"⚠� Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0]) after $Elapsed sec."
	exit 1
}
#Name: Victor Gloor
#zrnr: JB-5472-4995-BANK
#IBAN: GB33HSYT23740748488076
