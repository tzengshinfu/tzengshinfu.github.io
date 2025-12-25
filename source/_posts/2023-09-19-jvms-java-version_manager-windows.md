---
layout: post
title: JVMS - Java version manager for Windows
date: 2023-09-19 11:44:00
tags:
- java
- windows
---

[JVMS](https://github.com/ystyle/jvms "https://github.com/ystyle/jvms")作用與Linux平台的SDKMan!相同，可安裝管理不同版本的Java JDK。

※另外一套[Jabba](https://github.com/shyiko/jabba "https://github.com/shyiko/jabba")雖然⭐數有2.7k，但在Windows 10切換版本根本沒有作用。

安裝執行如下：

0.移除本機已安裝的所有Java版本。

1.下載[最新版](https://github.com/ystyle/jvms/releases "https://github.com/ystyle/jvms/releases")JVMS。

2.解壓縮放到%USERPROFILE%\.jvms目錄下。

3.執行jvms init初始化。

4.JVMS會建立全域系統變數JAVA\_HOME=C:\Program Files\jdk，實際指向%USERPROFILE%\.jvms\store\<所安裝的Java版本>，並在Path變數新增C:\Program Files\jdk\bin項目。

5.查看遠端指定Java版本可執行如：jvms rls -a | find "1.6"。

6.執行jvms install <Java版本>，如：jvms install 1.6.0\_43，可安裝1個或多個Java版本。

7.執行jvms switch <Java版本>，如：jvms switch 1.6.0\_43，切換到想要的Java版本。

8.執行java -version驗證切換結果。
