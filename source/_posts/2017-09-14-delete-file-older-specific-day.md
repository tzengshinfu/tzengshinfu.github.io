---
layout: post
title: 刪除特定天數以前的檔案
date: 2017-09-14 12:26:00
tags:
- dos command
---
通常使用forfiles指令去遍歷某路徑下的檔案並執行刪除  
 如:

```
 forfiles /P "D:\xx"[路徑] /D -3[天數] /C "cmd /c del /q /f @file"
```

  
 若要刪除遠端主機的檔案(路徑格式為\\xx\xx\xx = UNC格式)，  
 但因為forfiles不支援UNC格式，  
 除了使用網路磁碟機對應(\\xx\xx\xx→X:\)，  
 還可以使用以下指令:  

```
 PushD "\\xx\xx\xx"[UNC路徑] &&(  
 forfiles /D -3[天數] /C "cmd /c del /q /f @file"  
 ) & PopD
```
