---
layout: post
title: Windows無法用ssh-copy-id複製公鑰的替代方法
date: 2025-04-03 23:08:00
tags:
- ssh
- windows
---

在命令提示字元視窗執行

```
type %USERPROFILE%\.ssh\[SSH公鑰檔名] | ssh [Linux使用者]@[Linux主機] "cat >> .ssh/authorized_keys"
```

參考來源：[Alternative to ssh-copy-id on windows](https://superuser.com/a/1815968/209426 "https://superuser.com/a/1815968/209426")
