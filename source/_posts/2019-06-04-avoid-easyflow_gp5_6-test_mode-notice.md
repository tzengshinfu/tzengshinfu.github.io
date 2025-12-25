---
layout: post
title: 避免EasyFlow測試區跑流程會通知使用者造成不必要的誤解
date: 2019-06-04 17:06:00
tags:
- easyflow gp
- sql
---

```
UPDATE [測試區DB].dbo.Users   
 SET mailAddress = '' /**或改成開發者e-mail帳號*/   
 ,objectVersion = objectVersion + 1   
 WHERE id <> 'administrator';
```
