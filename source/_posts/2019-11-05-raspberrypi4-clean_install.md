---
layout: post
title: 全新樹莓派4安裝
date: 2019-11-05 00:41:00
tags:
- raspberry pi 4
---

# 下載映像檔(本次下載基本桌面版)

[https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/ "https://www.raspberrypi.org/downloads/raspbian/")

# 下載燒錄軟體並寫入SD卡

[https://www.balena.io/etcher/](https://www.raspberrypi.org/downloads/raspbian/ "https://www.raspberrypi.org/downloads/raspbian/")

# 軟體更新

$ sudo apt update
$ sudo apt full-upgrade  
$ sudo shutdown - r now

# HDMI無音效

[https://www.raspberrypi.org/documentation/configuration/audio-config.md](https://www.raspberrypi.org/documentation/configuration/audio-config.md "https://www.raspberrypi.org/documentation/configuration/audio-config.md")

修改/boot/config.txt,取消hdmi\_drive=2的註解,重新開機  
  
# 修改GPU

$ sudo raspi-config

選擇Advanced Options→Memory Split→128  
  
# 修改解析度

$ sudo raspi-config

選擇Advanced Options→選擇Resolution→選擇適合的解析度→Ok→Finish→Reboot  

# 重啟後如果畫面會自動縮小:  
左下角選單→偏好設定→Screen Configuration→右鍵選擇適合的解析度→套用  
  
# 修改鍵盤佈局

$ sudo raspi-config

選擇Localisation Options→選擇Change Keyboard Layout→選擇一般104鍵盤→按下OK→選擇close

# 修改Wifi頻段

$ sudo raspi-config

選擇Localisation Options→選擇Change Wi-fi Country→選擇Taiwan→按下OK→選擇close

# 設定系統自動對時

$ sudo timedatectl set-ntp yes  

# 安裝遠端桌面

$ sudo apt -y install xrdp

# 中文輸入法(預設已安裝)

$ sudo apt install fcitx

# 中文輸入法(倉頡)  
$ sudo apt install fcitx-table-cangjie3

# 中文輸入法(新酷音,預設已安裝)  
$ sudo apt install fcitx-chewing

# 安裝完中文輸入法要重啟  
$ sudo reboot

# 修改輸入法設定  
 選擇全域設定→顯示進階選項→外觀  
 →只有預編輯字串時不顯示輸入視窗→打勾  
 →只有一個候選詞和預編輯字串時不顯示輸入視窗→打勾  
  
# 安裝Samba  
$ sudo apt install samba  
  
# 加入pi到sambashare組  
$ sudo usermod -a -G sambashare pi  
  
# 修改pi的Samba密碼  
$ sudo pdbedit -a -u pi  
  
# 修改/etc/samba/smb.conf  
[global]  
   follow symlinks = yes  
   wide links = yes  
   unix extensions = no  
   strict locking = no  
  
# 加入到/etc/samba/smb.conf  
[pi]  
  comment = pi's home  
  path = /home/pi  
  read only = no  
  guest ok = no  
  browseable = yes  
  create mask = 0644  
  directory mask = 0755  
  
參考來源:  
[raspberry-pi-samba-setup-tutorial](https://blog.gtwang.org/iot/raspberry-pi/raspberry-pi-samba-setup-tutorial/?source=post_page-----b6a23c06c5a---------------------- "https://blog.gtwang.org/iot/raspberry-pi/raspberry-pi-samba-setup-tutorial/?source=post_page-----b6a23c06c5a----------------------")
