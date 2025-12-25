---
layout: post
title: 'Git on Windows: SSL certificate problem: unable to get local issuer certificate'
date: 2024-03-19 20:08:00
tags:
- git
- ssl
- windows
---

狀況：

在Windows平台使用git push/pull/clone等指令遇到錯誤如下，

D:\SomeRepo>git pull

fatal: unable to access 'https://mygit.com/SomeRepo.git/': SSL certificate problem: unable to get local issuer certificate

解法：

設定Windows憑證儲存機制即可。

D:\SomeRepo>git config --system http.sslbackend "schannel"
