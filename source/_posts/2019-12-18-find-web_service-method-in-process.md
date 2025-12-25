---
layout: post
title: 找出WebService方法用在哪些流程中
date: 2019-12-18 14:46:00
tags:
- easyflow gp
- sql
---

```
DECLARE @METHOD_NAME NVARCHAR(100) = '[要尋找的WebService方法]';  
  
SELECT  
 ProcessDefinition.id,  
 RedefinableHeader.version,  
 ProcessDefinition.processDefinitionName,  
 '最新版' AS STATUS  
FROM  
 WebApplication  
 INNER JOIN IAppDefContainer_AppDef ON WebApplication.OID = ApplicationDefinitionOID  
 INNER JOIN ProcessDefinition ON ProcessDefinition.OID = IAppDefContainer_AppDef.IAppDefContainerOID  
 INNER JOIN ProcessPackage_ProcessDef ON ProcessPackage_ProcessDef.ProcessDefinitionOID = ProcessDefinition.OID  
 INNER JOIN ProcessPackage ON ProcessPackage.OID = ProcessPackage_ProcessDef.ProcessPackageOID  
 INNER JOIN RedefinableHeader ON RedefinableHeader.OID = ProcessPackage.redefinableHeaderOID  
WHERE  
 WebApplication.OID IN (  
 SELECT  
 OID  
 FROM  
 WebApplication  
 WHERE  
 CONCAT(id, CAST(objectVersion AS VARCHAR)) IN (  
 SELECT  
 CONCAT(id, CAST(MAX(objectVersion) AS VARCHAR))  
 FROM  
 WebApplication  
 WHERE  
 urlString LIKE '%' + @METHOD_NAME +'%'  
 GROUP BY  
 id  
 )  
 )  
UNION  
SELECT  
 ProcessDefinition.id,  
 RedefinableHeader.version,  
 ProcessDefinition.processDefinitionName,  
 '進行中' AS STATUS  
FROM  
 WebApplication  
 INNER JOIN IAppDefContainer_AppDef ON WebApplication.OID = IAppDefContainer_AppDef.ApplicationDefinitionOID  
 INNER JOIN ProcessDefinition ON ProcessDefinition.OID = IAppDefContainer_AppDef.IAppDefContainerOID  
 INNER JOIN ProcessInstance ON ProcessInstance.processDefinitionId = ProcessDefinition.id  
 INNER JOIN ProcessPackage_ProcessDef ON ProcessPackage_ProcessDef.ProcessDefinitionOID = ProcessDefinition.OID  
 INNER JOIN ProcessPackage ON ProcessPackage.OID = ProcessPackage_ProcessDef.ProcessPackageOID  
 INNER JOIN RedefinableHeader ON RedefinableHeader.OID = ProcessPackage.redefinableHeaderOID  
WHERE  
 urlString LIKE '%' + @METHOD_NAME +'%'  
 AND ProcessInstance.currentState IN (0, 1, 2)  
UNION  
SELECT  
 ProcessDefinition.id,  
 RedefinableHeader.version,  
 ProcessDefinition.processDefinitionName,  
 '最新版' AS STATUS  
FROM  
 WebServicesApplication  
 INNER JOIN IAppDefContainer_AppDef ON WebServicesApplication.OID = ApplicationDefinitionOID  
 INNER JOIN ProcessDefinition ON ProcessDefinition.OID = IAppDefContainer_AppDef.IAppDefContainerOID  
 INNER JOIN ProcessPackage_ProcessDef ON ProcessPackage_ProcessDef.ProcessDefinitionOID = ProcessDefinition.OID  
 INNER JOIN ProcessPackage ON ProcessPackage.OID = ProcessPackage_ProcessDef.ProcessPackageOID  
 INNER JOIN RedefinableHeader ON RedefinableHeader.OID = ProcessPackage.redefinableHeaderOID  
WHERE  
 WebServicesApplication.OID IN (  
 SELECT  
 OID  
 FROM  
 WebServicesApplication  
 WHERE  
 CONCAT(id, CAST(objectVersion AS VARCHAR)) IN (  
 SELECT  
 CONCAT(id, CAST(MAX(objectVersion) AS VARCHAR))  
 FROM  
 WebServicesApplication  
 WHERE  
 operationName = @METHOD_NAME  
 GROUP BY  
 id  
 )  
 )  
UNION  
SELECT  
 ProcessDefinition.id,  
 RedefinableHeader.version,  
 ProcessDefinition.processDefinitionName,  
 '進行中' AS STATUS  
FROM  
 WebServicesApplication  
 INNER JOIN IAppDefContainer_AppDef ON WebServicesApplication.OID = ApplicationDefinitionOID  
 INNER JOIN ProcessDefinition ON ProcessDefinition.OID = IAppDefContainer_AppDef.IAppDefContainerOID  
 INNER JOIN ProcessInstance ON ProcessInstance.processDefinitionId = ProcessDefinition.id  
 INNER JOIN ProcessPackage_ProcessDef ON ProcessPackage_ProcessDef.ProcessDefinitionOID = ProcessDefinition.OID  
 INNER JOIN ProcessPackage ON ProcessPackage.OID = ProcessPackage_ProcessDef.ProcessPackageOID  
 INNER JOIN RedefinableHeader ON RedefinableHeader.OID = ProcessPackage.redefinableHeaderOID  
WHERE  
 operationName = @METHOD_NAME  
 AND ProcessInstance.currentState IN (0, 1, 2);
```
