---
title: 自訂PowerShell 6+指令別名
date: 2025-12-28 11:43:30
tags:
- powershell
---

1. 編輯設定檔。  
`
PS $env:USERPROFILE> notepad(或其他文字編輯器) $PROFILE
`

2. 寫入指令別名並存檔，如：  
`
function co {
    copilot --allow-all-tools --allow-all-paths @args
}
`

3. 即套用在新的PowerShell視窗。