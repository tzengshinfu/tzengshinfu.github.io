---
layout: post
title: 批次更新表單欄位SQL
date: 2019-08-27 14:24:00
tags:
- easyflow gp
- sql
---

```
DECLARE @oldValue NVARCHAR(255) = '{舊參與者工號}'; --欄位舊值
DECLARE @newValue NVARCHAR(255) = '{新參與者工號}'; --欄位新值
DECLARE @processDefId NVARCHAR(255) = 'PKGPROCESS_xxxxxx'; --流程定義代號
UPDATE FormInstance

SET fieldValues = REPLACE(CAST(fieldValues AS NVARCHAR(MAX)), @oldValue, @newValue)
--,maskFieldValues = REPLACE(CAST(maskFieldValues AS NVARCHAR(MAX)), @oldValue, @newValue) --如果是Tiptop流程的話
,objectVersion = objectVersion + 1
WHERE OID IN ( 
SELECT FormInstance.OID
FROM ProcessInstance
INNER JOIN LocalRelevantData ON LocalRelevantData.containerOID = ProcessInstance.contextOID
INNER JOIN FormInstance ON FormInstance.OID = LocalRelevantData.valueOID
WHERE ProcessInstance.processDefinitionId = @processDefId
AND ProcessInstance.currentState IN (1,2) --進行中
AND FormInstance.fieldValues LIKE '%' + @oldValue + '%'
);
```
