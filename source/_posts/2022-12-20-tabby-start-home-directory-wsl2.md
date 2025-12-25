---
layout: post
title: 讓Tabby一啟動WSL就進入Linux使用者目錄
date: 2022-12-20 08:44:00
tags:
- tabby
- wsl2
---

新增以下參數

C:\\Windows\\system32\\wsl.exe ~ -d Ubuntu

參考來源：[https://github.com/Eugeny/tabby/issues/271#issuecomment-450564808](https://github.com/Eugeny/tabby/issues/271#issuecomment-450564808 "https://github.com/Eugeny/tabby/issues/271#issuecomment-450564808")
