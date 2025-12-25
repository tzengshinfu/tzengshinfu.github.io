---
layout: post
title: 取得遠端DB所連接伺服器的檢視有錯誤訊息
date: 2017-04-21 14:29:00
tags:
- ssis
---
狀況：要取得遠端DB=OA的特定資料表，但該資料表其實是以[連結的伺服器]=HRM所建立的View(如下圖)  
  

[![](%E7%B9%AA%E5%9C%962.png)](%E7%B9%AA%E5%9C%962.png )

  
SSIS程式會有以下問題：  
1.OLE DB來源無法預覽，會顯示"找不到資料行"的錯誤訊息。  

[![](1.png)](1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
2."指定一個以上的字碼頁"的錯誤訊息。  

[![](2.png)](2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
解法：把[OLE DB 來源]改成[ADO NET 來源]元件即可。  
  
  
  
參考：[How to add a linked server to the SSIS Data Flow destination?](https://social.msdn.microsoft.com/Forums/sqlserver/en-US/554a360d-0265-4ff6-ab9b-d63fbaae5351/how-to-add-a-linked-server-to-the-ssis-data-flow-destination?forum=sqlintegrationservices "https://social.msdn.microsoft.com/Forums/sqlserver/en-US/554a360d-0265-4ff6-ab9b-d63fbaae5351/how-to-add-a-linked-server-to-the-ssis-data-flow-destination?forum=sqlintegrationservices")

