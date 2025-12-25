---
layout: post
title: 欄位別名在同一筆SQL指令立即使用
date: 2017-04-07 16:23:00
tags:
- sql
---
使用通用資料表運算式(CTE)  
  

```
WITH RESULT AS (  
 SELECT  
     5 - 1 AS COLUMN1  
     ,4 - 1 AS COLUMN2  
 )  
 SELECT COLUMN1, COLUMN2 FROM RESULT;
```

  
  
參考:[Tip: APPLY and Reuse of Column Aliases](http://sqlmag.com/blog/tip-apply-and-reuse-column-aliases "http://sqlmag.com/blog/tip-apply-and-reuse-column-aliases")
