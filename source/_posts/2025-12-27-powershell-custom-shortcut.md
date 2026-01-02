---
title: 自訂PowerShell 6+快捷鍵
date: 2025-12-27 18:08:59
tags:
- powershell
---

1. 列出已綁定的快捷鍵。  
`
PS $env:USERPROFILE> Get-PSReadLineKeyHandler
`

2. 列出其他未綁定的快捷鍵。  
`
PS $env:USERPROFILE> Get-PSReadLineKeyHandler -Unbound
`

3. 要綁定的快捷鍵功能可參考上述指令結果。

4. 編輯設定檔。  
`
PS $env:USERPROFILE> notepad(或其他文字編輯器) $PROFILE
`

5. 寫入新的快捷鍵並存檔，如：  
`
Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete
Set-PSReadLineKeyHandler -Key Ctrl+k -Function ForwardDeleteInput
Set-PSReadLineKeyHandler -Key Ctrl+RightArrow -Function ForwardWord
`

6. 即套用在新的PowerShell視窗。