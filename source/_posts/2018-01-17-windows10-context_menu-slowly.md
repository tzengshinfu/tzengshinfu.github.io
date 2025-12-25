---
layout: post
title: Windows 10 桌面右鍵選單出現"很慢"
date: 2018-01-17 23:32:00
tags:
- windows
---
一般狀況應該會在1秒內顯示右鍵選單, 延遲原因是因為被Intel顯卡右鍵選單拖慢。  

[![](Capture_20180117232554.png)](Capture_20180117232554.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
對策:  
在登錄檔,右鍵選單,Intel顯卡控制台移除即可。  
將此機碼  
HKEY\_CLASSES\_ROOT\Directory\Background\shellex\ContextMenuHandlers\**igfxDTCM**  
刪除。  
  
參考來源:[(分享)解決windows 10桌面右鍵選單反應很慢的方法](https://www.dcard.tw/f/3c/p/157357544 "https://www.dcard.tw/f/3c/p/157357544")

