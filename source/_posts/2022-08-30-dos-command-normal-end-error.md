---
layout: post
title: DOS指令不顯示錯誤訊息且同時ERRORLEVEL設為0(正常結束)
date: 2022-08-30 21:55:00
tags:
- dos command
---
場景：

遠端執行DOS指令搬移檔案，當檔案不存在時ERRORLEVEL變數會被設為1導致後續判斷異常。

解法：

在指令後加上**2>nul | cmd /c ""**

例如：

C:\>move \*.txt D:\ **2>nul | cmd /c ""**

**(2>nul不顯示找不到檔案的錯誤訊息，| cmd /c ""則將ERRORLEVEL設為0)**

C:\>echo %errorlevel%

0
