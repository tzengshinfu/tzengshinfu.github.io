---
layout: post
title: 使用ProcDump+WinDbg定位.NET Framework問題(筆記)
date: 2025-03-04 15:12:00
tags:
- ".net framework"
- procdump
- windbg
---

 1.首要條件

專案>右鍵>屬性>建置>輸出>進階(D)...>輸出>偵錯訊息(E):>僅限 Pdb

[![](image_20250303_083605.png)](image_20250303_083605.png )

  

參考來源：[.NET 知識高裝檢 - .pdb 檔、編譯最佳化與偵錯](https://blog.darkthread.net/blog/about-dotnet-pdb/ "https://blog.darkthread.net/blog/about-dotnet-pdb/")

2.執行ProcDump生成記憶體傾印檔案

procdump -accepteula -ma [TargetApp.exe] [D:\target-app\_dumps]

* **`-accepteula`**：自動接受終端使用者授權協議（EULA），避免在執行時出現提示
* **`-ma`**：生成完整的記憶體傾印，包括所有的記憶體內容，提供最詳細的調試資訊
* **`TargetApp.exe`**：目標應用程式的名稱，即需要監控的程式
* **`D:\target-app_dumps`**：指定記憶體傾印檔案的儲存路徑

參考來源：[ProcDump - Sysinternals](https://learn.microsoft.com/zh-tw/sysinternals/downloads/procdump "https://learn.microsoft.com/zh-tw/sysinternals/downloads/procdump")

3.執行WinDbg分析問題

安裝來源[安裝 Windows 調試程式](https://learn.microsoft.com/zh-tw/windows-hardware/drivers/debugger/ "https://learn.microsoft.com/zh-tw/windows-hardware/drivers/debugger/")

起手式

> 執行!sym noisy

+ 啟用詳細符號載入

> 執行.sympath+ [Pdb路徑]

+ 設定符號搜尋路徑

> 執行.reload
>
> 執行ld\*

+ 強制載入符號

> 執行.loadby sos clr

+ 載入.NET類別資訊偵錯用

> 執行.chain

+ 檢查載入是否成功

再依問題類型下對應指令查詢

參考來源：[真实案例大全](https://github.com/ctripxchuang/dotnetfly "https://github.com/ctripxchuang/dotnetfly")

