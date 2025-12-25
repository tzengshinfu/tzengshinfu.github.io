---
layout: post
title: 同一筆SQL指令進行新增/修改/刪除(MERGE)
date: 2017-04-07 16:19:00
tags:
- sql
---
MERGE enginner AS Target  
USING(<比對的條件語法>) AS Source  
ON (Target.name = Source.name AND Target.dept = Source.dept)→目的和來源比較條件  
WHEN MATCHED THEN→當目的符合來源就更新  
UPDATE SET Target.position = Source.position  
WHEN NOT MATCHED BY TARGET THEN→當目的無此紀錄就新增  
INSERT (name, position) VALUES (Source.name, Source.position, Source.dept)  
WHEN NOT MATCHED BY SOURCE THEN→當來源無此紀錄就刪除  
DELETE;  
  
<比對的條件語法>  
可以指定Table  
SELECT name, position from employee  
或指定固定值  
SELECT ‘frank\_tseng’ AS name, ‘engineer’ AS position  
或指定參數(程式使用)  
SELECT ? AS name, ? AS position  
  
\*需MS SQL Server 2008以上;另外MERGE是ANSI SQL:2003的標準,  
  每家資料庫廠商都有實作,所以不用擔心移殖的問題。  
  
\*僅針對單一紀錄合併新增/更新/刪除動作。
