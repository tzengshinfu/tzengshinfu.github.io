---
layout: post
title: VSCode 遠端開發無法儲存檔案
date: 2023-04-12 13:45:00
tags:
- linux
- remote development
- visual studio code
---
情境：
VSCode遠端開發透過SSH連至Linux主機，連線帳號為一般帳號(已加入sudo群組)，編輯檔案後無法存檔，會顯示錯誤訊息

Failed to save '[檔案名稱]': Unable to write file 'vscode-remote://ssh-remote+[帳號]@[主機][檔案路徑]' (NoPermissions (FileSystemError): Error: EACCES: permission denied, open '[檔案路徑]')

(如下圖)。  
![](2023-04-12 13 30 54.png)

原因：

微軟表示[VSCode不支援遠端開發儲存檔案時改用sudo權限](https://github.com/microsoft/vscode-remote-release/issues/8269 "https://github.com/microsoft/vscode-remote-release/issues/8269")，

目前能找到的替代方案為【安裝擴展套件[Save as Root in Remote - SSH](https://marketplace.visualstudio.com/items?itemName=yy0931.save-as-root "https://marketplace.visualstudio.com/items?itemName=yy0931.save-as-root")並設定快捷鍵】，

這樣在按下快捷鍵時就會先自動切換到sudo、詢問帳號密碼並儲存成功。

