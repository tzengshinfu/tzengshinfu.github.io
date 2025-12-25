---
layout: post
title: 在SSRS使用DECLARE陳述式的SQL無法預覽錯誤
date: 2019-12-25 15:32:00
tags:
- ssrs
---
原因:  
在SSRS的查詢SQL中,  
如果有自行宣告的變數跟查詢參數同時存在,  
如

```
DECLARE @processDefinitionId NVARCHAR(100) = @processDefId;
DECLARE @formSerialNumber NVARCHAR(50) = @formSN;
```

因為兩者都是@開頭,  
在解析時會把查詢參數當成自行宣告的變數,  
才會顯示以下異常  

[![](Image_20191225152343.png)](Image_20191225152343.png )

  
  

[![](Image_20191225152633.png)](Image_20191225152633.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
解法:  
按[當成文字編輯]即可正確解析預覽結果。  

[![](Image_20191226150225.png)](Image_20191226150225.png )

