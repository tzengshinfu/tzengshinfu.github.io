---
layout: post
title: MSSQL查詢AD群組使用者清單
date: 2019-08-27 11:51:00
tags:
- sql server
---

```
DECLARE @statment nvarchar(max) 
= N'select ROW_NUMBER() OVER (ORDER BY AD.SAMAccountName) AS RowNumber, AD.SAMAccountName,AD.mail, AD.name, AD.distinguishedName from openquery(ADSI,''select SAMAccountName, Name, mail, distinguishedName from ''''LDAP://OU=<公司名稱>,DC=<公司名稱>,DC=com'''' WHERE memberof=''''CN='
 + @GroupName + ',OU=群組帳號,OU=USUN,DC=<公司名稱>,DC=com'''''') AS AD ORDER BY AD.SAMAccountName'; 
EXEC sp_executesql @statment;
```
