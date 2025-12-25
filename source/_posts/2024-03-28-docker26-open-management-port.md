---
layout: post
title: Docker v.26開啟管理port:2375
date: 2024-03-28 19:45:00
tags:
- docker
---

官方文件有2種修改方法：

[Configuring remote access with systemd unit file](https://docs.docker.com/config/daemon/remote-access/#configuring-remote-access-with-systemd-unit-file "https://docs.docker.com/config/daemon/remote-access/#configuring-remote-access-with-systemd-unit-file")

└→不想動到服務設定，不管是docker.service設定檔本身或是override.conf。

[Configuring remote access with daemon.json](https://docs.docker.com/config/daemon/remote-access/#configuring-remote-access-with-daemonjson "https://docs.docker.com/config/daemon/remote-access/#configuring-remote-access-with-daemonjson")

└→無法啟動服務，因為設定與docker.service設定檔沖突。

解決方法：

編輯/etc/default/docker，新增DOCKER\_OPTS="-H tcp://0.0.0.0:2375"，

再執行sudo systemctl daemon-reload && sudo systemctl restart docker，

並驗證如下：

$ sudo netstat -lntp | grep dockerd

tcp6       0      0 :::2375                 :::\*                    LISTEN      534451/dockerd
