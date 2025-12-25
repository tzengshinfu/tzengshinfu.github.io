---
layout: post
title: Windows新電腦快速還原安裝程式(含設定)
date: 2025-03-07 15:27:00
tags:
- windows
---

1. 在舊電腦的準備工作

   #### 本例"存放路徑"為使用者文件(%USERPROFILE%\Documents)

   1. 匯出**已安裝程式清單**檔案  
      執行

      ```
      winget export --output [存放路徑]\[已安裝程式清單JSON檔]
      ```
   2. 複製已安裝程式設定檔資料夾到存放路徑
   3. 工作排程器>匯出>將工作XML檔儲存到存放路徑(如果有需要)
   4. 複製使用者捷徑到存放路徑(如果有需要)
   5. 複製使用者啟動資料夾捷徑到存放路徑(如果有需要)
   6. 記錄使用者路徑(Path)環境變數
2. 在新電腦執行匯入

   1. 執行

      ```
      winget import --import-file [存放路徑]\[已安裝程式清單JSON檔]
      ```
   2. 將已安裝程式的設定檔資料夾重新指向存放路徑

      #### 以下指令需以BatchScript形式執行

      ```
      :: 以下是檢查檔案是否為連結的範例
      :: 檢查.gitconfig檔案是否為連結
      DIR "%USERPROFILE%" | FINDSTR ".gitconfig" | FINDSTR "<SYMLINK>"

      :: 如果不是，刪除並建立連結到存放路徑
      IF %ERRORLEVEL% EQU 1 (
       DEL /Q "%USERPROFILE%\.gitconfig"
       MKLINK "%USERPROFILE%\.gitconfig" "[存放路徑]\.gitconfig"
      )

      :: 以下是檢查目錄是否為連結的範例
      :: 檢查.ssh資料夾是否為連結
      DIR "%USERPROFILE%" | FINDSTR ".ssh" | FINDSTR "<JUNCTION>"

      :: 如果不是，刪除並建立連結到存放路徑
      IF %ERRORLEVEL% EQU 1 (
       RMDIR /S /Q "%USERPROFILE%\.ssh"
       MKLINK /J "%USERPROFILE%\.ssh" "[存放路徑]\.ssh"
      )
      ```
   3. 匯入工作排程(如果有需要)  
      執行

      ```
      SCHTASKS /CREATE /TN \%USERNAME%\[工作名稱] /XML "[存放路徑]\[工作XML檔]"
      ```
   4. 複製捷徑至使用者開始功能表以利後續釘選(如果有需要)  
      執行

      ```
      XCOPY /S "[存放路徑]\[開始功能表捷徑資料夾]\*" "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\"
      ```
   5. 複製捷徑至使用者啟動資料夾(如果有需要)  
      執行

      ```
      XCOPY /S "[存放路徑]\[啟動捷徑資料夾]\*" "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
      ```
   6. 設定使用者路徑(Path)變數(如果有需要)

      #### 以下指令需以BatchScript形式執行

      ```
      FOR /F "delims=" %%A IN ('PowerShell -NoProfile -Command "(Get-ItemProperty HKCU:\Environment).Path"') DO SET UserPath=%%A
      SETX Path "%UserPath%";[使用者路徑清單(以分號區隔)]
      SET UserPath=
      ```
