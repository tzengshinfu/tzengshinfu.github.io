---
layout: post
title: Clink使用Tab鍵自動補完指令
date: 2023-05-08 13:29:00
tags:
- clink
- dos command
---
1.新增設定檔，檔案路徑為

%USERPROFILE%\.inputrc

2.修改設定檔，內容為

"\t": clink-insert-suggested-line

參考來源：

[https://github.com/chrisant996/clink/issues/332#issuecomment-1214454590](https://github.com/chrisant996/clink/issues/332#issuecomment-1214454590 "https://github.com/chrisant996/clink/issues/332#issuecomment-1214454590")
