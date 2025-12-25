---
layout: post
title: Maven 3.8.1+阻擋HTTP repositories(Blocked mirror for repositories)
date: 2023-05-12 11:26:00
tags:
- java
- maven
---

問題：

Maven無法下載私服套件，錯誤訊息如下：

[**ERROR**] Failed to execute goal on project xxx: **Could not resolve dependencies for project
xxx:jar:1.5: Failed to collect dependencies at xxx:jar:1.0**: Failed to read artifact descriptor
for xxx:jar:1.0: Could not transfer artifact xxx:pom:1.0 from/to maven-default-http-blocker (http://0.0.0.0/):
Blocked mirror for repositories: [ooo (http://maven.ooo.org/nexus/content/repositories/ooo, default, releases)]
-> **[Help 1]**

因為3.8.1+預設阻擋非HTTPS的倉庫。([來源](https://maven.apache.org/docs/3.8.1/release-notes.html "https://maven.apache.org/docs/3.8.1/release-notes.html"))

解法：

在${user.home}/.m2/settings.xml新增以下內容

```
<?xml version="1.0" encoding="UTF-8"?>



<settings xmlns="http://maven.apache.org/SETTINGS/1.2.0"



  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"



  xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.2.0
    https://maven.apache.org/xsd/settings-1.2.0.xsd">



  <mirrors>



    <mirror>



      <id>maven-default-http-blocker</id>



      <mirrorOf>dummy</mirrorOf>



      <name>Pseudo repository to mirror external repositories initially using HTTP.</name>



      <url>http://0.0.0.0/</url>



      <blocked>false</blocked>



    </mirror>



  </mirrors>



</settings>
```

參考來源：[How to disable maven blocking
external HTTP repositories?](https://stackoverflow.com/a/68394404 "https://stackoverflow.com/a/68394404")
