---
layout: post
title: dnSpy偵錯有pdb檔的dll(ASP.NET WebForm)
date: 2019-09-05 13:29:00
tags:
- asp.net
- visual studio
- web form
---
1.Debug=>Attach to process...=>找到w3wp.exe=>Attach  
(IIS的執行緒,因為開發機的IIS沒連線會自己終止,如果沒有就開啟首頁讓IIS啟動)  

[![](att1.png)](att1.png )

  
  
  
  
  
  
  
  
  
  
  
  
2.Debug=>Windows=>Modules=>Search=>輸入要偵錯的dll名稱,路徑會是＜暫存ASP.NET目錄＞\＜網站名稱\_資料夾名稱＞\＜亂數名稱目錄...＞\dll名稱  

[![](att2.png)](att2.png )

  
  
  
  
  
  
  
  
3.雙點開啟該dll,設中斷點,再進行相關動作即會進入中斷點  

[![](att3.png)](att3.png )

  

