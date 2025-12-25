---
layout: post
title: EasyFlow與Tiptop整合設定存放處
date: 2019-05-31 16:03:00
tags:
- easyflow gp
- sql
---

```
UPDATE [測試區DB].dbo.TiptopModel   
 SET mappingSet = (SELECT mappingSet FROM [正式區DB].dbo.TiptopModel);   
 /**這table居然在鼎新DB文件裡沒有…*/
```
