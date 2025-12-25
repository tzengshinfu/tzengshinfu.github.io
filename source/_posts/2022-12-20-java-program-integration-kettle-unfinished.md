---
layout: post
title: Java程式整合Kettle(未完成)
date: 2022-12-20 14:50:00
tags:
- java
- kettle
---

Kettle除了獨立運行的Carte Server，透過呼叫Rest API方式啟動Job及Transformer之外，

還有Java API可整合到系統內部。

Oracle資料庫驅動程式因為[Oracle許可證不允許](https://stackoverflow.com/a/1074971 "https://stackoverflow.com/a/1074971")發布在公共Maven倉庫，所以必須手動下載到自建的內部Maven倉庫。

Kettle核心庫也必須手動下載到自建的內部Maven倉庫。

mvn install:install-file -Dfile=jtds-1.3.1.jar -DgroupId=net.sourceforge.jtds -DartifactId=jtds -Dversion=1.3.1 -Dpackaging=jar #舊版(2008以前)MSSQL支援

mvn install:install-file -Dfile=ojdbc7.jar -DgroupId=com.oracle -DartifactId=ojdbc7 -Dversion=12.1.0.2 -Dpackaging=jar #舊版(10g)Oracle支援

mvn install:install-file -Dfile=orai18n.jar -DgroupId=com.oracle.ojdbc -DartifactId=orai18n -Dversion=19.3.0.0 -Dpackaging=jar #Oracle多語系支援

mvn install:install-file -Dfile=metastore-9.3.0.0-428.jar -DgroupId=org.pentaho -DartifactId=libformula -Dversion=9.3.0.0-428 -Dpackaging=jar

mvn install:install-file -Dfile=libformula-9.3.0.0-428.jar -DgroupId=org.pentaho.reporting.library -DartifactId=libformula -Dversion=9.3.0.0-428 -Dpackaging=jar

mvn install:install-file -Dfile=kettle-core-9.3.0.0-428.jar -DgroupId=pentaho-kettle -DartifactId=kettle-core -Dversion=9.3.0.0-428 -Dpackaging=jar

mvn install:install-file -Dfile=kettle-engine-9.3.0.0-428.jar -DgroupId=pentaho-kettle -DartifactId=kettle-engine -Dversion=9.3.0.0-428 -Dpackaging=jar

mvn install:install-file -Dfile=pentaho-encryption-support-9.3.0.0-428.jar -DgroupId=org.pentaho -DartifactId=pentaho-encryption-support -Dversion=9.3.0.0-428 -Dpackaging=jar

mvn install:install-file -Dfile=js-1.7R3.jar -DgroupId=org.mozilla -DartifactId=javascript -Dversion=1.7R3 -Dpackaging=jar

※目前進度卡在載入plugin失敗，仍無法克服。

※而且考量此整合方式如同再造一台Kettle AP主機，並且需自行開發與Carte Server的API查詢Job狀態相同的功能，故就此打住不再繼續研究。

※成功經驗的先進網友xuanbo的[代碼倉庫](https://github.com/xuanbo/kettle-web "https://github.com/xuanbo/kettle-web")
