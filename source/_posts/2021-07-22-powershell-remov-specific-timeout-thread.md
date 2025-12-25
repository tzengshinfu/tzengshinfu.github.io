---
layout: post
title: PowerShell刪除啟動已逾期的特定執行緒
date: 2021-07-22 15:47:00
tags:
- powershell
---

```
param([Int32]$second=10<# 逾期秒數 #>)

Get-Process | ForEach-Object {
    if ($_.ProcessName -eq "EXCEL"<# 要尋找的執行序名稱 #>) {
        $commandline = Get-CimInstance Win32_Process -Filter "ProcessId = '$($_.Id)'" | Select Commandline

        if ($commandline -like '*automation*'<# 當命令列包含特定文字 #>) {
            if ((NEW-TIMESPAN -Start $_.StartTime -End (Get-Date)).TotalSeconds -ge $second) {
                Stop-Process -Id $_.Id
            }
        }    
    }
}
```
