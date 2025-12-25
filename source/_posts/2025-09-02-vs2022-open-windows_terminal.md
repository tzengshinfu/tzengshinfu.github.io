---
layout: post
title: Visual Studio 2022在方案總管直接打開Windows Terminal
date: 2025-09-02 08:51:00
tags:
- visual studio 2022
- windows terminal
---

因為內建終端機快捷鍵與Visual Studio共用，當安裝Clink(擴充cmd.exe功能)時，  
像Ctrl+K(刪除游標後所有字元)會被當成快捷鍵的組合鍵而無效。

可以改在Windows Terminal以解決這個問題。

1.進入工具(T)>選項(O)...>環境>終端

2.新增設定檔，並**設為預設**  
名稱：Windows Terminal  
殼層位置：C:\Windows\System32\cmd.exe  
引數：/c wt.exe -d .\

[![](devenv_20250902_084612.png)](devenv_20250902_084612.png )

  

3.在方案總管任一位置按右鍵>在終端機中開啟，  
即會在對應路徑打開Windows Terminal。

