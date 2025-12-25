---
layout: post
title: 更新主部門,職務,核決層級,職稱
date: 2019-05-10 08:47:00
tags:
- easyflow gp
- sql
---

```
 DECLARE @userId nvarchar(100)   
 DECLARE @newOrganizationUnitId nvarchar(100)   
 DECLARE @newFunctionDefinitionName nvarchar(100)   
 DECLARE @newFunctionLevelName nvarchar(100)   
 DECLARE @occupantOID char(32)   
 DECLARE @newOrganizationOID char(32)   
 DECLARE @newOrganizationUnitOID char(32)   
 DECLARE @newFunctionsDefinitionOID char(32)   
 DECLARE @newApprovalLevelOID char(32)   
 DECLARE @newTitleDefinitionOID char(32)   
   
 SET @userId = '[工號]'   
 SET @newOrganizationUnitId = '[部門代號]'   
 SET @newFunctionDefinitionName = '[職務名稱]'   
 SET @newFunctionLevelName = '[核決權限名稱]'   
 SET @occupantOID = (SELECT OID FROM Users WHERE id = @userId)   
 SET @newOrganizationOID = (select organizationOID FROM OrganizationUnit WHERE id = @newOrganizationUnitId)   
 SET @newOrganizationUnitOID = (SELECT OID FROM OrganizationUnit WHERE id = @newOrganizationUnitId)   
 SET @newFunctionsDefinitionOID = (SELECT OID FROM FunctionDefinition WHERE organizationOID = @newOrganizationOID AND functionDefinitionName = @newFunctionDefinitionName)   
 SET @newApprovalLevelOID = (SELECT OID FROM FunctionLevel WHERE organizationOID = @newOrganizationOID AND functionLevelName = @newFunctionLevelName)   
 SET @newTitleDefinitionOID = (SELECT OID FROM TitleDefinition WHERE organizationOID = @newOrganizationOID AND titleDefinitionName = @newFunctionDefinitionName)   
   
 /*更新主部門*/   
 UPDATE Functions   
 SET organizationUnitOID = @newOrganizationUnitOID  
 ,objectVersion = objectVersion + 1   
 WHERE isMain = 1 AND occupantOID = @occupantOID   
   
 /*更新職務*/   
 UPDATE Functions   
 SET definitionOID = @newFunctionsDefinitionOID  
 ,objectVersion = objectVersion + 1   
 WHERE isMain = 1 AND occupantOID = @occupantOID   
   
 /*更新核決層級*/   
 UPDATE Functions   
 SET approvalLevelOID = @newApprovalLevelOID  
 ,objectVersion = objectVersion + 1   
 WHERE isMain = 1 AND occupantOID = @occupantOID   
   
 /*更新職稱*/   
 UPDATE Title   
 SET definitionOID = @newTitleDefinitionOID  
 ,objectVersion = objectVersion + 1   
 WHERE organizationUnitOID = @newOrganizationUnitOID AND occupantOID = @occupantOID
```
