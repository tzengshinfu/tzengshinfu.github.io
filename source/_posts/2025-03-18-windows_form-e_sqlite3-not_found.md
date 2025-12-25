---
layout: post
title: Windows Forms建立SQLite連線時顯示Library e\_sqlite3找不到的錯誤
date: 2025-03-18 10:16:00
tags:
- ".net framework"
- sqlite
- visual studio 2022
- windows form
---

版本：

VS2022 v17.13.3

SQLite-net v1.9.172

1. 使用新增Windows Forms App (.NET Framework)專案。

2. 安裝Nuget套件SQLite-net NuGet\Install-Package sqlite-net-pcl -Version [最新版]

3. 建立SQLite連線時顯示錯誤訊息：Library e\_sqlite3找不到

[![](Capture_20250318_092722.png)](Capture_20250318_092722.png )

  

解法：

1. 降版SQLitePCLRaw.lib.e\_sqlite3至v2.0.7

參考來源：[【茶包射手日記】.NET Framework 專案 SQLite 執行錯誤：找不到 e\_sqlite3](https://blog.darkthread.net/blog/sqlite-n-netfx/#9ab43c6e-601b-46f2-b6bf-f89caf1e6f79 "https://blog.darkthread.net/blog/sqlite-n-netfx/#9ab43c6e-601b-46f2-b6bf-f89caf1e6f79")

2. 遷移package.config到PackageReference

[![](Capture_20250318_092433.png)](Capture_20250318_092433.png )

  

[![](devenv_20250318_092440.png)](devenv_20250318_092440.png )

  

因為VS2022建立的Windows Forms App (.NET Framework)專案，

預設使用package.config管理Nuget套件，

但SQLite-net相依的SQLitePCLRaw NuGet套件在v2.1.0後需要使用PackageReference管理。

參考來源：[Exception after updating from 2.0.8 to 2.1.0](https://github.com/ericsink/SQLitePCL.raw/issues/483 "https://github.com/ericsink/SQLitePCL.raw/issues/483")

參考來源：[從 package.config 移轉到 PackageReference](https://learn.microsoft.com/zh-tw/nuget/consume-packages/migrate-packages-config-to-package-reference "https://learn.microsoft.com/zh-tw/nuget/consume-packages/migrate-packages-config-to-package-reference")

  

