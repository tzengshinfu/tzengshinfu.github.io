---
layout: post
title: VS2022開啓.NETFramework4.0的專案
date: 2024-12-30 23:31:00
tags:
- ".net framework"
- visual studio
---

問題：

 1.VS2022開啓.NETFramework4.0的專案，出現以下錯誤。

[![](p1.png)](p1.png )

2.因爲VS2022已不支援.NETFramework4.0。

[![](p2.png)](p2.png )

  

3.就算手動安裝.NETFramework4.0會顯示以下提示而安裝失敗。

[![](p3.png)](p3.png )

解法：

1.在nuget.org搜尋"Microsoft.NETFramework.ReferenceAssemblies.net40"

點擊Microsoft官方的package。

[![](p4.png)](p4.png )

  

2.點擊[Download package](https://www.nuget.org/api/v2/package/Microsoft.NETFramework.ReferenceAssemblies.net40/1.0.3 "https://www.nuget.org/api/v2/package/Microsoft.NETFramework.ReferenceAssemblies.net40/1.0.3")下載這個package。

[![](p5.png)](p5.png )

  

3.用解壓縮軟體開啟這個package。

[![](page6.png)](page6.png )

  

4.將這個package根目錄下的build\.NETFramework\v4.0內容解壓縮並覆蓋

%ProgramFiles(x86)%\Reference Assemblies\Microsoft\Framework\.NETFramework\v4.0

5.重啟VS2022再開啟專案即可。

  

