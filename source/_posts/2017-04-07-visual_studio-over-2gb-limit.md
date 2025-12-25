---
layout: post
title: Visual Studio突破2GB Memory使用限制
date: 2017-04-07 16:39:00
tags:
- visual studio
---

在[Visual Studio 2013]>>[開發人員命令提示字元]

按右鍵選單以系統管理員身分執行

輸入editbin /LARGEADDRESSAWARE devenv.exe

(原有執行檔建議先備份)

[![](Image_20170407163554.png)](Image_20170407163554.png )

  
  
參考:[[Visual Studio]使用Editbin命令讓Visual Studio突破2GB Memory使用限制](https://dotblogs.com.tw/larrynung/2011/11/03/50945 "https://dotblogs.com.tw/larrynung/2011/11/03/50945")

