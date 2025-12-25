---
layout: post
title: 每日排程刪除資源回收筒(保留一段時間)
date: 2023-06-26 16:19:00
tags:
- powershell
- windows
---
1.安裝最新PowerShell  
2.建立PowerShell script檔，內容為

```
[cmdletbinding()]
param(
    [parameter(Mandatory)]
    [ValidateNotNullorEmpty()]
    $RetentionDays
)

# 目前時間-保留天數=最早保留時間
$RetentionTime = (Get-Date).AddDays(-1 * $RetentionDays)

$Shell = New-Object -ComObject Shell.Application
$RecyclerBin = $Shell.NameSpace(10)

if ($RecyclerBin)
{
    $RecyclerBinFiles = $RecyclerBin.Items()

    foreach ($RecyclerBinFile in $RecyclerBinFiles)
    {
        # 檔案刪除時間
        $DeleteTime = Get-Date ($RecyclerBin.GetDetailsOf($RecyclerBinFile, 2) -replace "\u200f|\u200e", "")

        # 當檔案刪除時間早於最早保留時間時則刪除
        if ($DeleteTime -lt $RetentionTime)
        {
            Remove-Item -Path $RecyclerBinFile.Path -Confirm:$false -Force -Recurse
        }
    }
}
```

3.建立工作排程器工作，  
程式或指令碼："C:\Program Files\PowerShell\7\pwsh.exe"  
新增引數 (可省略)：-NoProfile -ExecutionPolicy Bypass -File "{script檔路徑}" -RetentionDays {保留天數}  
  
參考來源：[Delete old files in recycle bin with powershell - Stack Overflow](https://stackoverflow.com/a/22816296 "https://stackoverflow.com/a/22816296")
