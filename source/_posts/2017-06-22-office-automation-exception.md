---
layout: post
title: 執行Office Automation異常
date: 2017-06-22 15:53:00
tags:
- ssis
---
狀況：用指令碼工作(或元件)執行Excel會顯示以下錯誤  
[![](Image_20170622143636.png)](Image_20170622143636.png )  
  
  
  
  
  
  
  
解法：  
1.執行【嵌入式管理單元】，指令：mmc(如果Excel是32位元，需新增參數 /32)  
2.【檔案】>>【新增/移除崁入式管理單元】>>新增【元件服務】  

[![](step2.png)](step2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
3.【元件服務】>>【我的電腦】>>【DCOM設定】>>在【Microsoft Excel Application】按右鍵>>【內容】  

[![](step3.png)](step3.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
4.【內容】>>【識別身份】頁籤>>【使用下列使用者】新增執行SQL AGENT的帳號(本例為prologium/mes)  

[![](Image_20170622161048.png)](Image_20170622161048.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
5.【內容】>>【安全性】頁籤>>所有【權限】都新增執行SQL AGENT的帳號(本例為prologium/mes)  

[![](step5.png)](step5.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

[![](step6.png)](step6.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
參考:[Unhandled Exception: System.Runtime.InteropServices.COMException (0x800A03EC)](https://stackoverflow.com/questions/35642527/unhandled-exception-system-runtime-interopservices-comexception-0x800a03ec "https://stackoverflow.com/questions/35642527/unhandled-exception-system-runtime-interopservices-comexception-0x800a03ec")

