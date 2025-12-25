---
layout: post
title: 將Visual Studio快取資料夾移到Ram disk以加快編譯速度
date: 2020-03-04 10:36:00
tags:
- visual studio
---

將以下資料夾移到Ram disk可增進Visual Studio編譯速度
**1.Visual Studio**
在C:\Users\{使用者帳號}\Appdata\Local\Microsoft\VisualStudio\{版本號}下
[組件緩存資料夾]
\ComponentModelCache
[專案Assembly快取資料夾]
\ProjectAssemblies
[其他快取資料夾]

\Designer\ShadowCache

\ImageLibrary

※2019新增
\TextMateCache

**2.專案**
[各專案編譯輸出資料夾]
\{專案目錄}\bin

\{專案目錄}\obj
[Assembly快取資料夾]
C:\Users\{使用者帳號}\AppData\Local\assembly
**3.ASP.NET**
[編譯暫存資料夾]
設定檔位置
C:\Windows\Microsoft.NET\Framework\v{版本號}\Config\machine.config
C:\Windows\Microsoft.NET\Framework64\v{版本號}\Config\machine.config
修改區段 ＜compilation tempDirectory="{指向Ram disk暫存目錄}" /＞
[網站快取資料夾]
C:\Users\{使用者帳號}\AppData\Local\Microsoft\WebsiteCache
[IIS Express Log資料夾]
C:\Users\{使用者帳號}\Documents\IISExpress\Logs
C:\Users\{使用者帳號}\Documents\IISExpress\TraceLogFiles
