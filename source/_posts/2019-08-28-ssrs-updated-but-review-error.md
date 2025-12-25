---
layout: post
title: ReportingService已更新SQL但報表預覽異常
date: 2019-08-28 14:36:00
tags:
- ssrs
---
情況:  
SQL已修改但未反應在預覽的欄位,  
而且有錯誤訊息(如下圖)  
[![](Image_20190828141703.png)](Image_20190828141703.png )  
  
解決方法:  
刪除<報表名稱>.rdl.data檔即可。  
  
參考:  
[SQL Server Reporting Studio report showing “ERROR#” or invalid data type error](https://stackoverflow.com/a/21430840 "https://stackoverflow.com/a/21430840")  

[![](Image_20190828143405.png)](Image_20190828143405.png )

  

