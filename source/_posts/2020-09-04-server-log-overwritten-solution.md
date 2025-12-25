---
layout: post
title: 解決:server.log每次重開機都被覆蓋
date: 2020-09-04 09:03:00
tags:
- easyflow gp
---
路徑:<EasyFlow系統路徑>\jboss-4.2.3.GA\server\default\conf  
修改log4j.xml的節點
param name="Append" value="(改成true)"
位置如下

```
<log4j:configuration xmlns:log4j="http://jakarta.apache.org/log4j/" debug="false">

  <!-- ================================= -->
  <!-- Preserve messages in a local file -->
  <!-- ================================= -->

  <!-- A time/date based rolling appender -->
  <appender name="FILE" class="org.jboss.logging.appender.DailyRollingFileAppender">
    <errorHandler class="org.jboss.logging.util.OnlyOnceErrorHandler"/>
    <param name="File" value="${jboss.server.log.dir}/server.log"/>
    <param name="Append" value="false"/><!--改成true-->
```
