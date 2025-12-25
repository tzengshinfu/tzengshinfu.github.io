---
layout: post
title: 修正線上正在執行的流程關卡的SQL語法
date: 2019-02-01 09:49:00
tags:
- easyflow gp
- sql
---

```
 DECLARE @serialNumber nvarchar(50) = '<要修正的流程序號>';   
 DECLARE @activityDefinitionName nvarchar(100) = '<要修正的關卡ID>';   
 DECLARE @contextOID char(32) = (SELECT contextOID FROM ProcessInstance WHERE serialNumber = @serialNumber);   
 DECLARE @processPackageOID char(32) = (SELECT processPackageOID FROM ProcessContext WHERE OID = @contextOID);   
 DECLARE @ProcessDefinitionOID char(32) = (SELECT ProcessDefinitionOID FROM ProcessPackage_ProcessDef WHERE ProcessPackageOID = @processPackageOID);   
  
 SELECT   
     ParticipantDefinition.*   
 FROM ActivityDefinition   
 INNER JOIN ParticipantDefinition   
 ON ActivityDefinition.containerOID = ParticipantDefinition.containerOID   
 AND ParticipantDefinition.id LIKE '%' + CAST(ActivityDefinition.performerIds AS VARCHAR(MAX)) + '%'   
 AND ActivityDefinition.containerOID = @ProcessDefinitionOID   
 AND activityDefinitionName = @activityDefinitionName;   
  
 UPDATE ParticipantDefinition   
 SET organizationUnitId = '<修正後的部門代號>'   
 ,objectVersion = objectVersion + 1   
 WHERE OID = '<為上個SQL指令查出的ParticipantDefinition.OID>';
```
