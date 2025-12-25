---
layout: post
title: 用AutoHotKey建立全域自訂快捷鍵
date: 2024-02-24 00:13:00
tags:
- autohotkey
---

想達到

1.雙按Esc=Ctrl+W(關閉分頁，大部份程式適用)

2.雙按左Ctrl=Alt+←(瀏覽器為回上一頁)

3.雙按左Alt=Alt+→(瀏覽器為到下一頁)

4.按Ctrl+Shift切換輸入法(等同於WinKey+Space)

的目的：

本例使用AutoHotKey v2.0：

0.安裝AutoHotKey v2，執行winget install AutoHotkey.AutoHotkey。

1.開啟AutoHotKey Dash，選擇"New script"並選擇"Minimal for v2"。

2.編輯AHK script，內容為

```
#Requires AutoHotkey v2.0

~Esc::
{
    if (A_PriorHotkey != "~Esc" or A_TimeSincePriorHotkey > 400)
    {
        KeyWait "Esc"
        return
    }

    Send "{Ctrl down}w{Ctrl up}"
}

~LControl::
{
    if (A_PriorHotkey != "~LControl" or A_TimeSincePriorHotkey > 400)
    {
        KeyWait "LControl"
        return
    }

    Send "{Alt down}{Left}{Alt up}"
}

~LAlt:: {
    if (A_PriorHotkey != "~LAlt" or A_TimeSincePriorHotkey > 400)
    {
        KeyWait "LAlt"
        return
    }

    Send "{Alt down}{Right}{Alt up}"
}
```

```
LControl & LShift:: {
    Send "{LWin down}{Space}{LWin up}"
}
```

※**A\_TimeSincePriorHotkey**需依不同執行環境調整。

3.選擇"Compile"，開啟Ahk2Exe轉成執行檔，建立捷徑放在**啟動**資料夾。

參考來源：[KeyWait - Syntax & Usage | AutoHotkey v2](https://www.autohotkey.com/docs/v2/lib/KeyWait.htm#ExDouble "https://www.autohotkey.com/docs/v2/lib/KeyWait.htm#ExDouble")
