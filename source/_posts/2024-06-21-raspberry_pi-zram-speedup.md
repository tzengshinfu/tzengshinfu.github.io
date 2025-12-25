---
layout: post
title: 樹莓派啟用ZRAM以改善效能
date: 2024-06-21 11:26:00
tags:
- raspberry pi 4
- zram
---

 ZRAM解釋 [https://zh.wikipedia.org/zh-tw/Zram](https://zh.wikipedia.org/zh-tw/Zram "https://zh.wikipedia.org/zh-tw/Zram")

*zram仍有利於嵌入式裝置、小筆電和其它相似的低階硬體裝置。這些裝置通常使用固態儲存，它們由於其原生性質而壽命有限，因而避免以其提供交換空間可防止其迅速磨損。此外，使用zRAM還可顯著降低Linux系統用於交換的I/O。*

1.建立設定ZRAM的ShellScript

user@HOST:~ $ sudo nano /usr/local/sbin/zram\_setup.sh

內容如下

#!/bin/bash  
  
memsize=$(free | grep -e "^Mem:" | awk '{print $2}')  
echo $(( $memsize \* 1024 )) | sudo tee /sys/block/zram0/disksize  
mkswap /dev/zram0  
swapon -p 10 /dev/zram0

2.將其設定為可執行檔

user@HOST:~ $ sudo chmod +x /usr/local/sbin/zram\_setup.sh

3.設定服務，指向設定ZRAM的ShellScript

user@HOST:~ $ sudo nano /etc/systemd/system/zram\_setup.service

內容如下

[Service]  
Type=simple  
ExecStart=/usr/local/sbin/zram\_setup.sh

[Install]  
WantedBy=default.target

4.編輯/etc/modules

user@HOST:~ $ sudo nano /etc/modules

新增內容

zram

5.啟用ZRAM服務

user@HOST:~ $ sudo systemctl daemon-reload

user@HOST:~ $ sudo systemctl start zram\_setup.service

user@HOST:~ $ sudo systemctl enable zram\_setup.service

參考來源：[Raspberry Pi 效能改善 – 使用 ZRAM](https://www.team-bob.org/raspberry-pi-%E6%95%88%E8%83%BD%E6%94%B9%E5%96%84-%E4%BD%BF%E7%94%A8-zram/ "https://www.team-bob.org/raspberry-pi-%E6%95%88%E8%83%BD%E6%94%B9%E5%96%84-%E4%BD%BF%E7%94%A8-zram/")
