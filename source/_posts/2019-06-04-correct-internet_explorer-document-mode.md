---
layout: post
title: 修正IE開啟EasyFlow GP的文件模式
date: 2019-06-04 08:29:00
tags:
- easyflow gp
---
【修正】   
 [EasyFlow目錄]\jboss-4.2.3.GA\server\default\deploy\NaNaWeb.war\WMS\Templates\Template.jsp   
   
 原設定

[![](Image+002.png)](Image+002.png )

  
  

修改為

[![](Image+001.png)](Image+001.png )

【作用】   
 舊設定是不管用哪版IE開啟都只用IE8模擬,   
 這樣會造成有些新版IE才有的Javascript method跟開發者工具的function無法使用。   
而新設定是告訴IE用本身版本瀏覽, 不需模擬成IE8,   
 (參考: [https://msdn.microsoft.com/en-us/library/ff955275(v=vs.85).aspx#)](https://www.blogger.com/# "https://www.blogger.com/#")   
 因為BPM可以在Chrome上執行, 所以用IE11跑反而不用被IE8綁手綁腳。

