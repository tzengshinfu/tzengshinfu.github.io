---
layout: post
title: 檢查某目錄下檔案數量決定進行後續作業
date: 2018-05-02 18:14:00
tags:
- dos command
---

```
 @ECHO OFF  
 ::初始化變數[檔案數量]  
 SET FileCount=0  
 ::遍歷檔案,累加到[檔案數量]  
 FOR %A IN (D:\WorkDirectory\*) DO SET /A FileCount+=1  
 ::如果[檔案數量]大於等於100則進行後續作業  
 IF %FileCount% GEQ 100 (ECHO "file count greater or equal to 100!")
```
