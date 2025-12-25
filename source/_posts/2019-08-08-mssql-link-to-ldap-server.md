---
layout: post
title: MSSQL Server新增連結伺服器以取得網域資訊
date: 2019-08-08 17:00:00
tags:
- sql server
---
1.連結的伺服器屬性  

[![](att1.png)](att1.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
[![](att2.png)](att2.png )  
  
[![](att3.png)](att3.png )  
  
  
2.如果不能查詢,再進行以下步驟

```
/**預設SQL Server不允許OpenQuery,所以要先啟用系統預儲程式進階選項*/
sp_configure 'show advanced options', 1   
reconfigure with override   

/**再啟用特定分散式查詢選項*/
sp_configure 'Ad Hoc Distributed Queries', 1   
reconfigure
```

