---
layout: post
title: 假的SMTP伺服器
date: 2024-03-05 11:47:00
tags:
- docker
- smtp
- testing
---

```
version: "3.8"

services:
  fake-smtp-server:
    container_name: fake-smtp-server
    image: gessnerfl/fake-smtp-server:latest
    restart: always #重開機自動帶起
    ports:
      - "465:465"
      - "8081:8081"
      - "8082:8082"
    environment:
      - FAKESMTP_PORT=465 #SMTP埠號
      - SERVER_PORT=8081 #Web管理介面埠號
      - MANAGEMENT_SERVER_PORT=8082 #API埠號
    volumes:
      - /etc/timezone:/etc/timezone # 使用宿主機時區
      - /etc/localtime:/etc/localtime # 使用宿主機時間
```

啟動後連接到http://<假的SMTP伺服器位址>:8081/可以看到所寄送的郵件列表。

[![](image_20240305_114231.png)](image_20240305_114231.png )

  
  
  
  
  

參考來源：[Fake SMTP Server](https://github.com/gessnerfl/fake-smtp-server "https://github.com/gessnerfl/fake-smtp-server")

