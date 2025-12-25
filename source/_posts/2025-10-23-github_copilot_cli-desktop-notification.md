---
layout: post
title: GitHub Copilot CLI工作完成發送桌面通知
date: 2025-10-23 20:07:00
tags:
- github copilot cli
- windows
---
目前v0.0349無hook可設定在執行事件前後觸發，

但可以用系統層級的提示詞達到相同目的。

1.安裝PowerShell模組
`Install-Module -Name BurntToast -Scope CurrentUser`

2.在系統層級提示詞%USERPROFILE%\.copilot\copilot-instructions.md新增

- The PowerShell module `BurntToast` has been installed on this machine. You must send me a notification after each work. Execute the PowerShell command `New-BurntToastNotification -Text "{title}", "{content}" -Sound Alarm2`

[![](Capture_20251023_164252.png)](Capture_20251023_164252.png )

