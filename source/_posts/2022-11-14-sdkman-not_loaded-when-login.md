---
layout: post
title: SDKMAN在登入時無法使用
date: 2022-11-14 19:04:00
tags:
- sdkman
---
因SDKMAN設定指令預設是寫入.bashrc，  
但.bashrc是非登入的操作命令(登入後再另開terminal視窗時)才會生效，  
為了可以在登入時直接使用SDKMAN指令，  
可在.bash\_profile加上  

```
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi
```

參考來源：[https://joshstaiger.org/archives/2005/07/bash\_profile\_vs.html](https://joshstaiger.org/archives/2005/07/bash_profile_vs.html "https://joshstaiger.org/archives/2005/07/bash_profile_vs.html")
