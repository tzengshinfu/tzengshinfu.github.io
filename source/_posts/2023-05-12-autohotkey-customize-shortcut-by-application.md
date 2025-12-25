---
layout: post
title: 用AutoHotKey針對應用程式自訂快捷鍵
date: 2023-05-12 14:51:00
tags:
- autohotkey
---

想在某些無法自訂快捷鍵的應用程式，如：Mozilla ThunderBird，達到按Esc=Ctrl+W，即關閉Tab的~~(偷懶)~~目的，

本例使用AutoHotKey v2.0：

1.開啟AutoHotKey Window Spy，移到ThunderBird視窗，複製整行ahk\_exe thunderbird.exe

2.撰寫AHK script，建立檔案myhotkey.ahk，內容為

```
#Requires AutoHotkey v2.0



HotIfWinActive "ahk_exe thunderbird.exe"



Hotkey "Esc", CloseTab



CloseTab(Thiskey)



{



    Send "{Ctrl down}w{Ctrl up}"



Return



}
```

3.雙點script即執行，亦可用Ahk2Exe轉成執行檔，建立捷徑放在**啟動**資料夾。

參考來源：[HotIf / HotIfWin](https://www.autohotkey.com/docs/v2/lib/HotIf.htm "https://www.autohotkey.com/docs/v2/lib/HotIf.htm")
