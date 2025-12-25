---
layout: post
title: Oracle Developer Tools for Visual Studio 2019安裝注意事項
date: 2021-06-16 09:59:00
tags:
- visual studio
---

1.最新版(19.3.2版)改成Visual Studio擴充功能(VSIX)形式，安裝更方便。

2.本機不需安裝Oracle Data Access Components(ODAC)。

3.Visual Studio 2019需升級至16.4.2版以上。

4.專案Oracle.ManagedDataAccess及Oracle.ManagedDataAccess.EntityFramework套件  
需升級至19.3.0版以上。

5.Visual Studio 2019→工具→選項→Oracle Developer Tools→連線組態→TNS管理位置 及 公事包檔案位置 需指向已存在tnsnames.ora的實體路徑，修改後並重啟Visual Studio。
