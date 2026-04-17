---
title: WSL2鏡像網路模式異常處理
date: 2026-04-17 10:09:55
tags:
- wsl2
---

## 問題

在.wslconfig設定*鏡像網路模式*，  

```toml
[wsl2]
networkingMode=mirrored
```

啟動時遭遇以下錯誤而無法連接到其他內網主機。  

```powershell
CreateInstance/CreateVm/ConfigureNetworking/0x8007054f
wsl: 無法設定 networkingMode Mirrored 的網络
```

## 解法

1. 關閉WSL2及WSL2網路服務。  

```powershell
wsl --shutdown
net stop winnat
net start winnat
sc stop WSLService
```

2. 使用Process Explorer查看並移除與WSL2相關的佔用。  
[![](procexp64_20260417_104243.png)](procexp64_20260417_104243.png)

3. 重啟WSL2即可。

參考來源：[Error code: CreateInstance/CreateVm/ConfigureNetworking/0x8007054fs](https://github.com/microsoft/WSL/issues/12351#issuecomment-4140573866)
