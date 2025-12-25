---
layout: post
title: Windows 11修改Notepad++檔案圖示
date: 2025-04-25 10:38:00
tags:
- windows 11
---

 想用Notepad++開啟文字檔，卻想保留Windows文字檔案的圖示

1.執行regedit.exe

2.路徑指向HKEY\_CLASSES\_ROOT\Notepad++\_file\DefaultIcon

3.修改(預設值)數值資料為:%SystemRoot%\System32\Shell32.dll,70

4.在文字檔按右鍵，開啟檔案(H)>選擇其他應用程式(C)>Notepad++>一律

5.修改完成

參考來源：[How can I change the icon for Notepad++](https://community.notepad-plus-plus.org/post/99994 "https://community.notepad-plus-plus.org/post/99994")
