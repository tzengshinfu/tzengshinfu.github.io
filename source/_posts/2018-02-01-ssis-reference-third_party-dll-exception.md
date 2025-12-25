---
layout: post
title: SSIS引用第3方DLL發生異常
date: 2018-02-01 18:11:00
tags:
- ssis
---
場景:  
 1\_SSIS專案引用第3方DLL(如想用epplus解析Excel內容)  
 [![](step2.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
   
 2\_偵錯時顯示錯誤訊息而無法執行。  
 [![](step1.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
  
解法:  
 將第3方DLL加入GAC(全域組件快取)

1\_以管理員權限執行命令視窗。  
 2\_進入對應版本的.Net framework目錄下(本案例為SSIS 2014，使用.Net 4.0)  
 所以到 C:\Program Files (x86)\Microsoft SDKs\Windows\v8.0A\bin\NETFX 4.0 Tools  
 執行 gacutil.exe /i (DLL路徑)\EPPlus.dll  
 [![](step3.png)](https://www.blogger.com/# "https://www.blogger.com/#")

