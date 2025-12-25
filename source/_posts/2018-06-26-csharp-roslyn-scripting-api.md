---
layout: post
title: C# Roslyn Scripting API(程式靈活性上升, 但穩健性卻會大幅下降, 需配合大量[單元測試]服用!)
date: 2018-06-26 17:49:00
tags:
- c#
- roslyn scripting api
---
以呼叫轉換月份縮碼的方法為例:  
  
該dll內容如下圖:  
[![](Image_20180626173803.png)](Image_20180626173803.png )  
  
1.專案需加入該dll作為參考。  

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
2.重點是  
Type.GetType(<該類別的AssemblyQualifiedName>).Assembly  

[![](step3.png)](step3.png )

  
  
  
  
  
  
  
  
  
3.執行結果如下圖:  

[![](Image_20180626174236.png)](Image_20180626174236.png )

  

