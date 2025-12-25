---
layout: post
title: '[啟動/偵錯異常]The Ribbon/COM Add-in helper required by add-in "增益集名稱" Add-In could
date: 2017-10-18 18:49:00
not be registered.'
tags:
- excel-dna
---
狀況:  
偵錯時發現Excel顯示錯誤訊息  
"The Ribbon/COM Add-in helper required by add-in "增益集名稱" Add-In could not be registered."  
而無法載入增益集(如下圖)  

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
解法:  
當開發過程中如果發生例外狀況的次數較多時,  
Excel有時會自動停用我們撰寫的增益集,  
此時只要手動啟用即可  
(工具列>選項>增益集>管理(A):>選[停用的項目]>執行(G)...>把"增益集名稱"啟用)  

[![](step2.png)](step2.png )

  

