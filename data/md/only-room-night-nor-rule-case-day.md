*cd-videos.ps1*
================

This PowerShell script changes the working directory to the user's videos folder.

Parameters
----------
```powershell
PS> ./cd-videos.ps1 [<CommonParameters>]

[<CommonParameters>]
    This script supports the common parameters: Verbose, Debug, ErrorAction, ErrorVariable, WarningAction, 
    WarningVariable, OutBuffer, PipelineVariable, and OutVariable.
```

Example
-------
```powershell
PS> ./cd-videos
📂C:\Users\Markus\Videos

```

Notes
-----

Related Links
-------------
https://github.com/fleschutz/PowerShell

Script Content
--------------
```powershell

try {
	if ($IsLinux) {
		$Path = Resolve-Path "$HOME/Videos"
	} else {
		$Path = [Environment]::GetFolderPath('MyVideos')
	}
	if (-not(Test-Path "$Path" -pathType container)) { throw "Videos folder at 📂$Path doesn't exist (yet)" }
	Set-Location "$Path"
	"📂$Path"
	exit 0 # success
} catch {
	"⚠� Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
```

*(generated by convert-ps2md.ps1 using the comment-based help of cd-videos.ps1 as of 09/01/2023 17:51:48)*