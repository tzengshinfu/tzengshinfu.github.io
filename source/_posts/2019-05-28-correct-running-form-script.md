---
layout: post
title: 修正線上進行中的舊表單Js程式
date: 2019-05-28 10:22:00
tags:
- easyflow gp
- sql
---
  

1.      用[程式片段]定位線上進行中所有的表單版號

```
 DECLARE @CODE NVARCHAR(4000) = '[要尋找的程式片段]';   
  
 SELECT   
     DISTINCT FormDefinition.id,   
     FormDefinition.version,   
     FormDefinition.formDefinitionName,   
     CAST(FormDefinition.script AS NVARCHAR(MAX)) AS script,   
     '進行中' AS status   
 FROM   
     ProcessInstance   
     INNER JOIN LocalRelevantData ON LocalRelevantData.containerOID = ProcessInstance.contextOID   
     INNER JOIN FormInstance ON FormInstance.OID = LocalRelevantData.valueOID   
     INNER JOIN FormDefinition ON FormDefinition.OID = FormInstance.definitionOID   
 WHERE   
     ProcessInstance.currentState IN (0, 1, 2)   
     AND FormDefinition.script LIKE '%' + @CODE + '%'   
 UNION   
 SELECT   
     id,   
     version,   
     formDefinitionName,   
     CAST(FormDefinition.script AS NVARCHAR(MAX)) AS script,   
     '最新版' AS status   
 FROM   
     FormDefinition   
 WHERE   
     publicationStatus = 'RELEASED'   
     AND FormDefinition.script LIKE '%' + @CODE + '%';
```

[![](ATT.png)](ATT.png )

2.     
在表單設計師→右鍵[檢視表單發行歷程]→找到對應版號→右鍵[取出此版本]→修正Js程式→按[更新腳本]即可。  
  
[![](2.png)](https://www.blogger.com/# "https://www.blogger.com/#")

  

