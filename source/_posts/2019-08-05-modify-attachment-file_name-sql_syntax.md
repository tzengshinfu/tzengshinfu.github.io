---
layout: post
title: 修改附件檔名SQL
date: 2019-08-05 09:21:00
tags:
- easyflow gp
- sql
---

```
/**修改附件檔名SQL*/   
  
/**第1步.找出表單的XML(如果是Tiptop流程,連maskFieldValues也要一併修改)*/   
 SELECT FormInstance.OID,fieldValues   
   FROM ProcessInstance   
   JOIN LocalRelevantData ON contextOID = containerOID   
   JOIN FormInstance ON valueOID = FormInstance.OID   
 WHERE ProcessInstance.serialNumber = '(要修改附件檔名的流程序號)'   
  
/**第2步.修改XML內容*/   
 UPDATE FormInstance   
 SET fieldValues = N'(修改附件檔名後的XML)'  
 ,objectVersion = objectVersion + 1   
 WHERE OID = '(第1步的FormInstance.OID)'   
  
/**第3步.修改附件檔名(修改此處並不會影響附件名稱,但為了資料完整性所以一併修改)*/   
 UPDATE NoCmDocument   
 SET logicalName = '(附件修改後檔名)'  
 ,objectVersion = objectVersion + 1   
 WHERE OID = '(第2步的附件OID)'
```
