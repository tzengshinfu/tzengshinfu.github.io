---
layout: post
title: IIS設定遷移至新主機
date: 2017-09-11 15:08:00
tags:
- internet information server
---
步驟:  
1\_在舊主機匯出IIS設定(站台及應用集區)  
輸入指令(要以[系統管理員]權限執行):  

```
%windir%\system32\inetsrv\appcmd list site /config /xml > d:\sites.xml  
%windir%\system32\inetsrv\appcmd list apppool /config /xml > d:\apppools.xml
```

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
2\_刪除新主機預設站台及應用集區  

[![](step2.png)](step2.png )

[![](step3.png)](step3.png )

  
  
3\_匯入IIS設定到新主機即完成  
輸入指令(要以[系統管理員]權限執行):  

```
%windir%\system32\inetsrv\appcmd add site /in < d:\sites.xml  
%windir%\system32\inetsrv\appcmd add apppool /in < d:\apppools.xml
```

  
  
例外處理:  
1\_匯入應用集區設定檔時發生錯誤如下圖  
[![](step5.png)](step5.png )  
  
  
  
  
  
2\_因為舊主機IIS版本是10.0，而新主機是前1版的8.5，查閱MSDN可發現10.0新增一節點名為[environmentVariables]  

[![](step4.png)](step4.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
所以將設定檔中所有8.5版本不支援的節點刪除，即可正常匯入。  

[![](step6.png)](step6.png )

  
  
  

