---
title: VSCode的SFTP擴充套件無法正常上傳下載
date: 2026-09-16 14:44:10
tags:
- visual studio code
---
套件：  
natizyskunk.sftp  
[![](Code_20260916_140959.png)](Code_20260916_140959.png)

情況：  
在上傳下載檔案會顯示錯誤訊息。
[![](Code_20260916_140937.png)](Code_20260916_140937.png)

原因：  
因為隨著VSCode升級，底層Node.js也升至v23並已移除該函數導致異常。

解法：  
執行以下指令  
```bash
cd ~/.vscode/extensions/natizyskunk.sftp-1.16.3
npm install ssh2@1.17.0 --omit=dev
```

參考來源：  
[isDate is not a function (and temporary fix)](https://github.com/Natizyskunk/vscode-sftp/issues/586#issue-4580618915)
