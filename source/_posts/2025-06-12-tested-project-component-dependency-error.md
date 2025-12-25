---
layout: post
title: 測試專案顯示組件相依性問題
date: 2025-06-12 13:23:00
tags:
- ".net framework"
---

被測試專案組件如下

Serilog, Version=4.3.0.0

Serilog.Sinks.Async, Version=2.1.0.0

專案本身啟動能正常執行，

因為被測試專案csproj檔本身已有AutoGenerateBindingRedirects屬性，且內容為true；

但在引用該專案進行單元測試時，會拋出例外，FusionLog內容如下：

```
=== 繫結前狀態資訊 ===



...



正在呼叫組件 : Serilog.Sinks.Async, Version=2.1.0.0, Culture=neutral, PublicKeyToken=24c2f752a8e58a10。



===



...



記錄: 原則後參考: Serilog, Version=4.1.0.0, Culture=neutral,
    PublicKeyToken=24c2f752a8e58a10



...



警告: 比較組件名稱發現不符項目: 次要版本



錯誤: 無法完成組件的安裝 (hr = 0x80131040)。已終止探查。
```

此時要在測試專案csproj檔的**目前啟動的**組態屬性群組新增GenerateBindingRedirectsOutputType屬性，且內容為true：

```
<?xml version="1.0" encoding="utf-8"?>  
<Project ToolsVersion="15.0"
    xmlns="http://schemas.microsoft.com/developer/msbuild/2003">  
    <Import
    Project="$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props"
    Condition="Exists('$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props')" />  
 
      <PropertyGroup>  
        ...
        <!--↓↓↓在此插入↓↓↓-->
        <GenerateBindingRedirectsOutputType>true</GenerateBindingRedirectsOutputType>
      </PropertyGroup>
```

並重載測試專案即可正常測試。
