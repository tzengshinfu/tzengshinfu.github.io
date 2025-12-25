---
layout: post
title: 建立磁碟用量監控機制
date: 2017-04-17 14:14:00
tags:
- ssis
---
1.用dos指令取得欲監控主機的固定式磁碟使用率(drivetype=3)  

```
wmic logicaldisk where drivetype=3 get SystemName,Name,Size,FreeSpace > .\127.0.0.1.txt
```

  
  
2.[欲監控主機]的[系統管理工具]>>[工作排程器]設定每小時25及55分執行1次[取得主機固定式磁碟使用率]的dos指令並匯出文字檔。  

[![](step1.png)](step1.png )

  

[![](step2.png)](step2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
3.使用SSIS解析文字檔，將超標數值設為[Parameters]，當使用率大於等於超標界線時即發信通知管理者。  

[![](step3.png)](step3.png )

  
  

