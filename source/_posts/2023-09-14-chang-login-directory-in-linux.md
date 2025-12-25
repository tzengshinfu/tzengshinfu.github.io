---
layout: post
title: Linux修改登入時的目錄位置
date: 2023-09-14 16:33:00
tags:
- linux
---
目標為修改所有使用者登入目錄位置預設為根目錄；

在/etc/profile.d 目錄下新增change-directory-to-root.sh，內容為

```
eval "$( bash -c 'echo "cd /"' )"
```

(如果是用

```
cd / && bash
```

，會再產生一個子進程，退出要執行2次exit。)

參考來源：[shell script - changing current directory from child process - Unix & Linux Stack Exchange](https://unix.stackexchange.com/a/367078 "https://unix.stackexchange.com/a/367078")
