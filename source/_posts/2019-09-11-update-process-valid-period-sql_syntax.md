---
layout: post
title: 更新流程有效期間
date: 2019-09-11 11:18:00
tags:
- easyflow gp
- sql
---

```
UPDATE ProcessDefinitionHeader  
SET validTo = '9999-12-31 23:59:59.000'  
,objectVersion = objectVersion + 1  
WHERE OID IN (  
    SELECT  
        ProcessDefinitionHeader.OID  
    FROM ProcessDefinition  
    INNER JOIN ProcessDefinitionHeader  
        ON ProcessDefinition.headerOID = ProcessDefinitionHeader.OID  
    INNER JOIN ProcessPackage_ProcessDef  
        ON ProcessDefinition.OID = ProcessPackage_ProcessDef.ProcessDefinitionOID  
    INNER JOIN ProcessPackage  
        ON ProcessPackage_ProcessDef.ProcessPackageOID = ProcessPackage.OID  
    INNER JOIN RedefinableHeader  
        ON ProcessPackage.redefinableHeaderOID = RedefinableHeader.OID  
    INNER JOIN ProcessPackageCmItem  
        ON ProcessPackage.id = ProcessPackageCmItem.id  
        AND RedefinableHeader.version = ProcessPackageCmItem.lastVersion  
    WHERE 1 = 1  
    AND validTo >= GETDATE() /**不更新舊流程*/  
    AND RedefinableHeader.publicationStatus = 'RELEASED' /**只更新RELEASE的*/  
);
```

建議也可將表單截止有效日欄位設為NULL以避免突然找不到表單的問題。

```
UPDATE FormDefinition SET validTo = NULL WHERE validTo IS NOT NULL
```
