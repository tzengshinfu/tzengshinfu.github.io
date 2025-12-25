---
layout: post
title: 使用Apache Flink SQL+SQL Server CDC connector同步MSSQL資料表
date: 2023-04-27 14:12:00
tags:
- apache flink
- change data capture
- sql server
---
1.開啟來源SQL Server資料庫CDC(Change data capture)功能，

在SQL客戶端執行

```
EXEC sys.sp_cdc_enable_db
```

2.開啟來源資料表CDC功能，

在SQL客戶端執行

```
EXEC sys.sp_cdc_enable_table
```

@source\_schema = N'dbo',

@source\_name   = N'[來源資料表名稱]',

@role\_name     = N'db\_cdcadmin',

@supports\_net\_changes = 0

3.驗證設定是否正確，

在SQL客戶端執行

```
EXEC sys.sp_cdc_help_change_data_capture
```

4.複製

[flink-sql-connector-sqlserver-cdc-2.3.0.jar](http://flink-sql-connector-sqlserver-cdc-2.3.0.jar "http://flink-sql-connector-sqlserver-cdc-2.3.0.jar")(擷取來源SQL Server資料表CDC紀錄用)

flink-connector-jdbc-3.1-SNAPSHOT.jar(寫入目的SQL Server資料表用)

[mssql-jdbc-12.2.0.jre11.jar](https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/12.2.0.jre11/mssql-jdbc-12.2.0.jre11.jar "https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/12.2.0.jre11/mssql-jdbc-12.2.0.jre11.jar")(SQL Server JDBC驅動程式)

以上3個jar檔到Apache Flink主機的$FLINK\_HOME/lib目錄。

※TaskManager和JobManager都要放置。

※由於目前Maven Central Repository的flink-connector-jdbc-3.0還不支援SQL Server，

所以需先到官方GitHub下載[source code](https://github.com/apache/flink-connector-jdbc/releases/tag/v3.1.0-rc1 "https://github.com/apache/flink-connector-jdbc/releases/tag/v3.1.0-rc1")依照[說明](https://github.com/apache/flink-connector-jdbc/blob/main/README.md "https://github.com/apache/flink-connector-jdbc/blob/main/README.md")自行編譯。

5.開啟Flink SQL CLI，

在JobManager的shell執行

```
$FLINK_HOME/bin/sql-client.sh
```

6.建立來源資料表，

參照[Flink-CDC-connector官方文件](https://ververica.github.io/flink-cdc-connectors/master/content/connectors/sqlserver-cdc.html "https://ververica.github.io/flink-cdc-connectors/master/content/connectors/sqlserver-cdc.html")在Flink SQL CLI執行Flink SQL即可。

語法類似SQL，但欄位型態需參照文件最下面的**Data Type Mapping**進行修正。

7.驗證是否正常連接，

在Flink SQL CLI執行

```
SELECT * FROM [來源資料表];
```

8.建立目的資料表，

參照[Flink-JDBC-connector官方文件](https://github.com/apache/flink-connector-jdbc/blob/main/docs/content/docs/connectors/table/jdbc.md "https://github.com/apache/flink-connector-jdbc/blob/main/docs/content/docs/connectors/table/jdbc.md")在Flink SQL CLI執行Flink SQL即可。

9.驗證是否正常連接，

在Flink SQL CLI執行

```
SELECT * FROM [目的資料表];
```

10.建立同步作業，

在Flink SQL CLI執行

```
INSERT INTO [目的資料表] SELECT * FROM [來源資料表];
```

11.在Flink管理介面(http://[Flink主機位址]:8081/#/job/running)

可看到該同步作業執行中。

※在Flink SQL CLI會顯示新增作業的Job ID，比照Flink管理介面可看到該同步作業執行中。

12.針對[來源資料表]進行CRUD作業，[目的資料表]資料也會(近乎)即時同步。
