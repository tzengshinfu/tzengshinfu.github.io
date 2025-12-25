---
layout: post
title: 取得測試專案路徑
date: 2025-06-12 14:01:00
tags:
- ".net framework"
- c#
---

場景：

被測試專案組件有以下敘述：

```
Path.Combine(Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) ??
    throw new NullReferenceException(), fileName)
```

專案本身啟動能正常執行，但因為測試專案無法取得被測試專案的Assembly.GetEntryAssembly().Location(組件路徑，通常是被測試專案的bin目錄)而拋出NullReferenceException。

解法：

改寫為以下敘述取得測試專案路徑即可正常測試。

```
Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), fileName)
```
