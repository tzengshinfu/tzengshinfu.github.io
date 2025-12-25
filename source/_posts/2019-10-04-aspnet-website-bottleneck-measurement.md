---
layout: post
title: ASP.NET網站瓶頸測量
date: 2019-10-04 09:59:00
tags:
- asp.net
- internet information server
- visual studio
---
1.測量對象主機需安裝[IIS Metabase 及 IIS 6 設定相容性]功能。  

[![](att2.png)](att2.png )

  
  
2.複製Visual Studio Profiler安裝檔到測量對象主機並安裝。  
(在Visual Studio安裝路徑\Team Tools\Performance Tools\Setups)  

[![](att3.png)](att3.png )

  
  
  
  
  
  
  
  
  
  

3.執行VSPerfASPNetCmd,依照指示執行之。  
(選項可參照:[https://docs.microsoft.com/zh-tw/visualstudio/profiling/vsperfaspnetcmd?view=vs-2015](https://docs.microsoft.com/zh-tw/visualstudio/profiling/vsperfaspnetcmd?view=vs-2015 "https://docs.microsoft.com/zh-tw/visualstudio/profiling/vsperfaspnetcmd?view=vs-2015"))  
※發現此動作會將該台IIS全部應用程式集區'停止',最好在另外的測試區IIS執行。

4.將產生的vspx檔用Visual Studio開啟即可看到分析結果。  

[![](Image_20191004095920.png)](Image_20191004095920.png )

\*2019/10/07更新  
發現Prefix更好用,可以即時監控每個連線的.Net函式及DB連線耗時。  
參考來源:[http://kevintsengtw.blogspot.com/2016/04/profile-aspnet-application-prefix.html](http://kevintsengtw.blogspot.com/2016/04/profile-aspnet-application-prefix.html "http://kevintsengtw.blogspot.com/2016/04/profile-aspnet-application-prefix.html")  
  
另外如果發現瓶頸都在DB,亦可使用SQL Server Profiler錄製耗時較多的SQL。  
1.一般>使用範本:TSQL\_Duration。  
2.事件選取範圍>資料行篩選>Duration大於等於x亳秒。

