---
layout: post
title: 快速切換網路介面卡設定
date: 2025-03-31 09:57:00
tags:
- windows
---

場景1: 筆電有線網路連接內部路由器與PLC連線

執行

```
netsh interface ip set address "[有線網路名稱]" static [PLC內網的IP位址] 255.255.255.0 [PLC內網的預設閘道IP位址] 1
```

場景2: 回到辦公室改回DHCP

執行

```
netsh interface ip set address "[有線網路名稱]" dhcp
```

上述指令可製成批次檔

(檔案編碼需為Big5)

參考來源：[使用 netsh 設定網路卡 IP 位址 - 1](https://ithelp.ithome.com.tw/m/articles/10080955 "https://ithelp.ithome.com.tw/m/articles/10080955")
