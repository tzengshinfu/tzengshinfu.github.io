---
layout: post
title: 安裝Seafile community版
date: 2020-01-04 20:25:00
tags:
- raspberry pi 4
---

參考來源  
#[https://www.kancloud.cn/kancloud/seafile-manual/51505](https://www.kancloud.cn/kancloud/seafile-manual/51505 "https://www.kancloud.cn/kancloud/seafile-manual/51505")

1.下載Seafile套件  
   
 2.建立資料夾並解壓縮  
 cd /home  
 sudo mkdir haiwen   
 sudo mv seafile-server\_[版本號] haiwen   
 cd haiwen   
 sudo tar -xzf seafile-server\_[版本號]   
 sudo mkdir installed   
 sudo mv seafile-server\_\* installed  
   
 3.安裝Python套件   
 sudo apt update   
 sudo apt install python2.7 python-setuptools python-imaging python-mysqldb   
   
 4.建立root密碼並解鎖(等下MySQL會用到)   
 sudo passwd root   
 sudo passwd --unlock root

5.安裝MariaDB  
 sudo apt install mariadb-server  
 sudo mysql\_secure\_installation   
   
 6.修改Linux 文件最大打開數   
 ulimit -n 30000   
   
 7.開始安裝  
 sudo ./setup-seafile-mysql.sh  
   
 8.設定seafile-data資料夾掛到其他如:NAS設備  
 sudo nano /etc/fstab  
   
 9.修改設定,不限IP可登入管理界面  
編輯/home/haiwen/conf/gunicorn.conf  
 將原本bind = "127.0.0.1:8000"  
 改成bind = "0.0.0.0:8000"

#[https://forum.seafile.com/t/seafile-7-only-listens-to-127-0-0-1/9544/6](https://forum.seafile.com/t/seafile-7-only-listens-to-127-0-0-1/9544/6 "https://forum.seafile.com/t/seafile-7-only-listens-to-127-0-0-1/9544/6")

10.啟動Seafile服務   
 sudo ./seafile.sh start   
 sudo ./seahub.sh start  
  
 11.設定開機啟動

可參考#[https://www.kancloud.cn/kancloud/seafile-manual/51496](https://www.kancloud.cn/kancloud/seafile-manual/51496 "https://www.kancloud.cn/kancloud/seafile-manual/51496")

@刪除自動啟動腳本的-u ${user},直接以root帳號執行

12.如果Seafile服務有對外需修改設定(改成對外IP)

[![](Image_20200210115117.png)](Image_20200210115117.png )

13.安裝client端並登入,設定同步

