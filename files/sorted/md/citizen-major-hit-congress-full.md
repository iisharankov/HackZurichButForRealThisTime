*open-xing.ps1*
================

This script launches the XING application.

Parameters
----------
```powershell
PS> ./open-xing.ps1 [<CommonParameters>]

[<CommonParameters>]
    This script supports the common parameters: Verbose, Debug, ErrorAction, ErrorVariable, WarningAction, 
    WarningVariable, OutBuffer, PipelineVariable, and OutVariable.
```

Example
-------
```powershell
PS> ./open-xing

```

Notes
-----

Related Links
-------------
https://github.com/fleschutz/PowerShell

Script Content
--------------
```powershell

Start-Process xing:
exit 0 # success
```

*(generated by convert-ps2md.ps1 using the comment-based help of open-xing.ps1 as of 09/01/2023 17:51:54)*
