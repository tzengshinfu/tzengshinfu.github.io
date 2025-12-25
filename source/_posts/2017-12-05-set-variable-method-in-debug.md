---
layout: post
title: 只在debug組態下設定變數及執行方法
date: 2017-12-05 11:58:00
tags:
- visual studio
---
在程式片段前後加上**#if DEBUG**及**#endif**  

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
當切換release組態則不會執行該程式片段;  
另外視情況可加上**#else**作為當處於非debug模式(release或自訂組態)的動作。

