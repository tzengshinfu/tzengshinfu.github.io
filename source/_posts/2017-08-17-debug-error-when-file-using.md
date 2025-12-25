---
layout: post
title: 偵錯時出現[由於另一個處理序正在使用檔案，所以無法執行該檔案]的訊息而無法偵錯
date: 2017-08-17 09:26:00
tags:
- ssis
---
狀況：

當按下[F5]開始偵錯時顯示錯誤訊息如下  
![](step1.png)  
  
  
解法:

工作管理員刪除殘留的處理序DtsDebugHost.exe即可![](step2.png)

