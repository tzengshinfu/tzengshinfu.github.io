---
layout: post
title: 將資料庫檔案附加到另一台主機無法以原帳號登入
date: 2017-04-10 12:52:00
tags:
- sql
---
因為該帳號存在於[資料庫].[DB\_Name].[Security].[Users]  
但不存在於[資料庫].[Security].[Users]  
(或兩者設定不同)  
  
使用以下預存程式建立或同步設定  

```
EXEC sp_change_users_login 'Auto_Fix', '<有問題的帳號>', NULL, '<密碼>';
```

  
  
參考:[MS-SQL 資料庫還原到另一台主機無法登入](http://blog.xuite.net/tolarku/blog/39283410-MS-SQL+%E8%B3%87%E6%96%99%E5%BA%AB%E9%82%84%E5%8E%9F%E5%88%B0%E5%8F%A6%E4%B8%80%E5%8F%B0%E4%B8%BB%E6%A9%9F%E7%84%A1%E6%B3%95%E7%99%BB%E5%85%A5 "http://blog.xuite.net/tolarku/blog/39283410-MS-SQL+%E8%B3%87%E6%96%99%E5%BA%AB%E9%82%84%E5%8E%9F%E5%88%B0%E5%8F%A6%E4%B8%80%E5%8F%B0%E4%B8%BB%E6%A9%9F%E7%84%A1%E6%B3%95%E7%99%BB%E5%85%A5")
