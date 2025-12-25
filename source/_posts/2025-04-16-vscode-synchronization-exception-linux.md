---
layout: post
title: VSCode在Linux同步異常
date: 2025-04-16 21:35:00
tags:
- visual studio code
---
出現錯誤訊息Failed to execute default Web Browser.

[![](1.png)](1.png )

  

解法：

1. 在Settings→Workbench: External Browser輸入已安裝的瀏覽器如firefox。

[![](2.png)](2.png )

  

2. 會跳出Firefox並執行同步登入作業，如果出現以下錯誤  
Error while turning on Settings Sync. Cancelled

則改執行後來跳出的對話框

Would you like to try a different way?(local server)。

[![](3.png)](3.png )

  

3. 設定同步作業成功。

[![](4.png)](4.png )

  

