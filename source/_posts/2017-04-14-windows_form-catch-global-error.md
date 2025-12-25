---
layout: post
title: Windows Form捕捉全域錯誤並處理
date: 2017-04-14 10:30:00
tags:
- windows form
---
在Program.cs的進入點(Main方法)新增  

```
// 宣告在Application.Run之前
#region 捕捉全域錯誤
Application.ThreadException += new ThreadExceptionEventHandler(OnThreadException);
Application.SetUnhandledExceptionMode(UnhandledExceptionMode.CatchException);
AppDomain.CurrentDomain.UnhandledException += new UnhandledExceptionEventHandler(OnUnhandledException);
#endregion
```

  
 並在OnThreadException和OnUnhandledException事件做處理

參考：[Application.SetUnhandledExceptionMode 方法](https://learn.microsoft.com/zh-tw/dotnet/api/system.windows.forms.application.setunhandledexceptionmode?view=windowsdesktop-8.0 "https://learn.microsoft.com/zh-tw/dotnet/api/system.windows.forms.application.setunhandledexceptionmode?view=windowsdesktop-8.0")
