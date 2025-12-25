---
layout: post
title: 'Linux無法連接MSSQL(provider: SSL Provider, error: 31 - Encryption(ssl/tls) handshake failed)的暫時解法'
date: 2022-09-29 15:01:00
tags:
- java
- linux
- remote development
- sql server
- visual studio code
- wsl2
---
在/etc/ssl/openssl.cnf加入一段

```
#region 連接到USUN-SQL需降低TLS版本
openssl_conf = default_conf

[default_conf]
ssl_conf = ssl_sect

[ssl_sect]
system_default = system_default_sect

[system_default_sect]
MinProtocol = TLSv1
CipherString = DEFAULT@SECLEVEL=1
#endregion
```

Java程式需移除所指向版本目錄的conf/security/java.security

※VSCode + Remote developement + JUnit時，需修改~/.vscode-server/extensions/redhat.java-<插件版本>-linux-x64/jre/<Java版本>-linux-x86\_64/conf/security

找到  
jdk.tls.disabledAlgorithms=SSLv3, TLSv1, TLSv1.1, RC4, DES, MD5withRSA, \  
移除TLSv1, TLSv1.1  
變成  
jdk.tls.disabledAlgorithms=SSLv3, RC4, DES, MD5withRSA, \  
存檔  
  
連線字串需新增  
trustServerCertificate=true

重啟Java程式

但盡速升級MSSQL的SSL版本才是正道。

參考來源：  
[LINUX 下连接 SQL SERVER 数据库遇到了错误](http://www.zhishibo.com/articles/57511.html "http://www.zhishibo.com/articles/57511.html")
