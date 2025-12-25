---
layout: post
title: 執行遠端主機的DOS指令
date: 2018-05-22 15:09:00
tags:
- dos command
---
用單引號將各參數內容包起來以避免特殊符號造成錯誤(Invalid Global Switch)  

```
%windir%\System32\wbem\wmic.exe /node:'{遠端主機名稱}' /user:'{網域\使用者帳號}' /password:'{密碼}' process call create '{DOS指令}'
```
