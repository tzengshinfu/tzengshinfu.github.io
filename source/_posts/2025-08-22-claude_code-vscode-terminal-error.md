---
layout: post
title: Claude Code在VSCode終端機多行輸入及多Profile快捷鍵問題及解法
date: 2025-08-22 09:42:00
tags:
- claude code
- vscode
---

環境

Windows 11 24H2  
VSCode 1.103.1

1. 多行輸入

問題：執行/terminal-setup後，按Shift+Enter每行都以一個多餘的"\"結尾。

[![](478846268-19939a9a-b1a7-48d3-b471-c0748aa34ca4.png)](478846268-19939a9a-b1a7-48d3-b471-c0748aa34ca4.png )

  

解決方法：參考[網友](https://github.com/anthropics/claude-code/issues/1259#issuecomment-3135636804 "https://github.com/anthropics/claude-code/issues/1259#issuecomment-3135636804")的設定。

將"\\\r\n"改成"\u001B\u000A"即可正常運作。

2. 多個設定檔

問題：切換到其他設定檔後，即使執行/terminal-setup也無法使捷徑生效。

原因：不同的設定檔引用了各自的keybindings.json。

解決方案：

1.首先複製快捷鍵配置

%USERPROFILE%\AppData\Roaming\Code\User\keybindings.json。

2.然後切換到新的Profile，按下Ctrl+Shift+P，執行Open Keyboard Shortcuts (JSON)，

並將複製的快捷鍵配置貼上到該Profile的keybindings.json。

或將該Profile的快捷鍵改成與預設Profile共用。

[![](Code_20250822_091245.png)](Code_20250822_091245.png )

  

