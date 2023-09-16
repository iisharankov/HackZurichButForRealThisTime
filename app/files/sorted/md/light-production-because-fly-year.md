*close-microsoft-paint.ps1*
================

This PowerShell script closes the Microsoft Paint application gracefully.

Parameters
----------
```powershell
PS> ./close-microsoft-paint.ps1 [<CommonParameters>]

[<CommonParameters>]
    This script supports the common parameters: Verbose, Debug, ErrorAction, ErrorVariable, WarningAction, 
    WarningVariable, OutBuffer, PipelineVariable, and OutVariable.
```

Example
-------
```powershell
PS> ./close-microsoft-paint.ps1

```

Notes
-----

Related Links
-------------
https://github.com/fleschutz/PowerShell

Script Content
--------------
```powershell

TaskKill /im mspaint.exe
if ($lastExitCode -ne "0") {
	& "$PSScriptRoot/speak-english.ps1" "Sorry, Microsoft Paint isn't running."
	exit 1
}
exit 0 # success
```

*(generated by convert-ps2md.ps1 using the comment-based help of close-microsoft-paint.ps1 as of 09/01/2023 17:51:49)*