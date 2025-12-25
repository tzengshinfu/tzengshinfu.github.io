---
layout: post
title: 繼承的表單在設計工具檢視模式顯示錯誤訊息
date: 2018-05-07 23:24:00
tags:
- visual studio
- windows form
---
父表單如下  
[![](Image_20180504161919.png)](Image_20180504161919.png )  
  
  
  
  
  
  
  
  
  
  
  
子表單使用父表單的物件  

[![](Image_20180504161844.png)](Image_20180504161844.png )

  
  
  
  
  
  
  
  
  
在設計工具檢視模式下會顯示錯誤訊息如下  
(1)*並未將物件參考設定為物件的執行個體。*  

[![](Image_20180504153342.png)](Image_20180504153342.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
或(2)類似如 *服務 System.Windows.Forms.Design.IEventHandlerService 已經存在於服務容器中。參數名稱: serviceType*  

[![](Image_20180504135851.png)](Image_20180504135851.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
加上是否為DesignMode判斷式，編譯並重新打開設計工具檢視模式即可  

[![](Image_20180504152049.png)](Image_20180504152049.png )

  

