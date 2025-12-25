---
layout: post
title: 修改表單欄位資料
date: 2019-05-16 12:39:00
tags:
- easyflow gp
- sql
---

```
SELECT   
 FormInstance.OID,   
 fieldValues,   
 maskFieldValues   
 FROM   
 ProcessInstance   
 JOIN LocalRelevantData ON contextOID = containerOID   
 JOIN FormInstance ON valueOID = FormInstance.OID   
 WHERE   
 ProcessInstance.serialNumber = '[流程序號]';
```

注意事項:   
 1.一般流程改[fieldValues]欄位的XML,   
 如果是TIPTOP發起的流程則[maskFieldValues]及[fieldValues]欄位的XML都要修改。   
 2.Grid控制項有其特殊規則:

[![](Image_20190516123925.png)](Image_20190516123925.png )

