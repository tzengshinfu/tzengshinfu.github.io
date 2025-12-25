---
layout: post
title: SDKMAN無法切換Java版本
date: 2022-11-14 14:01:00
tags:
- sdkman
---

情況：

1.之前已手動安裝Java 11

2.在安裝SDKMAN後，用以下指令其安裝Java 17

```
me@server:~$ sdk install java 17.0.4.1-ms
```

```

```

3.設定Java當前版本

```
me@server:~$ sdk default java 17.0.4.1-ms
```

```

```

4.確認Java當前版本

```
me@server:~$ sdk current java
  

Not using any version of java
```

解法：

1.執行

```
me@server:~$ sdk selfupdate force
```

2.再執行即可

```
me@server:~$ source "$HOME/.sdkman/bin/sdkman-init.sh"
```

參考來源：
[https://stackoverflow.com/a/67084548](https://stackoverflow.com/a/67084548 "https://stackoverflow.com/a/67084548")
