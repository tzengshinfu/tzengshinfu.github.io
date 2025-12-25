---
layout: post
title: ReportingService每日首次啟動緩慢
date: 2017-06-27 17:50:00
tags:
- ssrs
---
SSRS每12小時會回收資源,造成每日首次啟動緩慢的現象  
我們可以增加RsReportServer.config的RecycleTime  
但如果設太長導致未收回,恐會資源耗盡影響主機運作。  
  
較佳解法:  
1.在SQL Agent設定每1分鐘執行1次的排程,  
作用是模擬開啟SSRS首頁的行為,在資源回收後強制重新建立,  
加快使用者開啟報表速度。  
  
2.執行類型:CmdExec  
指令如下:  

```
curl --ntlm --user <網域>/<使用者帳號>:<密碼> "http://localhost/ReportServer/Pages/ReportViewer.aspx?%2f報表名稱"
```

PS:curl執行檔需另外下載。  

[![](runcurl.png)](runcurl.png )

  

