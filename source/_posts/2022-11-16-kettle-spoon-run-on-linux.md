---
layout: post
title: Kettle Spoon在Linux主機執行相關設定
date: 2022-11-16 17:08:00
tags:
- kettle
- linux
- spoon
- wsl2
---

因為Kettle目前仍不能像VSCode或Intellij等軟體使用WSL2執行並除錯，  
為彌平開發環境(Windows)與部署環境(Linux)的差異，  
決定將開發區移至另一台與部署環境設定相同的Linux主機。

1.安裝Java(推薦使用SDKMAN)

2.安裝Kettle([注意事項](https://tzengshinfu.blogspot.com/2022/06/kettle.html "https://tzengshinfu.blogspot.com/2022/06/kettle.html"))

3.安裝Fcitx中文輸入法

4.Linux安裝Xfce桌面([教程](https://www.linuxmi.com/ubuntu-20-04-xfce.html "https://www.linuxmi.com/ubuntu-20-04-xfce.html"))

5.安裝遠端桌面Xrdp([教程](https://learn.microsoft.com/zh-tw/azure/virtual-machines/linux/use-remote-desktop?tabs=azure-cli "https://learn.microsoft.com/zh-tw/azure/virtual-machines/linux/use-remote-desktop?tabs=azure-cli"))

效果圖：

[![](img-20221116-171316.png)](img-20221116-171316.png )

  
  

※2023/03/14更新，Windows 10組建 19044+已可執行Kettle GUI程式，

建立程式捷徑如下：

```
> <wslg.exe路徑> (--user <使用者帳號>) -- <spoon.sh路徑>
```

※2023/04/25更新，WSLg程式中文字型顯示亂碼，可安裝Windows字型

在WSL2命令列執行指令如下：

```
$ sudo ln -s /mnt/c/Windows/Fonts /usr/share/fonts/truetype/windows  
$ fc-cache -fv
```

```

```

參考來源：[https://github.com/microsoft/wslg/issues/9#issuecomment-835320480](https://github.com/microsoft/wslg/issues/9#issuecomment-835320480 "https://github.com/microsoft/wslg/issues/9#issuecomment-835320480")

※2024/05/22更新，WSLg安裝中文輸入法

在WSL2命令列執行指令如下：  

```
$ sudo apt install fcitx # 中文輸入法  
$ sudo apt install fcitx-table-cangjie3 # 倉頡第3代  
$ sudo apt install fcitx-chewing # 新酷音
```

編輯/etc/locale.gen  
  
取消註解 zh\_TW.UTF-8 UTF-8  
  
編輯~/.profile

新增以下設定  

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export DefaultIMModule=fcitx
fcitx-autostart &>/dev/null
```

套用設定  
$ source ~/.profile  
  
參考來源：[https://www.80shihua.com/archives/2994](https://github.com/microsoft/wslg/issues/9#issuecomment-835320480 "https://github.com/microsoft/wslg/issues/9#issuecomment-835320480")

