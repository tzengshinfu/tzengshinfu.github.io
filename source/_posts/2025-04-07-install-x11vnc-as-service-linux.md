---
layout: post
title: Linux安裝X11VNC並設為服務
date: 2025-04-07 14:12:00
tags:
- linux
- x11vnc
- xrdp
---

```
sudo apt update  
#更新APT套件清單
```

```
sudo apt install -y x11vnc  
#安裝X11VNC
```

```
sudo vncpasswd  
#建立VNC密碼檔(最多8個字元，可包含數字/特殊符號)
```

```
sudo nano /etc/systemd/system/graphical.target  
#新增graphical.target 是一個 systemd 目標單元，負責啟動系統的圖形介面，並確保相關的服務（如顯示管理器和 VNC 服務）在適當的順序下啟動
```

`graphical.target`內容如下：

```
[Unit]  
Description=Graphical Interface  
Documentation=man:systemd.special(7)  
Requires=multi-user.target  
After=multi-user.target  
Conflicts=rescue.target  
Wants=display-manager.service  
Wants=x11vnc.service  
AllowIsolate=yes
```

[Install]  
Alias=default.target

```
sudo nano /etc/systemd/system/x11vnc.service  
#新增X11VNC服務
```

x11vnc.service內容如下：

```
[Unit]  
Description=X11VNC service  
Requires=display-manager.service  
After=display-manager.service
```

[Service]  
Type=forking  
ExecStart=/usr/bin/x11vnc \  
-display
:0 \  
-rfbport 5900 \  
#-localhost \  
-rfbauth [VNC密碼檔路徑] \  
#-shared \  
-bg \  
-xkb
\  
-ncache \  
-ncache\_cr \  
-forever \  
-repeat \  
-auth guess

[Install]  
WantedBy=display-manager.service

```
sudo systemctl daemon-reload  
#重新讀取已新增的服務設定檔
```

```
sudo systemctl start graphical.target  
#啟動graphical.target服務
```

```
sudo systemctl status graphical.target  
#查看graphical.target服務狀態
```

```
sudo systemctl start x11vnc.service  
#啟動X11VNC服務
```

```
sudo systemctl status x11vnc.service  
#查看X11VNC服務狀態
```

  

```
sudo systemctl enable graphical.target  
#將graphical.target服務設為開機啟動
```

```
sudo systemctl enable x11vnc.service  
#將X11VNC服務設為開機啟動
```

(在樹莓派5實測還是[xrdp](https://learn.microsoft.com/zh-tw/azure/virtual-machines/linux/use-remote-desktop?tabs=azure-cli "https://learn.microsoft.com/zh-tw/azure/virtual-machines/linux/use-remote-desktop?tabs=azure-cli")效能較佳)

參考來源：[launch x11vnc on bootup](https://unix.stackexchange.com/a/110308 "https://unix.stackexchange.com/a/110308")
