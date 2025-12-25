---
layout: post
title: VS Code對Blazor應用程式偵錯時顯示[遠端憑證無效]的異常
date: 2021-07-28 08:55:00
tags:
- visual studio code
---

 狀況：

[![](image_20210728082150-1.png)](image_20210728082150-1.png )

  

解法：

在終端視窗輸入

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

會顯示憑證安裝視窗

[![](Image_20210728082117.png)](Image_20210728082117.png )

按是(Y)安裝後即可正常偵錯。

