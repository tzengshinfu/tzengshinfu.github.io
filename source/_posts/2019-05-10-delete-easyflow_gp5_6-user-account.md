---
layout: post
title: 刪除使用者帳號
date: 2019-05-10 08:38:00
tags:
- easyflow gp
- sql
---

```
 DECLARE @userId nvarchar(100) = '[工號]'   
 DECLARE @userOID char(32) = (SELECT OID FROM Users WHERE id = @userId)   
   
 DELETE FROM Users where id = @userId;   
 DELETE FROM Employee WHERE employeeId = @userId;   
 DELETE FROM Functions where occupantOID = @userOID;
```
