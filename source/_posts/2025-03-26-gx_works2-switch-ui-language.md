---
layout: post
title: GX Works2 切換介面語系
date: 2025-03-26 13:24:00
tags:
- gx works2
---

問題：

要切換介面顯示語系，但發現工具>選擇語言是針對工程內容，而不是介面顯示。

解法：

1. 關閉GX Works2。

2. 開啟登錄編輯程式，路徑：

HKEY\_CURRENT\_USER\Software\MITSUBISHI\SWnDN-GPPW2\App\CodePage

編輯 DWORD (32-位元) 值

底數選十進位(D)

數值資料輸入如下：

[![](regedit_20250326_130507.png)](regedit_20250326_130507.png )

  

數值資料內容[說明](https://zh.wikipedia.org/zh-tw/%E4%BB%A3%E7%A0%81%E9%A1%B5 "https://zh.wikipedia.org/zh-tw/%E4%BB%A3%E7%A0%81%E9%A1%B5")：

1252 西歐拉丁字母ISO-8859-1

950  繁體中文（大五碼）

936  簡體中文（GBK）

932  日文（Shift\_JIS）

3. 重新啟動GX Works2即可。

參考來源：[GX WORKS2 1.77F 語言檔問題,簡中,繁中,英文](http://www.ymmfa.com/read-gktid-1371103-uid-3.html "http://www.ymmfa.com/read-gktid-1371103-uid-3.html")

