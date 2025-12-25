---
layout: post
title: MariaDB開放外連
date: 2024-02-06 16:13:00
tags:
- mariadb
---

 1.修改 /etc/mysql/mariadb.conf.d/50-server.cnf

將

bind-address            = 127.0.0.1

改成

bind-address            = 0.0.0.0

2.重啟服務，輸入以下指令

user@host:~$ sudo systemctl restart mysql.service

3.進入MariaDB主控台，輸入以下指令

user@host:~$ mysql -u<DB帳號> -p<DB帳號密碼>

4.設定要外連的資料庫，輸入以下指令

MariaDB [(none)]> use <DB名稱>

5.設定要外連的帳號和IP位址，輸入以下指令

MariaDB [<DB名稱>]> GRANT ALL ON <DB名稱>.\* to '<DB帳號>'@'<外連的IP位址>' IDENTIFIED BY '<DB帳號密碼>' WITH GRANT OPTION

6.重新讀取權限，輸入以下指令

MariaDB [<DB名稱>]> FLUSH PRIVILEGES

7.生效，輸入以下指令退出MariaDB主控台

MariaDB [<DB名稱>]> EXIT
