---
layout: post
title: VSCode新增JShell插件指令(Maven限定)
date: 2022-12-15 09:23:00
tags:
- java
- jshell
- visual studio code
---

在VSCode的設定檔 C:\Users\<使用者帳號>\AppData\Roaming\Code\User\settings.json

新增

```
"maven.terminal.favorites":
[
{
"alias": "jshell",
"command": "com.github.johnpoth:jshell-maven-plugin:1.3:run -Dmaven.test.skip=true"
}
]
```

效果如下：

[![](image-small.png)](image.png )

  
  
  
  

