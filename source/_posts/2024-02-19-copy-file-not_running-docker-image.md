---
layout: post
title: 複製尚未啟動Docker映像檔內的檔案
date: 2024-02-19 14:39:00
tags:
- docker
---

user@host:~$ id=$(docker create "映像檔ID")

user@host:~$ docker cp $id:"檔案的映像檔內部路徑" - > "檔案的外部存放路徑"*(因為會打包成tar檔，所以副檔名要為.tar)*

user@host:~$ docker rm -v $id

參考來源：[Docker - how can I copy a file from an image to a host?](https://stackoverflow.com/a/31316636/1472545 "https://stackoverflow.com/a/31316636/1472545")
