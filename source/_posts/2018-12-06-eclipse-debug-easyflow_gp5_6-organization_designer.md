---
layout: post
title: Eclipse偵錯鼎新EasyFlow組織設計師
date: 2018-12-06 15:19:00
tags:
- debugger
- easyflow gp
---
1.用文字編輯器開啟jnlp檔, 到server將＜resources＞ tag內所有用到的jar檔下載到本地端。   
 [![](Image_20181206144148.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
  
   
 2.下載Java Decompiler Eclipse[套件](https://www.blogger.com/# "https://www.blogger.com/#")。   
   
   
 3.開啟Eclipse, 安裝之, 開啟class檔可顯示原始碼。   
 [![](Image_20181206140252.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
  
 新增套件順序如下。   
 [![](Image_20181206140300.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
  
   
 [![](Image_20181206140324.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 [![](Image_20181206140332.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
  
   
 4.新增專案。   
 [![](Image_20181206140441.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 5.新增引用, 加入之前下載的jar檔。   
 [![](Image_20181206140455.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
  
   
 [![](Image_20181206140814.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 6.偵錯組態新增遠端偵錯。   
 [![](Image_20181206143921.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 7.開啟source code, 找到要偵錯的段落, 加上中斷點。   
 [![](Image_20181206142740.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 8.以命令列執行jnlp檔, 程式不會顯示, 因為要等Eclipse連接上。   
 javaws.exe -J-agentlib:jdwp=transport=dt\_socket,server=y,suspend=y,address=5005 nana-organization-designer.jnlp   
   
   
 9.Eclipse執行偵錯, 組織設計師顯示畫面, 且執行到中斷點則會暫停。   
 [![](Image_20181206144031.png)](https://www.blogger.com/# "https://www.blogger.com/#")   

