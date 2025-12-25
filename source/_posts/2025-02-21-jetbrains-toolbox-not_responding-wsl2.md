---
layout: post
title: JetBrains Toolbox在WSL執行未回應
date: 2025-02-21 01:31:00
tags:
- jetbrains toolbox
- wsl2
---

1.依照[SOP](https://www.jetbrains.com/help/idea/installation-guide.html#toolbox_linux "https://www.jetbrains.com/help/idea/installation-guide.html#toolbox_linux")安裝Toolbox。

2.在命令列執行JetBrains Toolbox後無回應

(user@host:/opt/jetbrains-toolbox-<build>$ ./jetbrains-toolbox)

解法：安裝以下元件即可正常執行

sudo apt install libgtk-3-dev

參考來源：[Cannot launch jetbrains-toolbox from WSL2 environment](https://youtrack.jetbrains.com/issue/TBX-8755/Cannot-launch-jetbrains-toolbox-from-WSL2-environment#focus=Comments-27-6724754.0-0 "https://youtrack.jetbrains.com/issue/TBX-8755/Cannot-launch-jetbrains-toolbox-from-WSL2-environment#focus=Comments-27-6724754.0-0")
