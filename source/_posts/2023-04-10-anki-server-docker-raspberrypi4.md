---
layout: post
title: 用Docker在樹莓派建立Anki同步伺服器
date: 2023-04-10 23:21:00
tags:
- anki
- docker
- raspberry pi 4
---
情境：  
客戶端為AnkiDroid，伺服器端為自建Anki同步主機，  
架在樹莓派，使用ISP派發的固定IP，但不使用DNS。  
  
手順：  
1.樹莓派需安裝docker及docker compose。  
2.建立/opt/anki目錄，在其下建立資料夾app、cert、conf.d、log。  
3.在其下建立docker-compose.yml，以啟動Anki同步主機及前端Nginx服務，  
內容為：

```
version: "3"

services:
    anki:
        image: ankicommunity/anki-sync-server-rs:latest
        container_name: anki
        working_dir: "/app"
        restart: always #開機即自動重新啟動
        ports:
          - "27701:27701"
        volumes:
          - ./app:/app
    nginx:
        image:
        container_name: nginx:latest
        restart: always #開機即自動重新啟動
        ports:
          - "8443:8443"
        volumes:
          - ./cert:/etc/nginx/cert
          - ./conf.d:/etc/nginx/conf.d
          - ./log:/var/log/nginx
```

4.在app資料夾建立Anki同步主機設定檔(ankisyncd.toml)，  
內容為：

```
[listen]
host = "0.0.0.0"
port = 27701

[paths]
root_dir = "."

[encryption]
ssl_enable = false
cert_file = ""
key_file = ""
```

5.建立自簽章憑證(AnkiDroid只能透過https與主機同步，但雙方只要有CA憑證即可)  
5-1.執行wget https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-linux-arm64  
5-2.執行sudo mv mkcert-v1.4.4-linux-arm64 /usr/bin/mkcert  
5-3.執行chmod +x /usr/bin/mkcert，設定為'可執行'權限。  
5-4.執行mkcert -install，以產生Root CA憑證。  
5-5.執行mkcert my-cert <ISP派發的固定IP> localhost 127.0.0.1 ::1  
5-6.將產生的憑證移到cert資料夾。  
  
6.設定前端Nginx https站台，在conf.d資料夾建立設定檔(Anki.conf)，  
內容為：

```
server {
    listen <自訂https port> ssl;
    listen [::]:<自訂https port> ssl;

    server_name <ISP派發的固定IP>;

    ssl_certificate cert/<mkcert生成的CA憑證>;
    ssl_certificate_key cert/<mkcert生成的CA憑證Key>;

    location / {
        client_max_body_size 0;

        proxy_pass http://172.17.0.1:27701; # 宿主機
    }
```

7.建立Anki使用者帳號密碼(AnkiDroid與主機同步用)  
執行docker-compose run anki ankisyncd user -a <使用者帳號> <使用者密碼>  
  
8.執行docker compose up -d  
9.執行mkcert -CAROOT，顯示Root CA憑證路徑，將該路徑的rootCA.pem安裝到Android手機。  
  
10.設定AnkiDroid客戶端，  
設定→AnkiDroid→AnkiWeb 帳號輸入<使用者帳號>及<使用者密碼>→  
進階設定→自訂同步伺服器→選取'使用自訂同步伺服器'→  
同步地址輸入"https://<ISP派發的固定IP>:<自訂https port>"→  
媒體檔案同步地址輸入"https://<ISP派發的固定IP>:<自訂https port>/msync"  
  
11.完成。
  
  
參考：  
[anki自定义同步服务器，附自建教程和福利](https://zhuanlan.zhihu.com/p/414484355 "https://zhuanlan.zhihu.com/p/414484355")  
[使用 anki-sync-server-rs 部署自己的 anki 同步服务](https://www.bilibili.com/read/cv15441748 "https://www.bilibili.com/read/cv15441748")  
[How to Create Locally Trusted SSL Certificates with mkcert on Ubuntu 20.04](https://www.howtoforge.com/how-to-create-locally-trusted-ssl-certificates-with-mkcert-on-ubuntu/#install-mkcert "https://www.howtoforge.com/how-to-create-locally-trusted-ssl-certificates-with-mkcert-on-ubuntu/#install-mkcert")
