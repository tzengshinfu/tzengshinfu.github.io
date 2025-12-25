---
layout: post
title: SSIS讀入Excel只能讀到前幾列資料的解決方法
date: 2017-04-17 09:46:00
tags:
- ssis
---
狀況:  
User將數個表格放在同一個工作表中，  
用SSIS讀入發現前8列有值，但之後的列內容都是null。  
  
解法:  
1.Excel檔的連線字串需增加IMEX=1→指定唯讀模式。  
2.讀Excel的主機(開發區&正式區)的登錄檔需修改TypeGuessRows:8→0，  
意指不以前8列推斷以下所有列的欄位型態  
(因為當時前8列是屬於第1個表格，內容是數字，  
但之後的列是屬於第2個表格，內容是文字，欄位型態不同導致讀取失敗)，  
而是強制Excel讀取每列內容判斷欄位型態。  

[![](type.png)](type.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
參考:[透過 OleDb 精準讀入](http://blog.miniasp.com/post/2008/08/05/How-to-read-Excel-file-using-OleDb-correctly.aspx "http://blog.miniasp.com/post/2008/08/05/How-to-read-Excel-file-using-OleDb-correctly.aspx")[Excel 檔的方法](http://blog.miniasp.com/post/2008/08/05/How-to-read-Excel-file-using-OleDb-correctly.aspx "http://blog.miniasp.com/post/2008/08/05/How-to-read-Excel-file-using-OleDb-correctly.aspx")

