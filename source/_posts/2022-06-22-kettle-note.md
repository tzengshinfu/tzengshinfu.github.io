---
layout: post
title: Kettle注意事項
date: 2022-06-22 09:56:00
tags:
- kettle
---
1.Spoon編輯器的啟動script(Spoon.bat/spoon.sh)下面這行最後面要加上UTF-8("-Dfile.encoding=UTF-8")，不然當ETL排程工作名稱含有中文字將無法開啟。

```
if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms1024m" "-Xmx2048m" "-XX:MaxPermSize=256m" "-Dfile.encoding=UTF-8"
```

  
2.寫入資料庫發現如果文字型態欄位設非NULL時，當寫入空字串時，會被Kettle轉換成NULL而造成異常。

需在.kettle\kettle.properties 增加一行 KETTLE\_EMPTY\_STRING\_DIFFERS\_FROM\_NULL=Y
讓空字串保持原狀寫入。

※位置預設在~/.kettle/kettle.properties或在$KETTLE\_HOME/.kettle/kettle.properties

  
3.舊版(2008以前)MSSQL支援，需在lib目錄新增jtds-1.3.1.jar，Database Connection的Connection type需選MS SQL Server

載點 [https://sourceforge.net/projects/jtds/](https://sourceforge.net/projects/jtds/ "https://sourceforge.net/projects/jtds/")

  
4.如果MSSQL Server只支援舊版TLS，需在Database Connection的Options新增trustServerCertificate=true。
  
  
5.Kettle Carte Server支援SSL，修改pwd/carte-config-master-8080.xml

```
<slaveserver>  

    <name>master1</name>  

    <hostname>127.0.0.1</hostname>  

    <port>8080</port>  

    <hostname>(主機位址)</hostname>  

    <port>(主機Port)</port>  

    <username>(帳號)</username>  

    <password>(密碼)</password>  

    <master>Y</master>  

    <sslConfig>  

        <keyStore>(JKS憑證)</keyStore>  

        <keyStorePassword>(keyStorePassword)</keyStorePassword>  

        <keyPassword>(keyPassword)</keyPassword>  

    </sslConfig>  

</slaveserver>
```

  
6.停止紀錄Kettle log，修改classes/log4j2.xml，註解以下節點即可。

```
<!--
<RollingFile name="pdi-execution-appender" fileName="logs/pdi.log" filePattern="logs/pdi.%d{yyyy-MM-dd}.log">
    <PatternLayout>
        <Pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5p &lt;%t&gt; %m%n</Pattern>
    </PatternLayout>
    <Policies>
        <TimeBasedTriggeringPolicy />
    </Policies>
    <DefaultRolloverStrategy/>
</RollingFile>
-->
```

7.在/etc/profile.d新增一個<設定檔名>.sh檔用來設定Kettle相關系統變數

```
export LD_LIBRARY_PATH="" #Kettle連接Oracle客戶端
export NLS_LANG="" #Kettle連接Oracle資料庫字符集
export TNS_ADMIN="" #Oracle客戶端配置文件目錄(如果有的話)
export PENTAHO_JAVA_HOME="" #Kettle用Java JRE/JDK(目前Kettle需要Java 11)
export CLASSPATH="./:$PENTAHO_JAVA_HOME/lib:$LD_LIBRARY_PATH/orai18n.jar" #Kettle引用的JDBC Jar檔
export KETTLE_HOME="" #Kettle路徑
export PATH="$PATH:$LD_LIBRARY_PATH"
```

變更<設定檔名>.sh檔的權限並生效

```
$ chmod +x <設定檔名>.sh
$ source <設定檔名>.sh
```

8.啟動時提示缺少libwebkitgtk-1.0時，需自行安裝

```
sudo sh -c "echo 'deb http://cz.archive.ubuntu.com/ubuntu bionic main universe' >> /etc/apt/sources.list" && \
sudo apt update -y && apt install -y libwebkitgtk-1.0-0
```

參考來源：

【[Ubuntu環境變數設定位置](https://help.ubuntu.com/community/EnvironmentVariables "https://help.ubuntu.com/community/EnvironmentVariables")】

【[環境變數 - Oracle客戶端](https://docs.oracle.com/en/database/oracle/oracle-database/21/lacli/environment-variables-instant-client.html#GUID-BA8FB14E-1463-4F6A-9926-4F9F696E52D0 "https://docs.oracle.com/en/database/oracle/oracle-database/21/lacli/environment-variables-instant-client.html#GUID-BA8FB14E-1463-4F6A-9926-4F9F696E52D0")】

【[查看Oracle資料庫字符集](https://docs.oracle.com/cd/E12102_01/books/AnyInstAdm784/AnyInstAdmPreInstall18.html "https://docs.oracle.com/cd/E12102_01/books/AnyInstAdm784/AnyInstAdmPreInstall18.html")】

【[環境變數 - Kettle](https://help.hitachivantara.com/Documentation/Pentaho/5.4/0F0/0G0/020#da089c89-c26f-4443-8613-5ae9fd6e1360__set_environment_variables "https://help.hitachivantara.com/Documentation/Pentaho/5.4/0F0/0G0/020#da089c89-c26f-4443-8613-5ae9fd6e1360__set_environment_variables")】
