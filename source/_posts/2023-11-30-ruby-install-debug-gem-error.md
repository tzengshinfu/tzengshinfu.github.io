---
layout: post
title: Ruby在Alpine Linux安裝debug gem失敗
date: 2023-11-30 11:10:00
tags:
- alpine linux
- debugger
- ruby
---

 1.執行gem install debug，顯示錯誤

ERROR:  Error installing debug:

ERROR: Failed to build gem native extension.

2.缺少編譯用元件，

Alpine linux執行apk add make && apk add gcc && apk add libc-dev && gem install debug 即可

Ubuntu linux執行apt install ruby-dev && gem install debug 即可
