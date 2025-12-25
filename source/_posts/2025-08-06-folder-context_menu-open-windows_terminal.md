---
layout: post
title: 在資料夾右鍵新增"在終端中開啟"(WindowsTerminal)
date: 2025-08-06 11:46:00
tags:
- windows 11
- windows terminal
---

```
將以下內容另存.reg檔，修改[WindowsTerminal路徑(以兩個反斜線區隔)]並匯入登錄檔：
```

```
Windows Registry Editor Version 5.00  
  
[HKEY_CLASSES_ROOT\Directory\shell\wt]  
@="在終端中開啟"  
"Icon"="\"%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\wt.exe\""  
  
[HKEY_CLASSES_ROOT\Directory\shell\wt\command]  
@="\"%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\wt.exe\" -d \"%V\""
```
