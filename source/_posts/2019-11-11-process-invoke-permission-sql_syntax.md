---
layout: post
title: 流程發起權限設定值SQL
date: 2019-11-11 09:25:00
tags:
- easyflow gp
- sql
---

```
SELECT
    ProcessDefinition.processDefinitionName,
    PackageInvokeAuthority.userList,
    PackageInvokeAuthority.organizationUnitList,
    PackageInvokeAuthority.groupList,
    PackageInvokeAuthority.functionDefList
FROM
    ProcessPackage
    INNER JOIN ProcessPackageCmItem ON ProcessPackage.containerOID = ProcessPackageCmItem.OID
    INNER JOIN RedefinableHeader ON ProcessPackage.redefinableHeaderOID = RedefinableHeader.OID
    INNER JOIN ProcessPackageHeader ON ProcessPackage.headerOID = ProcessPackageHeader.OID
    INNER JOIN ProcessPackage_ProcessDef ON ProcessPackage.OID = ProcessPackage_ProcessDef.ProcessPackageOID
    INNER JOIN ProcessDefinition ON ProcessPackage.id = ProcessDefinition.id
    INNER JOIN ProcessDefinitionHeader ON ProcessDefinition.headerOID = ProcessDefinitionHeader.OID
    LEFT JOIN PackageInvokeAuthority ON ProcessPackage.packageInvokeAuthorityOID = PackageInvokeAuthority.OID
WHERE
    ProcessDefinition.OID = ProcessPackage_ProcessDef.ProcessDefinitionOID
    AND ProcessPackageCmItem.lastVersion = RedefinableHeader.version
    AND validTo >= GETDATE()
    AND RedefinableHeader.publicationStatus = 'RELEASED'
    AND processDefinitionName = '＜流程名稱＞'
```
