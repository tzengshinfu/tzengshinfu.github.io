---
layout: post
title: 本機LocalDB降版
date: 2019-01-08 13:39:00
tags:
- localdb
- visual studio
---
場景:  
本機已安裝LocalDB 2016,想降版到2014。  
  
作法:  
1.移除LocalDB 2016。  
2.安裝LocalDB 2014。  
3.如果在新增/連線到LocalDB顯示異常如下圖:  

[![](Image_20190108115342.png)](Image_20190108115342.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
4.進到事件檢視簿,如果發現錯誤訊息如下圖:  

[![](111.png)](111.png )

  
  
  
  
  
  
  
  
  
  
5.編輯登錄檔如下圖:  
路徑:HKEY\_CURRENT\_USER\Software\Microsoft\Microsoft SQL Server\UserInstances  
刪除錯誤版本即可。  

[![](Image_20190108132124.png)](Image_20190108132124.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
參考來源:[LocalDB parent instance version invalid: MSSQL13E.LOCALDB](https://stackoverflow.com/a/43693155 "https://stackoverflow.com/a/43693155")

