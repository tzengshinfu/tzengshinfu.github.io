---
layout: post
title: MySQL容器SQL腳本初始化UTF8內容為亂碼
date: 2024-03-13 15:24:00
tags:
- docker
- mysql
---

原因：因為執行初始化的終端環境語系不是UTF-8。

解法：在docker-compose.yml MySQL服務的環境變數加上"LANG: C.UTF-8"即可。

```
version : '3.8'
services:
  mysql:
  ..............
    environment:
      LANG: C.UTF-8 #加上這行
```

參考來源：[Docker Mysql DB 初始化 UTF8 乱码问题的解决](https://www.codesky.me/archives/docker-mysql-utf8-encoded.wind "https://www.codesky.me/archives/docker-mysql-utf8-encoded.wind")
