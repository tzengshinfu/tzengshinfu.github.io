---
layout: post
title: 設定Windows 10右下角通知停留時間
date: 2024-07-09 15:05:00
tags:
- windows
---

 1.設定->輕鬆存取

[![](image_20240709_143953.png)](image_20240709_143953.png )

  

2.簡化及個人化Windows->顯示通知->修改訊息停置秒數

[![](image_20240709_144030.png)](image_20240709_144030.png )

  

3.自訂秒數則需修改註冊檔，

路徑：HKEY\_CURRENT\_USER\Control Panel\Accessibility

底數改為十進位，並修改數值資料為訊息停置秒數，

登出或重開機套用變更。

[![](image_20240709_144116.png)](image_20240709_144116.png )

  

參考來源：[Windows 10 show notification time setting is not working](https://answers.microsoft.com/en-us/windows/forum/all/windows-10-show-notification-time-setting-is-not/fa81b950-4808-4afa-9fc2-e14e3a28ce88 "https://answers.microsoft.com/en-us/windows/forum/all/windows-10-show-notification-time-setting-is-not/fa81b950-4808-4afa-9fc2-e14e3a28ce88")

