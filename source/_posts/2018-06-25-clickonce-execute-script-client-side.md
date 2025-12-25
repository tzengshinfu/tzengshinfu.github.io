---
layout: post
title: clickonce執行script(Client端)
date: 2018-06-25 18:15:00
tags:
- clickonce
- dos command
- visual studio
- windows form
---

```
 @ECHO OFF  
 SET APP=%1  
 ::此script檔執行需帶參數=%APP%  
   
 ::建置ClickOnce專案  
 "MSBuild.exe" "<專案名稱>.csproj" /target:publish /property:Configuration=Debug;PublishUrl=\\<主機名稱>\%APP%;AssemblyName=%APP%;PublisherName=<公司名稱>;ProductName=%APP%;ApplicationRevision=1;MinimumRequiredVersion=1.0.0.1  
   
 ::建立Deploy資料夾  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create 'cmd.exe /c mkdir C:\%APP%'  
   
 ::Deploy資料夾權限:everyone, 執行  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create 'cmd.exe /c icacls C:\%APP% /grant "everyone:RX"'  
   
 ::複製專案到資料夾  
 robocopy <專案名稱>\bin\Debug\app.publish \\<主機名稱>\C$\%APP% /MIR /Z /ZB /TBD /NP /R:5 /W:0 /MT:32
```
