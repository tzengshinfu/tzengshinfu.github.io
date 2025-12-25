---
layout: post
title: VSCode在LimeSurvey進行開發除錯
date: 2023-04-21 09:39:00
tags:
- php
- visual studio code
---
情境：

LimeSurvey用Bitnami打包，部署在實體主機；

使用VSCode透過Remote Development在LimeSurvey開發自訂功能。

手順：

1.安裝必要元件，在命令列執行：

```
sudo apt install autoconf gcc libc6-dev make && sudo pecl install xdebug
```

2.編輯/opt/bitnami/php/lib/php.ini，在最後面加上

```
[XDebug]



zend_extension = "/opt/bitnami/php/lib/php/extensions/xdebug.so"



xdebug.mode = debug,develop,trace



xdebug.start_with_request = yes
```

3.重啟LimeSurvey服務，在命令列執行：

```
sudo /opt/bitnami/ctlscript.sh restart
```

4.測試xdebug，在/opt/bitnami/limesurvey目錄新增test.php，內容為

```
<?php



phpinfo();



?>
```

5.瀏覽器連至<LimeSurvey主機網址>/test.php，會顯示PHP設定資訊，如果有xdebug項目代表主機端開啟除錯功能成功。

6.開發端的VSCode安裝PHP除錯[PHP Debug](https://marketplace.visualstudio.com/items?itemName=xdebug.php-debug "https://marketplace.visualstudio.com/items?itemName=xdebug.php-debug")。

7.再用VSCode Remote Development連至該台主機，開啟/opt/bitnami/limesurvey目錄。

8.新增launch.json，會自動增加除錯設定"Listen for Xdebug"，  
此時可以在PHP源碼上打中斷點，再按F5監聽即可。
