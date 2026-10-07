---
title: Apache Hop docker-compose.yaml設定
date: 2026-10-07 16:22:28
tags:
- apache hop
- docker
---

設定如下，依個人需求新增或修改：

```yml
services:
  hop-server: # 執行管道的伺服器
    image: apache/hop:latest # 注意，生產環境需固定映像檔版本
    ports:
      - "12000:8080" # 設宿主機12000埠(需與hop-web錯開)
    environment:
      HOP_CONFIG_FOLDER: /files/config # 系統設定路徑(資料庫連線設定等)
      HOP_AUDIT_FOLDER: /files/audit
      HOP_PROJECT_FOLDER: /files/projects/usun # 專案路徑
      HOP_PROJECT_NAME: usun # 專案名稱
      HOP_SHARED_JDBC_FOLDERS: /opt/hop/lib/jdbc,/files/jdbc # JDBC驅動程式路徑
      HOP_PLUGIN_BASE_FOLDERS: /opt/hop/plugins,/files/plugins # 外掛路徑
      HOP_SERVER_HOSTNAME: "0.0.0.0"
      HOP_SERVER_PORT: "8080"
      HOP_SERVER_USER: admin
      HOP_SERVER_PASS: admin
      HOP_SERVER_SHUTDOWN_TIMEOUT: "120" # 延遲120秒結束(等內部正常關閉)
      HOP_SERVER_METADATA_FOLDER: /files/projects/usun/metadata # Hop Web Service使用
      HOP_OPTIONS: "-XX:+AggressiveHeap -Duser.timezone=Asia/Taipei" # 時區設為本地端
    volumes: # 對應到宿主機相同路徑如:`./config`，使2個容器能共用設定、專案等
      - ./config:/files/config
      - ./audit:/files/audit
      - ./projects:/files/projects
      - ./jdbc:/files/jdbc
      - ./plugins:/files/plugins
    restart: unless-stopped
    stop_grace_period: 120s

  hop-web: # 設計管道的Web IDE
    image: apache/hop-web:latest # 注意，生產環境需固定映像檔版本
    ports:
      - "12001:8080" # 設宿主機12001埠(需與hop-server錯開)
    environment:
      HOP_CONFIG_FOLDER: /hop/config # 系統設定路徑(資料庫連線設定等)
      HOP_AUDIT_FOLDER: /hop/audit
      HOP_PROJECT_FOLDER: /hop/projects/usun # 專案路徑
      HOP_PROJECT_NAME: usun # 專案名稱
      HOP_SHARED_JDBC_FOLDERS: /usr/local/tomcat/jdbc-drivers,/hop/jdbc # JDBC驅動程式路徑
      HOP_PLUGIN_BASE_FOLDERS: /usr/local/tomcat/plugins,/hop/plugins # 外掛路徑
      HOP_WEB_SECURITY_MODE: BASIC
      HOP_WEB_ADMIN_USER: admin
      HOP_WEB_ADMIN_PASSWORD: admin
      HOP_OPTIONS: "-XX:+AggressiveHeap -Dorg.eclipse.rap.rwt.resourceLocation=/tmp/rwt-resources -Duser.timezone=Asia/Taipei" # 時區設為本地端
    volumes: # 對應到宿主機相同路徑如:`./config`，使2個容器能共用設定、專案等
      - ./config:/hop/config
      - ./audit:/hop/audit
      - ./projects:/hop/projects
      - ./jdbc:/hop/jdbc
      - ./plugins:/hop/plugins

networks:
  hop-network:
    driver: bridge
```
