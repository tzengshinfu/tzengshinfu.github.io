---
title: Windows終端機直接上傳下載檔案的輕量級方案
date: 2026-04-22 13:09:22
tags:
- windows terminal
---

場景說明

- 本機: Windows
- 遠端: Linux

設定手順

1. 在本機執行`winget install tssh`安裝**trzsz-ssh(tssh)**。
2. 在本機執行`winget install lrzsz`安裝**lrzsz**。
3. 修改%USERPROFILE%\.ssh\config，新增以下區段以支援*ZMODEM檔案傳輸*：

```config
Host *
    #!! EnableZmodem Yes
```

另外如果要啟用拖拉檔案自動上傳遠端，則需要加上以下2行：  
(注意，*使用者帳戶控制*必須啟用，而且Windows終端機不能以*系統管理員*身份執行。)

```config
    #!! EnableDragFile Yes
    #!! DragFileUploadCommand rz
```

4. 原本ssh連線指令改用tssh連線，其餘參數不變。
5. 要上傳本機檔案到遠端，在遠端執行`rz`，會顯示檔案選擇介面以選取上傳檔案。  
[![](WindowsTerminal_20260422_133132.png)](WindowsTerminal_20260422_133132.png)
6. 要下載遠端檔案到本機，在遠端執行`sz {檔案名稱}`，會顯示資料夾選擇介面以選取下載儲存路徑。  
[![](WindowsTerminal_20260422_133817.png)](WindowsTerminal_20260422_133817.png)

參考來源：[Plugin: add support for [XYZ]MODEM file transfers](https://github.com/microsoft/terminal/issues/1999#issuecomment-1828895334)
