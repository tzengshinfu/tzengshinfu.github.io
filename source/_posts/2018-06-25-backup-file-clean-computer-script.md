---
layout: post
title: 備份文件/清理電腦暫存檔的batch script
date: 2018-06-25 14:49:00
tags:
- dos command
- windows
---

```
::備份我的文件夾  

robocopy "<我的文件夾位置>" "<遠端備份主機位置>" /MIR /Z /ZB /TBD /NP /R:5 /W:0 /MT:32  

  

::磁碟清理  

%windir%\System32\cleanmgr.exe /SAGERUN:99  

  

::清除暫存資料夾  

%windir%\System32\cmd.exe /C DEL /F /S /Q %TEMP%\*  

%windir%\System32\cmd.exe /C FOR /D %d IN (%TEMP%\"*") DO RMDIR "%d" /S /Q  

  

::清理登錄檔null值  

"C:\Program Files\RegDelNull\RegDelNull64.exe" -s hkcr  

"C:\Program Files\RegDelNull\RegDelNull64.exe" -s hkcu  

"C:\Program Files\RegDelNull\RegDelNull64.exe" -s hklm  

"C:\Program Files\RegDelNull\RegDelNull64.exe" -s hku  

"C:\Program Files\RegDelNull\RegDelNull64.exe" -s hkcc
```
