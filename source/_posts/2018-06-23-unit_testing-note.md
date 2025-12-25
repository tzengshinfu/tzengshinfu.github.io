---
layout: post
title: 單元測試需注意事項
date: 2018-06-23 16:37:00
tags:
- ".net framework"
- dapper
- entity framework
- testing
- visual studio
- 踩坑
---
  
 狀況:  
 當使用TransactionScope將之前寫入資料庫動作撤銷,  
 專案有使用到EntityFramework及Dapper會遇到以下錯誤;  
   
 (1)顯示"No Entity Framework provider found for the ADO.NET provider with invariant name ‘System.Data.SqlClient'"錯誤  
 解法:EntityFramework的DbContext需新加建構式如下:  
   

```
 public partial class xxxEntities {  
         public static xxxEntities Create() {  
             return new xxxEntities("name=xxxEntities");  
         }  
   
         private xxxEntities(string contextName) : base(contextName) {  
             var ensureDLLIsCopied = System.Data.Entity.SqlServer.SqlProviderServices.Instance;  
         }  
     }
```

  
   
 參考:  
 [1][https://stackoverflow.com/questions/15088426/overriding-code-generated-dbcontext-constructor/15088572#15088572](https://www.blogger.com/# "https://www.blogger.com/#")  
 [2][http://robsneuron.blogspot.com/2013/11/entity-framework-upgrade-to-6.html](https://www.blogger.com/# "https://www.blogger.com/#")   
   
 (2)Dapper使用SqlConnection  
 會顯示"已停用分散式交易管理員 (MSDTC) 的網路存取。請使用元件服務系統管理工具啟用 DTC，以使用 MSDTC 安全性設定中的網路存取"  
 解法:在連線字串增加enlist=False, 避免觸發MSTDC
