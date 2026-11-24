---
title: Docker容器通訊埠轉發
date: 2026-11-24 15:46:57
tags:
- docker
---

場景：  
因某些原因無法修改原本容器的docker-compose.yml,  
如DataEase的mysql-de容器在加入自訂ports mapping後,  
每次升級後設定會被覆蓋的情況就適用本解法。

```yml
services:
  {要監聽的容器名稱}-proxy:
    image: alpine/socat
    container_name: {要監聽的容器名稱}-proxy
    restart: unless-stopped
    command:
      - TCP-LISTEN:{要監聽的容器Port},fork
      - TCP:{要監聽的容器名稱}:{要監聽的容器Port}
    ports:
      - "{要轉發的宿主Port}:{要監聽的容器Port}"
    networks:
      - {docker network ls查詢的網路名稱}

networks:
  {docker network ls查詢的網路名稱}:
    external: true
```

之後就能用{要轉發的宿主Port}連到{要監聽的容器名稱}的服務。
