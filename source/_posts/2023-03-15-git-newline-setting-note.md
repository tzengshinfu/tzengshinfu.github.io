---
layout: post
title: 開發端在不同OS的git換行符號設定
date: 2023-03-15 23:28:00
tags:
- git
- linux
- windows
---

先前將git repository push到版控主機，  
使用VSCode remote development在另一台server(Ubuntu 20.04)開發，

在重新pull git repository後，

執行shellscript顯示錯誤訊息xxxx.sh:
/bin/sh^M: bad interpreter: No such file or directory  
詢問New Bing後應該是跟git的換行符號設定有關。

先用Notepad++開啟該檔並開啟View→Show
Symbol→Show All Characters，  
發現換行符號不是Linux的[LF]而是Windows的[CR][LF]。

再查該台Ubuntu的git轉換換行符號的設定，  
user@host:path$ git config --global
core.autocrlf  
居然顯示為true

這代表雖然push到repository時是[LF]，但在該台Ubuntu執行pull時，  
卻又被轉換成[CR][LF]而造成執行錯誤。

所以在該台Linux主機執行

user@host:path$ sudo git config --**global**core.autocrlf **input**  
(--**global**代表該帳號的全局設定；而**input**代表push時轉成[LF]，pull時不變動。)

另外再執行

user@host:path$ sudo git config --**system**core.autocrlf **input**  
(--**system**代表整個系統所有帳號都適用這個規則。)

而在Windows主機則是執行

C:\Users\user> git config --**system** core.autocrlf **true**

C:\Users\user> git config --**global** core.autocrlf **true**

(**true**代表push時轉成[LF]，但在pull時要自動轉成[CR][LF]。)
