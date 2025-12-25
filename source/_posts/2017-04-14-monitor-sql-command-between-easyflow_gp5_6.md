---
layout: post
title: 監看EasyFlow與DB間的SQL指令
date: 2017-04-14 11:37:00
tags:
- easyflow gp
- sql
- ssms
---

開啟[SQL Server Profiler]>>[新增追蹤]

1.事件選取範圍  
→選取事件RPC:Completed及SQL:BatchCompleted  

[![](at1.png)](at1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
2.資料行篩選  
在DatabaseName新增資料庫名稱  

[![](at2.png)](at2.png )

在TextData新增  
declare @p1 int%  
select%  
update%  
delete%  
insert%  

[![](at3.png)](at3.png )

  

  
  
  
  
  
  
  
3.即可在結果尋找相關的SQL指令

[![](Image_20170414112019+%283%29.png)](Image_20170414112019+%283%29.png )

