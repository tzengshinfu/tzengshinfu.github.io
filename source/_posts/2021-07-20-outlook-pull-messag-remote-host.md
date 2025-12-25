---
layout: post
title: Outlook從遠端主機拉信回本機
date: 2021-07-20 14:37:00
tags:
- vba
---在Module1新增

```
Sub MoveItemsFromRemoteToLocal()
    On Error Resume Next
    
    Set myNameSpace = Application.GetNamespace("MAPI")
    Set myLocalInbox = myNameSpace.Stores.Item("本機信箱顯示名稱").GetDefaultFolder(olFolderInbox)
    Set myRemoteInbox = myNameSpace.Stores.Item("遠端主機信箱顯示名稱").GetDefaultFolder(olFolderInbox)  
    Set myRemoteItems = myRemoteInbox.Items

    For Each myRemoteItem In myRemoteItems
        DoEvents
        myRemoteItem.Move myLocalInbox '拉信回本機
    Next

    Set myRules = myRemoteInbox.Store.GetRules()

    For Each myRule In myRules
        myRule.Execute False, myLocalInbox, False, 2 '背景執行規則
    Next
End Sub
```

再執行此副函式即可。
