---
layout: post
title: 用Visual Studio Code對Python程式偵錯顯示錯誤訊息的解法
date: 2017-10-10 16:42:00
tags:
- python
- visual studio code
---
狀況:  
1\_已安裝Visual Studio 2017 Python開發環境(Python 3.6.2)  
2\_在Visual Studio Code對Python程式偵錯顯示錯誤訊息(如下圖)  

[![](Image_20171009232420.png)](Image_20171009232420.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
解法:  
1\_在系統>進階系統設定>進階>環境變數>系統變數  
選擇[Path]>按[編輯]  

[![](Image_20171010162540.png)](Image_20171010162540.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
2\_新增Visual Studio 2017所安裝的Python 3的路徑(本例為C:\Program Files\Python36)  

[![](Image_20171010162525.png)](Image_20171010162525.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
3\_重啟Visual Studio Code即可正常偵錯

