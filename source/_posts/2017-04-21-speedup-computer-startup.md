---
layout: post
title: 加速電腦啟動速度
date: 2017-04-21 10:09:00
---
狀況：  
如果有多個耗用資源較多的大型程式(如Outlook, Skype等)  
都設定在開機時啟動，往往會影響開機的啟動速度。  
  
解法：  
改以[工作排程器]延遲執行(如登入後5分鐘啟動)；  
但因為此種執行方式的程式基本優先順序會為"在標準以下"，  
為了不影響大型程式的執行效能，  
所以要另外增加排程如下圖  

[![](pro.png)](pro.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
用wmic指令將大型程式的基本優先順序提高到"標準型"。  

```
wmic process where name="OUTLOOK.EXE" CALL setpriority "normal"
```

