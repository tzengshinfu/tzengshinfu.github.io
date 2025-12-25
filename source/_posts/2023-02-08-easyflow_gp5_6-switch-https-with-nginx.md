---
layout: post
title: EasyFlow改用https連線(以Nginx作為反向proxy)
date: 2023-02-08 14:24:00
tags:
- easyflow gp
- nginx
- ssl
---

[使用者]→https→[Nginx]→[EasyFlow]

1.EasyFlow位址 http://<EasyFlow FQDN>:<EasyFlow port>/

2.安裝SS憑證後EasyFlow位址 https://<EasyFlow FQDN>/

3.Nginx設定檔

```
http {
    # 設定請求內容大小無限制
    client_max_body_size 0;
}


server {
    listen       443 default_server ssl;
    server_name  <EasyFlow FQDN>;

    ssl_certificate      SSL憑證路徑;
    ssl_certificate_key  PrivateKey路徑;
    ssl_prefer_server_ciphers  on;

    # https://<EasyFlow FQDN>/ -> https://<EasyFlow FQDN>/NaNaWeb/*
    location = / {
        rewrite ^/(.*)$ /NaNaWeb/$1 last;
    }

    # favicon.ico圖示
    location ~* ^/favicon.ico$ {
        proxy_pass http://<EasyFlow FQDN>:<EasyFlow port>;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location ~* ^/NaNaWeb/.*$ {
        proxy_pass http://<EasyFlow FQDN>:<EasyFlow port>;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        sub_filter_once off;
        sub_filter http://<EasyFlow FQDN> https://<EasyFlow FQDN>;
    }
}
```

```
```

```



```
再reload Nginx即可
```
```
