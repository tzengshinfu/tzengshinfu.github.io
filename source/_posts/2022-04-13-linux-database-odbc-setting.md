---
layout: post
title: Linux 各資料庫 ODBC 設定
date: 2022-04-13 11:35:00
tags:
- linux
- odbc
---

1.安裝UnixODBC(ODBC驅動程式管理員)(請參照網路教程)

2.安裝各資料庫的ODBC驅動程式(請參照網路教程)

3.把~/.odbc.ini(使用者ODBC)內容清空，統一修改/etc/odbc.ini(全域ODBC)(視狀況)

編輯odbc.ini如下：

```
    #region MySQL
    [<資料庫別名>]
    Description=<資料庫敘述>
    Driver=<驅動程式名稱，需與odbcinst.ini設定相同>
    SERVER=<資料庫位址>
    DATABASE=<資料庫名稱>
    PORT=<資料庫埠號，通常是3306>
    #endregion
    
    #region MSSQL
    [<資料庫別名>]
    Description=<資料庫敘述>
    Driver=<驅動程式名稱，需與odbcinst.ini設定相同>
    Server=tcp:<資料庫位址>,<資料庫埠號，通常是1433>
    Database=<資料庫名稱>
    #endregion
    
    #region Oracle
    [<資料庫別名>]
    Application Attributes = T
    Attributes = W
    BatchAutocommitMode = IfAllSuccessful
    BindAsFLOAT = F
    CloseCursor = F
    DisableDPM = F
    DisableMTS = T
    Driver = <驅動程式名稱，需與odbcinst.ini設定相同>
    DSN =
    EXECSchemaOpt =
    EXECSyntax = T
    Failover = T
    FailoverDelay = 10
    FailoverRetryCount = 10
    FetchBufferSize = 64000
    ForceWCHAR = F
    Lobs = T
    Longs = T
    MaxLargeData = 0
    MetadataIdDefault = F
    QueryTimeout = T
    ResultSets = T
    ServerName = <資料庫位址>:<資料庫埠號，通常是1521>/<資料庫名稱>
    SQLGetData extensions = F
    Translation DLL =
    Translation Option = 0
    DisableRULEHint = T
    StatementCache=F
    CacheBufferSize=20
    UseOCIDescribeAny=F
    SQLTranslateErrors=F
    MaxTokenSize=8192
    AggregateSQLType=FLOAT
    #endregion
```

4.另外Oracle資料庫需在/etc/environment設定系統變數內容，  
PATH(將Instant Client路徑附加到最後，以冒號分隔)  
LD\_LIBRARY\_PATH(即Instant Client路徑)  
NLS\_LANG(與Oracle資料庫相同，可用此SQL語法查詢：

```
SELECT * FROM V$NLS_PARAMETERS WHERE PARAMETER IN ('NLS_LANGUAGE', 'NLS_TERRITORY', 'NLS_CHARACTERSET')
```

)  
※不需TNS\_ADMIN

5.MSSQL如遇到SSL連線問題，
可編輯/etc/ssl/openssl.cnf降低TLS版本暫時繞過  
(參考來源：[[Microsoft][ODBC Driver 17 for SQL Server]SSL Provider: [error:1425F102:SSL routines:ssl\_choose\_client\_version:unsupported protocol]
#1112](https://github.com/microsoft/msphpsql/issues/1112#issuecomment-643522139 "https://github.com/microsoft/msphpsql/issues/1112#issuecomment-643522139"))

```
    #region 因SQL SERVER TLS版本較低，故先降低TLS版本
    openssl_conf = default_conf
    
    [default_conf]
    ssl_conf = ssl_sect
    
    [ssl_sect]
    system_default = system_default_sect
    
    [system_default_sect]
    MinProtocol = TLSv1
    CipherString = DEFAULT@SECLEVEL=1
    #endregion
```
