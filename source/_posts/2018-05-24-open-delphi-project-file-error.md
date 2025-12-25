---
layout: post
title: 點擊Delphi專案檔時會顯示[傳送命令給程式時發生錯誤]而無法直接開啟
date: 2018-05-24 17:52:00
tags:
- delphi
---
【狀況】  
 雙點dpr檔圖示(Delphi專案檔), 在開啟Delphi 時IDE卻顯示錯誤訊息,  
 而直接開啟一個空的作業環境。  
 [![](Image_20180524173330.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
 【解法】  
 開啟{登錄編輯程式}。  
 搜尋{DelphiProject}，展開並刪除{ddeexec}這個機碼。  
 [![](Image_20180524173733.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 將同階的{command}機碼的內容由  
 C:\Delphi6\Bin\Delphi32.exe /np  
 改為  
 C:\Delphi6\Bin\Delphi32.exe "%1"  
 即可。  
 [![](Image_20180524173753.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
   
   
   
   
   
   
   

