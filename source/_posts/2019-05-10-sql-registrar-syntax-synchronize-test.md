---
layout: post
title: SQL註冊器 SQL語法 測試區同步至正式區
date: 2019-05-10 08:30:00
tags:
- easyflow gp
- sql
---

```
/*SQL註冊器 SQL語法 測試區同步至正式區*/   
 INSERT INTO [正式區EFGP DB].dbo.FormSqlClause   
     SELECT   
         *   
     FROM [測試區EFGP DB].dbo.FormSqlClause   
     WHERE id IN ('[SQL代號]');   
   
 /*SQL註冊器 表單權限 測試區同步至正式區*/   
 INSERT INTO [正式區EFGP DB].dbo.SqlAllowedForm   
     SELECT   
         *   
     FROM [測試區EFGP DB].dbo.SqlAllowedForm   
     WHERE containerOID IN (   
         SELECT   
             OID   
         FROM [測試區EFGP DB].dbo.FormSqlClause   
         WHERE id IN ('[SQL代號]')   
     );
```
