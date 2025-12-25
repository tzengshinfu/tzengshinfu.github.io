---
layout: post
title: Nuget無法取得套件清單，顯示"無法建立 SSL/TLS 的安全通道"的錯誤
date: 2021-07-19 12:04:00
tags:
- ".net core"
- ".net framework"
- dos command
---

[![](Image_20210719113923.png)](Image_20210719113923.png )

原因：Nuget於2020/04移除對TLS 1.0/1.1的支援。

對策：執行以下指令即可。

```
reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client" /v DisabledByDefault /t REG_DWORD /d 0 /f /reg:32
reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client" /v DisabledByDefault /t REG_DWORD /d 0 /f /reg:64
reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client" /v Enabled /t REG_DWORD /d 1 /f /reg:32
reg add "HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client" /v Enabled /t REG_DWORD /d 1 /f /reg:64
```

參考：[Deprecating TLS 1.0 and 1.1 on NuGet.org](https://devblogs.microsoft.com/nuget/deprecating-tls-1-0-and-1-1-on-nuget-org/ "https://devblogs.microsoft.com/nuget/deprecating-tls-1-0-and-1-1-on-nuget-org/")

