---
layout: post
title: Android Studio顯示錯誤訊息"Cannot resolve XXX"
date: 2017-11-30 11:15:00
tags:
- android studio
---
狀況:  
變數名稱顯示紅色,有錯誤訊息"Cannot resolve XXX"  

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
解法:  
1\_在功能列>Build>Rebuild Project  

[![](step2.png)](step2.png )

  
  
2\_當解法1無效時,可更動(如輸入空白再刪除等)build.gradle(Project)內容,以觸發Sync功能  

[![](step3.png)](step3.png )

  
  
  
  
  
  
  
  
  
  
3\_亦可嘗試清除快取  

[![](step1.png)](step1.png )

  

