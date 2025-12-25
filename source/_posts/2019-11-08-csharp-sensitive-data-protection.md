---
layout: post
title: C#機敏資訊放到C++ Dll以避免被直接反組譯
date: 2019-11-08 16:14:00
tags:
- c#
---
說明:  
.Net Framework因為其特性,  
編譯的執行檔或Dll有很多工具能反組譯,  
機敏資訊如連線字串等如果直接寫在程式碼中  
容易被取得造成資安問題。  
但像C++/Delphi等語言(非託管)是直接編譯成機器碼,  
反組譯難度較高,  
所以如果將機敏資訊放在非託管Dll中,  
反組譯工具就看不出內容而能提升安全性。  
  
做法:  
1)Visual Studio開啟專案→Visual C++→Win32主控台應用程式→應用程式類型:DLL  
  
2)在cpp原始檔加上以下敘述,然後編譯成Dll

```
#include "stdafx.h"
#include "COMDEF.H"

extern "C" __declspec(dllexport) BSTR getConnectionString(BSTR hash) {
    if (wcscmp(hash, L"＜驗證字串＞") == 0) {
        return ::SysAllocString(L"＜連線字串＞");     
    }
    else {
        return ::SysAllocString(L"error!");
    }
}
```

3)引用的C#專案加上以下敘述

```
using System;
using System.Runtime.InteropServices;

namespace 專案名稱 {
    class Program {

        [DllImport(@"＜Dll完整路徑＞", CallingConvention = CallingConvention.Cdecl)]
        [return: MarshalAs(UnmanagedType.BStr)]
        private static extern string getConnectionString([MarshalAs(UnmanagedType.BStr)]string hash);
        [DllImport(@"＜Dll完整路徑＞", CallingConvention = CallingConvention.Cdecl)]
        [return: MarshalAs(UnmanagedType.BStr)]
        private static extern string getConnectionString([MarshalAs(UnmanagedType.BStr)]string hash);
        [return: MarshalAs(UnmanagedType.BStr)]
        private static extern string getConnectionString([MarshalAs(UnmanagedType.BStr)]string hash);

        static void Main(string[] args) {
            var connStr = getConnectionString("＜驗證字串＞");
        }
    }
}
```

```
※該Dll的屬性→建置動作必須是"內容",不能以ILMerge等套件編譯成同一個執行檔,
不然會找不到。
```

4)用反組譯工具來查看,看不到Dll存放的連線字串。
但是最新的反組譯工具如dnSpy還是能執行以取得字串,
要再提升安全性可能要使用其他工具將.Net程式編譯成機器碼。

[![](Image_20191108155612.png)](Image_20191108155612.png )

