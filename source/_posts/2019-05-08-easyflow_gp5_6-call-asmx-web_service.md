---
layout: post
title: Invoke關卡呼叫.Net web service(asmx)
date: 2019-05-08 11:15:00
tags:
- easyflow gp
- web service
---
1-1.web service網站的web.config需新增HttpPost protocol  

[![](2.png)](2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
1-2.在asmx.cs的開頭  
將[WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1\_1)]  
改成[WebServiceBinding(ConformsTo = WsiProfiles.None)]  

[![](att0.png)](att0.png )

  
  
  
  
  
  
  
  
1-3.在method開頭新增  
[SoapRpcMethod(Use = System.Web.Services.Description.SoapBindingUse.Literal)]  

[![](att2.png)](att2.png )

  
  
  
  
  
  
注意:1-2跟1-3都要設定,不然會有參數值為null的問題;  
另外method只支援string型態的參數跟回傳結果  
1)如果參數其中之一不是string型態,則無法進入method(找不到method)  
2)如果回傳結果不是string型態,則無法回傳結果  

[![](Image_20190923155508.png)](Image_20190923155508.png )

  
  
  
  
  
  
2.Invoke關卡選擇web service  
[![](1.png)](1.png )  
  
  
3.選擇HttpPost  

[![](att9.png)](att9.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
4.再設定參數對應的流程變數即可。  

[![](att10.png)](att10.png )

  
  

