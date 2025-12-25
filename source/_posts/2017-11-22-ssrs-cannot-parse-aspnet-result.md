---
layout: post
title: SSRS無法解析ASP.NET Web Service回傳結果
date: 2017-11-22 11:19:00
tags:
- asp.net
- ssrs
- web service
---
場景:  
1\_使用ASP.NET建立Web Service，回傳結果格式為DataSet。  

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
2\_欲使用SSRS將回傳結果當成Data Source以利重用，卻發現結果不是我們要的。  

[![](step2.png)](step2.png )

  
  
  
  
  
  
  
  
  
  
3\_建立自訂類別取代DataSet如下，將屬性為基本類型並設為公開：  

[![](step3.png)](step3.png )

  
  
  
  
  
  
  
  
  
  
  
4\_SSRS可正確解析。  

[![](step4.png)](step4.png )

  

