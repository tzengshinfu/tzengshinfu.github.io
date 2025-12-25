---
layout: post
title: 使用JBang產生原生平台程式
date: 2023-08-14 10:33:00
tags:
- java
- jbang
---
1.使用SDKMAN!安裝JBang，

命令列執行

```
sdk install jbang
```

2.安裝VSCode擴展套件JBang(增加引用語法//DEPS自動補完功能)

[https://marketplace.visualstudio.com/items?itemName=jbangdev.jbang-vscode](https://marketplace.visualstudio.com/items?itemName=jbangdev.jbang-vscode "https://marketplace.visualstudio.com/items?itemName=jbangdev.jbang-vscode")

3.初始化，

命令列執行

```
jbang init helloworld.java
```

4.撰寫Java程式

5.偵錯與運行時參數

在.vscode/launch.json
修改如下

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "helloworld",
            "request": "launch",
            "mainClass": "helloworld",
            "projectName": "helloworld.java",
            "args": [
                "args1",
                "args2",
                "args3"
            ]
        }
    ]
}
```

5.產生原生平台程式，

命令列執行

```
jbang --native helloworld.java
```

※進度輸出在編譯log，可用指令去追蹤，

命令列執行

```
tail -f /tmp/jbang[亂數]native-image
```

6.如果編譯時有問題可清除快取，

命令列執行

```
jbang cache clear
```
