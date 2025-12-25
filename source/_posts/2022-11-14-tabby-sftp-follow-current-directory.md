---
layout: post
title: Tabby的SFTP目前目錄跟著終端機cd指令而變動
date: 2022-11-14 15:02:00
tags:
- linux
- tabby
---

 在遠端主機的使用者目錄下的Shell設定檔，

Bash:

編輯~/.bash\_profile(不存在請自建)

加上

```
export PS1="$PS1\[\e]1337;CurrentDir="'$(pwd)\a\]'
```

重新登入即可

ZSH:

編輯~/.zshrc(不存在請自建)

加上

```
precmd () { echo -n "\x1b]1337;CurrentDir=$(pwd)\x07" }
```

重新登入即可
