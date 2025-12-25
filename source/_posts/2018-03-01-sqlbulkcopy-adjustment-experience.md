---
layout: post
title: SqlBulkCopy調整心得
date: 2018-03-01 13:21:00
tags:
- ".net framework"
- sql
---
場景：  
從MySQL同步數個Table到MSSQL，採取先清空(Truncate Table)再寫入的策略；  
因為某些Table筆數較多(約百萬筆)，所以使用SqlBulkCopy類進行大量批次寫入。  
  
做法：  
1\_取得各Table的筆數,設定SqlBulkCopy.BatchSize屬性=該Table筆數。  
  
2\_SqlBulkCopy.BulkCopyTimeout(逾時)設為0。  
  
3\_設定SqlBulkCopyOptions.TableLock,可以更快完成,但寫入期間會造成Table被鎖定。  
→個人測試加入此選項反而增加30秒的寫入時間。
