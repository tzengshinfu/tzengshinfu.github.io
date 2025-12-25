---
layout: post
title: 將CRT憑證轉換成PFX格式供IIS使用
date: 2022-03-17 13:04:00
tags:
- internet information server
- ssl
---

```
#cat intermediate.crt                                            intermediate.crt      root.crt                    > ca_bundle.crt
cat  <證書頒發機構名稱>RSAOrganizationValidationSecureServerCA.crt USERTrustRSAAAACA.crt AAACertificateServices.crt > ca_bundle.crt
#產生PFX格式憑證
openssl pkcs12 -export -in STAR_<公司名稱>_com.crt -inkey private.key -certfile ca_bundle.crt -out STAR_<公司名稱>_com.pfx
```

1.安裝步驟可參照網友John Wu心得：[IIS - 安裝SSL憑證](https://blog.johnwu.cc/article/iis-install-ssl-certificate.html "https://blog.johnwu.cc/article/iis-install-ssl-certificate.html")  
2.如果出現【憑證鏈結中缺少一或多個中繼憑證】的錯誤訊息，

[![](image-small.png)](image.png )

則再另外安裝缺少的中繼憑證即可。

步驟可參照：[在執行伺服器驗證的 IIS 電腦上設定中繼憑證](https://docs.microsoft.com/zh-tw/troubleshoot/developer/webapps/iis/www-authentication-authorization/configure-intermediate-certificates "https://docs.microsoft.com/zh-tw/troubleshoot/developer/webapps/iis/www-authentication-authorization/configure-intermediate-certificates")

下圖為現在安裝的所有中繼憑證，缺什麼就裝什麼。

[![](image2-small.png)](image2.png )

3.若需將現有http連線導向至https，

可參考Will保哥心得：[強迫網站轉向到 HTTPS 加密安全連線 ( IIS URL Rewrite )](https://blog.miniasp.com/post/2014/06/04/Redirect-to-HTTPS-from-HTTP-using-IIS-URL-Rewrite "https://blog.miniasp.com/post/2014/06/04/Redirect-to-HTTPS-from-HTTP-using-IIS-URL-Rewrite")

