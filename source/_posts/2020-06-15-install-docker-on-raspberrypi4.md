---
layout: post
title: 樹莓派安裝Docker
date: 2020-06-15 10:07:00
tags:
- docker
- raspberry pi 4
---
# 裝https相關  
$ sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common

# 取得Docker金鑰  
$ curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -

# 編輯Docker來源  
$ echo "deb [arch=armhf] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \ $(lsb\_release -cs) stable" | \ sudo tee /etc/apt/sources.list.d/docker.list

# 安裝Docker  
$ sudo apt install -y --no-install-recommends \ docker-ce \ cgroupfs-mount  
  
# 加入pi到docker組  
$ sudo addgroup --system docker $ sudo adduser pi docker $ newgrp docker

# 設為啟動服務

$ sudo systemctl restart docker  
$ sudo systemctl enable docker

# 測試Docker是否正常  
$ docker run hello-world  
  
# 清理殘留軟體包

$ sudo apt autoremove --purge  
$ sudo apt clean  
  
參考來源:  
[yes-you-can-run-docker-on-raspbian](https://www.blogger.com/# "https://www.blogger.com/#")
