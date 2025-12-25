---
layout: post
title: Ubuntu 20.04連Oracle資料庫
date: 2023-04-13 23:44:00
tags:
- linux
- oracle
- python
---

1.下載Oracle Instant Client的壓縮包 [Instant Client for Linux x86-64 (64-bit) (oracle.com)](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html#ic_x64_inst "https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html#ic_x64_inst")，本例為instantclient-basiclite-linux.x64-21.9.0.0.0dbru.zip。

2.解壓縮，移至/opt/oracle目錄下，本例為/opt/oracle/instantclient\_21\_9。

3.設定環境變數，在/etc/profile.d目錄下，新增set-ld\_library\_path.sh，內容為：

```
#!/bin/bash



export LD_LIBRARY_PATH="/opt/oracle/instantclient_21_9"
```

4.執行sudo apt install libaio1安裝APT套件。

5.執行pip install cx\_oracle安裝Python套件。

6.完成。
