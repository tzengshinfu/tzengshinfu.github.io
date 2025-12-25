---
layout: post
title: 取得線上全部流程序號名稱
date: 2019-07-17 11:00:00
tags:
- easyflow gp
- sql
---

```
SELECT   
     ProcessDefinition.id,   
     ProcessDefinition.processDefinitionName   
 FROM   
     ProcessPackage   
     INNER JOIN ProcessPackageCmItem ON ProcessPackage.containerOID = ProcessPackageCmItem.OID   
     INNER JOIN RedefinableHeader ON ProcessPackage.redefinableHeaderOID = RedefinableHeader.OID   
     INNER JOIN ProcessPackageHeader ON ProcessPackage.headerOID = ProcessPackageHeader.OID   
     INNER JOIN ProcessPackage_ProcessDef ON ProcessPackage.OID = ProcessPackage_ProcessDef.ProcessPackageOID   
     INNER JOIN ProcessDefinition ON ProcessPackage.id = ProcessDefinition.id   
     INNER JOIN ProcessDefinitionHeader ON ProcessDefinition.headerOID = ProcessDefinitionHeader.OID   
 WHERE   
     ProcessDefinition.OID = ProcessPackage_ProcessDef.ProcessDefinitionOID   
     AND ProcessPackageCmItem.lastVersion = RedefinableHeader.version   
     AND validTo >= GETDATE()   
     AND RedefinableHeader.publicationStatus = 'RELEASED'
```
