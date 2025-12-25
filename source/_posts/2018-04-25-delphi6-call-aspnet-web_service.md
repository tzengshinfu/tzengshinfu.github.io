---
layout: post
title: Delphi 6呼叫ASP.NET Web service
date: 2018-04-25 13:32:00
tags:
- delphi
---

1. 用WSDL Import將指定的 Web service 介面轉成 Delphi 的介面。
2. 修改生成的檔案(如service.pas)  
   [1]在RIO := THTTPRIO.Create(nil);的下一行加入  
   RIO.HTTPWebNode.UseUTF8InHeader := True;  
     
   [2]在InvRegistry.RegisterDefaultSOAPAction(TypeInfo(ServiceSoap), 'http://<命名空間>/%operationName%');的下一行加入  
   InvRegistry.RegisterInvokeOptions(TypeInfo(ServiceSoap), ioDocument);
3. 添加參考並使用介面提供的函數呼叫即可[![](step3.png)](step3.png )

  
  

