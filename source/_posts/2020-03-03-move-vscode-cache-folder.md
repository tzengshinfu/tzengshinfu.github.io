---
layout: post
title: 將VS Code快取資料夾移到Ram disk以加快執行速度
date: 2020-03-03 00:01:00
tags:
- visual studio code
---

1.將所有開啟中的VS Code程式全部關閉。

或執行

TASKKILL /IM code.exe

2.在C:\Users\{使用者帳號}\AppData\Roaming\Code下

將以下資料夾刪除

\Cache

\CachedConfigurations

\CachedData

\CachedExtensions

\CachedExtensionVSIXs

\CachedProfilesData

\Code Cache

\DawnCache

\FontLookupTableCache

\GPUCache

\logs

\webrtc\_event\_logs

\Service Worker\CacheStorage

\Service Worker\ScriptCache

或執行

RMDIR /S /Q "C:\Users\{使用者帳號}\AppData\Roaming\Code\上述資料夾名稱"

3.

在RAM DISK逐一建立資料夾

或用

MKDIR "{RAM DISK磁碟代號}:\{上述資料夾名稱}"

3.以"系統管理員權限"逐一執行

MKLINK /J "C:\Users\{使用者帳號}\AppData\Roaming\Code\上述資料夾名稱" "{RAM DISK磁碟代號}:\{上述資料夾名稱}"

4.出現捷徑箭頭的上述資料夾,逐一測試點擊內容將連結到Ram disk快取路徑則完成。
