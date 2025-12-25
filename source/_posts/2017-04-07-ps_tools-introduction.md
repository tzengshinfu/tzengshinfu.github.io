---
layout: post
title: PSTools使用簡介
date: 2017-04-07 22:51:00
---
1.**遠端安裝**  
 1.1.

```
psexec \\<遠端電腦名稱> -accepteula -u <有管理權限的帳號> -p <密碼> -h cmd  "/c <指令>“
```

  
1.2. 案例：不在電腦前，想要安裝.net framework 4.6.2，可以下dos指令  

```
psexec \\192.168.3.201 -u prologium\frank_tseng -p <我的密碼> -h cmd /c \\192.168.2.12\mes\NDP462-KB3151800-x86-x64-AllOS-ENU.exe /q /norestart /log %temp%\NDP462-KB3151800-x86-x64-AllOS-ENU.htm
```

  
  
   
 2.**遠端啟動服務**  
 2.1.

```
psservice \\<遠端電腦名稱> -u <有管理權限的帳號> -p <密碼> start <服務名稱>
```

  
 2.2. 案例：不在電腦前，想要啟動遠端桌面的服務，可以下dos指令  

```
psservice \\192.168.3.201 -u prologium\frank_tseng -p <我的密碼> start termservice
```
