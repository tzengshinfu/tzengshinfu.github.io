---
layout: post
title: KeePassXC自動輸入{CLEARFIELD}無法清除欄位內容
date: 2025-03-04 11:05:00
tags:
- keepassxc
---

由KeePass改用跨平台的KeePassXC，

發現原本設定的自動輸入{CLEARFIELD}不會清除已有文字存在的欄位內容。

解法：

將{CLEARFIELD}改為^a{DELETE}即可。

參考來源：[{CLEARFIELD} not working on Windows 11 either (with SQuirreL)](https://github.com/keepassxreboot/keepassxc/issues/10916#issuecomment-2175914913 "https://github.com/keepassxreboot/keepassxc/issues/10916#issuecomment-2175914913")
