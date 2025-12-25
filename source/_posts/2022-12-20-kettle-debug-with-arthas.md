---
layout: post
title: PDI Kettle異常使用Arthas偵錯排除
date: 2022-12-20 16:12:00
tags:
- arthas
- java
- kettle
---

1.Kettle Spoon的[Run SSH commands]連線異常

[![](image-small.png)](image.png )

  
  

2.下載[Arthas](https://arthas.aliyun.com/doc/ "https://arthas.aliyun.com/doc/")並執行，附加到/<Kettle目錄>/launcher/launcher.jar

3.在GitHub搜尋[source code](https://github.com/jenkinsci/trilead-ssh2/blob/main/src/com/trilead/ssh2/Connection.java "https://github.com/jenkinsci/trilead-ssh2/blob/main/src/com/trilead/ssh2/Connection.java")，得知進行SSH連線的元件是com.trilead.ssh2，方法是connect

4.輸入tt -t com.trilead.ssh2.Connection connect監控connect方法

5.回到Spoon，點擊[Test connection]按鈕重現錯誤，記下INDEX數字(本例為1000)

6.輸入tt -i 1000 -w 'target.connect'觸發錯誤

7.查看~/logs/arthas/arthas.log，發現"Caused by: java.io.IOException: Cannot negotiate, proposals do not match"的異常

8.查詢此[錯誤](https://www.dell.com/support/kbdoc/zh-tw/000196454/srm-4-7-%E5%B7%B2%E6%8E%92%E5%AE%9A-%E5%A0%B1%E5%91%8A-%E9%81%A0%E7%AB%AF-%E4%BD%8D%E7%BD%AE-ssh-%E5%82%B3%E8%BC%B8-%E5%A4%B1%E6%95%97-%E5%87%BA%E7%8F%BE-cannot-negotiate-proposals-do-not-match-%E9%8C%AF%E8%AA%A4 "https://www.dell.com/support/kbdoc/zh-tw/000196454/srm-4-7-%E5%B7%B2%E6%8E%92%E5%AE%9A-%E5%A0%B1%E5%91%8A-%E9%81%A0%E7%AB%AF-%E4%BD%8D%E7%BD%AE-ssh-%E5%82%B3%E8%BC%B8-%E5%A4%B1%E6%95%97-%E5%87%BA%E7%8F%BE-cannot-negotiate-proposals-do-not-match-%E9%8C%AF%E8%AA%A4")為SSH演算法不相容，修改伺服端主機的/etc/ssh/sshd\_config，  
MACS區段加入hmac-sha1-96，Kexalgorithms區段加入diffie-hellman-group-exchange-sha1  
※Windows主機為%programdata%\ssh\sshd\_config

新增內容如下

Match Group administrators

       AuthorizedKeysFile \_\_PROGRAMDATA\_\_/ssh/administrators\_authorized\_keys

Match all<--如果有Match Group要加這行關閉Match block

# Pentaho Kettle [Run SSH commands]

Kexalgorithms +diffie-hellman-group-exchange-sha1

MACS +hmac-sha1-96

HostKeyAlgorithms +ssh-rsa,ssh-dss<--Windows主機再加這行

9.重啟SSH服務

10.Kettle Spoon的[Run SSH commands]連線即正常

PS:Arthas誠為神器也

PS:sshd[啟用log紀錄](https://github.com/PowerShell/Win32-OpenSSH/wiki/Logging-Facilities "https://github.com/PowerShell/Win32-OpenSSH/wiki/Logging-Facilities")會很有幫助

