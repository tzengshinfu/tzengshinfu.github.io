---
layout: post
title: 'Error: 無法套用 ForEach Variable Mapping 數字 1 至變數 "User::xxxx"'
date: 2017-04-12 20:52:00
tags:
- ssis
---
狀況：此錯誤偶爾會發生，導致擷轉程式異常。  

[![](step1.png)](step1.png )

此元件所承接的結果是前1個元件(Execute SQL Task)所傳回的Result Set。

[![](result2.png)](result2.png )

解法：

因為所傳回的Result Set含有NULL值，使用SQL指令過濾即可。

[![](result.png)](result.png )

  
  

