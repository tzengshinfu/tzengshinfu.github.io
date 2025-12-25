---
layout: post
title: 列欄轉置語法(PIVOT)
date: 2017-12-26 13:33:00
tags:
- sql
---

```
 SELECT "欄位1"  
       ,"欄位2"  
       ,"欄位3"  
       ,"A","B","C","D" /**轉置後的欄位*/  
 FROM  
 (  
     SELECT "欄位1"  
           ,"欄位2"  
           ,"欄位3"  
           ,"條件欄位"  
           ,"要統計的欄位"  
     FROM "表格名稱"  
 ) AS "SOURCE"  
 PIVOT  
 (  
     SUM("要統計的欄位") /**彙總函式*/  
     FOR "條件欄位" IN ("A","B","C","D") /**轉置後的欄位,即條件欄位的值*/  
 ) AS "PIVOT_COLUMN"
```

  
   
