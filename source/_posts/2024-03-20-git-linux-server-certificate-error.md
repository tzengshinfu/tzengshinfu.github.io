---
layout: post
title: 'Git on Linux: server certificate verification failed. CAfile: none CRLfile:
date: 2024-03-20 15:28:00
none'
tags:
- git
- linux
- ssl
---

狀況：

在Linux平台使用git push/pull/clone等指令遇到錯誤如下，

SomeUser@SomeServer:~/SomeRepo$ git pull

fatal: unable to access 'https://mygit.com/SomeRepo.git/': server certificate verification failed. CAfile: none CRLfile: none

解法：

將SomeRepo主機SSL憑證上傳至該Linux平台主機存放憑證處即可。

(本例為/etc/ssl/certs/，可用`curl-config --ca`查詢存放處。)
