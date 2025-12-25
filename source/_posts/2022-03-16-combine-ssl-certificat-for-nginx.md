---
layout: post
title: 合併SSL憑證供Nginx使用
date: 2022-03-16 17:08:00
tags:
- nginx
- ssl
---

```
#cat intermediate.crt                                            intermediate.crt      root.crt                    > ca_bundle.crt
cat  <證書頒發機構名稱>RSAOrganizationValidationSecureServerCA.crt USERTrustRSAAAACA.crt AAACertificateServices.crt > ca_bundle.crt
#cat *_company_com.crt          ca_bundle.crt > server.crt
cat  STAR_<公司名稱>_com.crt ca_bundle.crt > server.crt
```

```
內容由上而下會是
```

```
[STAR_<公司名稱>_com.crt]
```

```
[<證書頒發機構名稱>RSAOrganizationValidationSecureServerCA.crt]
```

```
```
[USERTrustRSAAAACA.crt]
```



```
```
[AAACertificateServices.crt]
```



```
```

```



```
可對比以下2個指令的輸出
```



```
openssl x509 -noout -modulus -in server.crt | openssl md5
```



```
openssl rsa -noout -modulus -in server.key | openssl md5
```



```
如果相同代表組合無誤，不然就是順序錯誤或內容有誤(空格造成位移等)
```



```

```



```
另可執行以下指令檢查憑證到期日
```



```
openssl x509 -enddate -noout -in server.crt
```



輸出如下



notAfter=Apr  6 23:59:59 2026 GMT



```

```
```
```
```

在Nginx設定檔填入

```
server {
    listen 80;

    server_name #網域名稱;

    return 302 https://$host$request_uri; #將http要求導向到https
}
server {
        listen 443 ssl;

        server_name #網域名稱;
        
        ssl_certificate /etc/nginx/cert/server.crt;
        ssl_certificate_key /etc/nginx/cert/server.key;
        ssl_prefer_server_ciphers on;

        location / {
            #既有設定
        }
}
```

```

```

```
再reload Nginx即可
```
