---
layout: post
title: EasyFlow取得附件實體路徑程式碼(C#/VB6=ReportingService用)
date: 2019-08-30 16:58:00
tags:
- easyflow gp
---

C#版

```
var physicalName = "42f5a298x16cddb6dd3ex6a19";
var extension = "jpg";
var docServerRootPath = "";
var mod = physicalName.Length % 2;
var locationTempString = physicalName.Substring(2, physicalName.Length - 4 + mod);

for (var currentIndex = locationTempString.Length - 1; currentIndex >= mod; currentIndex -= 2) {
    var folder = locationTempString.Substring(currentIndex - 1, 2);
    folders.Add(folder);
}

var directoryPath = string.Join(@"\", folders);
var physicalFilePath = docServerRootPath + @"\" + directoryPath + @"\" + physicalName + "." + extension;
```

VB6版

```
Dim physicalName As String
physicalName = "42f5a298x16cddb6dd3ex6a19"

Dim extension As String
extension = "jpg"

Dim docServerRootPath As String
docServerRootPath = "";

Dim folders() As String
ReDim Preserve folders(0)

Dim modNumber As Integer
modNumber = Len(physicalName) Mod 2

Dim locationTempString As String
locationTempString = Mid(physicalName, 3, Len(physicalName) - 4 + modNumber)

Dim currentIndex As Integer
Dim folderIndex As Integer
folderIndex = 0

For currentIndex = Len(locationTempString) - 1 To currentIndex > modNumber Step -2
    Dim folder As String
    folder = Mid(locationTempString, currentIndex, 2)

    folders(folderIndex) = folder
    folderIndex = folderIndex + 1

    ReDim Preserve folders(folderIndex)
Next

Dim directoryPath As String
directoryPath = Join(folders, "\")

Dim physicalFilePath As String
physicalFilePath = docServerRootPath + "\" + directoryPath + physicalName + "." + extension 'folder陣列在Join後最後會多一個\符號,所以directoryPath最後不用再加上\符號
```



```

```
