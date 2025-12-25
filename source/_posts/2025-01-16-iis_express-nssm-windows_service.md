---
layout: post
title: IIS Express使用NSSM掛載成本機網站服務
date: 2025-01-16 11:52:00
tags:
- iis express
- nssm
- windows
---

 本機有網頁格式的說明文件，想掛載成網站服務

1.安裝NSSM

執行

```
winget install nssm.nssm
```

2.透過NSSM新增服務

執行

```
nssm install "服務名稱"
```

會啟動設定用的GUI

[![](image_20250116_114557.png)](image_20250116_114557.png )

  

在Path設定<IIS Express路徑>

Arguments設定 /port:<PORT號碼> /path:"<文件路徑>"

PS:如果直接執行sc create "IIS Express" binPath="<IIS Express路徑> /port:<PORT號碼> /path:"<文件路徑>" 新增服務，在啟動時會失敗並顯示"錯誤 1503
: 服務並未已適時的方式回應啟動獲控制請求"，因為IIS Express沒有能以服務啟動的介面。

