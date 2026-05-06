---
title: C#以腳本模式運行並透過Dapper存取Oracle
date: 2026-05-06 15:54:51
tags:
- c#
- dapper
- oracle
---

## 腳本內容如下

本例檔名為`app.css`

```csharp
// Dapper不支援AOT
#:property PublishAot=false

#:package Oracle.ManagedDataAccess.Core@23.26.200
#:package Dapper@2.1.72
// Dapper擴充功能: Insert/Update/etc.
#:package DapperExtensions@1.7.0

using Dapper;
using DapperExtensions;
using DapperExtensions.Mapper;
using DapperExtensions.Sql;
using Oracle.ManagedDataAccess.Client;

// 設定DapperExtensions使用Oracle方言
DapperExtensions.DapperExtensions.SqlDialect = new OracleDialect();

using var connection = new OracleConnection("User Id={資料庫使用者帳號};Password={資料庫使用者密碼};Data Source={資料庫主機名稱或IP}:{資料庫主機Port}/{資料庫服務名稱};");

connection.Open();

var xxx_files = connection.Query<XxxFile>("SELECT XXX01, XXX02, XXX03, XXX04 FROM XXX_FILE WHERE XXX01 = :XXX01", new { XXX01 = "xxx" }).ToList();

foreach (var xxx_file in xxx_files)
{
    xxx_file.Xxx04 = DateTime.Today; // 僅日期不帶時間: 2024-06-17 00:00:00

    try
    {
        connection.Update(xxx_file);
    }
    catch (Exception ex)
    {
        // 捕獲異常並獲取最後執行的SQL語句
        var sql = DapperExtensions.DapperExtensions.LastExecutedCommand();

        throw;
    }
}

// Oracle表格
public class XxxFile
{
    public string Xxx01 { get; set; }
    public string Xxx02 { get; set; }
    public string Xxx03 { get; set; }
    public DateTime Xxx04 { get; set; }
}

// Oracle表格映射規則
public class XxxFileMapper : ClassMapper<XxxFile>
{
    public XxxFileMapper()
    {
        Table("XXX_FILE");

        // 設定複合主鍵XXX01+XXX02+XXX03
        Map(m => m.Xxx01).Column("XXX01").Key(KeyType.Assigned);
        Map(m => m.Xxx02).Column("XXX02").Key(KeyType.Assigned);
        Map(m => m.Xxx03).Column("XXX03").Key(KeyType.Assigned);
        Map(m => m.Xxx04).Column("XXX04");
    }
}
```

## 執行方法

執行dotnet run `app.cs`即可。
