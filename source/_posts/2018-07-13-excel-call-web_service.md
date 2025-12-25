---
layout: post
title: Excel叫用Web service
date: 2018-07-13 09:59:00
tags:
- excel
- vba
- web service
---
1.VBA編輯器→工具→設定引用項目  

[![](Image_20180713093944.png)](Image_20180713093944.png )

2.增加Microsoft Office Soap Type Library v3.0

(路徑:C:\Program Files (x86)\Common Files\microsoft shared\OFFICE14\MSSOAP30.DLL)

  

及Microsoft XML, v6.0

[![](Image_20180713094108.png)](Image_20180713094108.png )

3.以下代碼叫用即可

```
 Dim service As SoapClient30   
   
 Dim result As MSXML2.IXMLDOMSelection '回傳結果   
 Dim isOk As MSXML2.IXMLDOMElement '回傳結果屬性(執行結果OK/NG)   
 Dim message As MSXML2.IXMLDOMElement '回傳結果屬性(返回訊息)   
 Dim value As MSXML2.IXMLDOMElement '回傳結果屬性(返回值)   
   
   
 Set service = New SoapClient30   
 Call service.MSSoapInit("WSDL的URL")   
      
 Set result = service.方法名稱("參數")   
 Set isOk = result.Item(0)   
 Set message = result.Item(1)   
 Set value = result.Item(2)
```

