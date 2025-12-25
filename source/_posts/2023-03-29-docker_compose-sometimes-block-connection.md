---
layout: post
title: 用docker-compose啟動docker有時佔用內網網段造成連線異常
date: 2023-03-29 13:57:00
tags:
- docker
---

用指令docker network inspect container\_default查詢，

可發現該內網網段被佔用。

1.編輯/etc/docker/daemon.json。(不存在則新增。)

2.編輯內容：

```
{

  "default-address-pools": [



    {



      "base": "172.17.1.0/16",



      "size": 24



    }



  ]

}
```

3.執行docker-compose down關閉container。

4.執行docker network prune清除docker網路設定。

5.執行sudo systemctl restart docker重啟docker服務。

6.執行docker-compose up -d啟動container。
