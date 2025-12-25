---
layout: post
title: 修正進行中的表單欄位權限
date: 2019-01-07 09:41:00
tags:
- easyflow gp
---
場景:  
   
流程的某一關(本例為ACT2)的控件(本例為附件按鈕Attachment)忘了設成Enable,導致在這關都無法上傳附件。   
 [![](Image_20190107083620.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 動作:   
 (1)找出目前在使用的流程定義。  
SQL語法:  

```
SELECT *   
FROM ProcessDefinition   
INNER JOIN ProcessDefinitionHeader   
ON ProcessDefinition.headerOID = ProcessDefinitionHeader.OID   
AND ProcessDefinitionHeader.validTo >= GETDATE()   
INNER JOIN RedefinableHeader   
ON ProcessDefinition.redefinableHeaderOID = RedefinableHeader.OID   
AND RedefinableHeader.publicationStatus = 'RELEASED'   
WHERE id = 'test00011';
```

  
 [![](Image_20190107091413.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
  
(2)以(1)的OID查詢這個流程定義底下所用的所有活動關卡定義。   
 SQL語法:

```
SELECT id, formFieldAccessDefinitionOID   
 FROM ActivityDefinition   
 WHERE containerOID = '4beabe6fe40510048797ab8fbcef89eb';
```

  
 [![](Image_20190107091636.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
  
   
 (3)以(2)的formFieldAccessDefinitionOID查詢該活動關卡的存取權限。  
 SQL語法:  

```
SELECT *  
 FROM FormFieldAccessDefinition  
 WHERE OID = '4beb4023e40510048797ab8fbcef89eb';
```

  
 [![](Image_20190107091844.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
  
 (4)把ACT2錯誤的內容跟正確內容(如ACT1)相比,可發現差異如下。  
 [![](Image_20190107084423.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 (5)更正ACT2的formFieldAccessControl內容,補上ENABLED。  
 SQL語法:  
 [![](pro.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 (6)ACT2即可上傳附件。  
 [![](Image_20190107084918.png)](https://www.blogger.com/# "https://www.blogger.com/#")

