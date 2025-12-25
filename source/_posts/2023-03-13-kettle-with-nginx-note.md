---
layout: post
title: Kettle用Nginx作為反向代理的注意事項
date: 2023-03-13 14:02:00
tags:
- docker
- kettle
- nginx
---

場景：

統一用Nginx作為反向代理，而Kettle及Nginx皆為Docker容器。

Nginx:

在Kettle的設定檔，需新增sub\_filter修正WebUI連結，避免找不到網頁錯誤。

{

sub\_filter\_once off;

sub\_filter /kettle/status /kettle/status/;

sub\_filter /kettle/jobStatus /kettle/jobStatus/;

}

Kettle:

需修改<Kettle目錄>/pwd/carte-config-master-8080.xml，

<hostname>localhost</hostname>改為

<hostname>0.0.0.0</hostname>
