---
layout: post
title: Linux各資料庫JDBC連線字串
date: 2022-05-30 15:24:00
tags:
- jdbc
---

 MSSQL 2014

jdbc:sqlserver://**<資料庫位址>**:1433;databaseName=**<資料庫名稱>**

※如果資料庫主機因未更新而只能用TLS v1.0連線，連線字串需加上 trustServerCertificate=true

要另外修改java.security內容，開放TLS v1.0

路徑 $JAVA\_HOME/conf/security/java.security

找到 jdk.tls.disabledAlgorithms=SSLv3, TLSv1, TLSv1.1, RC4, DES, MD5withRSA

將TLSv1, TLSv1.1刪除並存檔

Oracle 10g

jdbc:oracle:thin:@**<資料庫位址>**:1521:**<資料庫名稱>**

MariaDB 10

jdbc:mariadb://**<資料庫位址>**:3306/**<資料庫名稱>**
