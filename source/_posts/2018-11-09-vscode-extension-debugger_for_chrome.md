---
layout: post
title: Visual Studio Code插件Debugger for Chrome偵錯本機檔案
date: 2018-11-09 09:16:00
tags:
- chrome
- debugger
- visual studio code
---
1.Visual Studio Code→開啟要偵錯的檔案的【所在資料夾】。  
  
2.編輯偵錯組態檔launch.json如下:

```
{   
 /**使用 IntelliSense 以得知可用的屬性。*/   
 /**暫留以檢視現有屬性的描述。*/   
 /**如需詳細資訊，請瀏覽: https://go.microsoft.com/fwlink/?linkid=830387*/   
 "version": "0.2.0",   
 "configurations": [   
 {   
 "type": "chrome",   
 "request": "launch",   
 "name": "本機檔案偵錯",   
 /**"file": "${workspaceFolder}/<指定檔案名稱>",*/ /**-->每次都偵錯此檔案*/   
 "file": "${file}", /**-->或偵錯目前所編輯的檔案*/   
 "sourceMaps": true,   
 "userDataDir": "${workspaceFolder}/profile"   
 }   
 ]   
 }
```
