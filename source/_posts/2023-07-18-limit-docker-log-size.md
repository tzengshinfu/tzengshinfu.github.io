---
layout: post
title: 限制Docker log大小
date: 2023-07-18 16:39:00
tags:
- docker
---

1.編輯/etc/docker/daemon.json。(不存在則新增。)

2.編輯內容：

```
```
```
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```
```
```

3.執行docker-compose down關閉container。

4.執行docker network prune清除docker網路設定。

5.執行sudo systemctl restart docker重啟docker服務。

6.執行docker-compose up -d啟動container。

參考來源：[JSON File logging driver](https://docs.docker.com/config/containers/logging/json-file/ "https://docs.docker.com/config/containers/logging/json-file/")
