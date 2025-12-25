---
layout: post
title: Outlook存檔時自動格式化圖片(加上邊框及超過規定大小則自動縮小)
date: 2020-07-17 16:56:00
tags:
- vba
---
在ThisOutlookSession新增  

[![](Image+016.png)](Image+016.png )

```
Public WithEvents outlookInspectors As Outlook.Inspectors
Public WithEvents outlookMailItem As Outlook.mailItem

Private Sub Application_Startup()
    Set outlookInspectors = Application.Inspectors
End Sub

Private Sub outlookInspectors_NewInspector(ByVal Inspector As Inspector)
    Set currentOutlookMailItem = Inspector.CurrentItem
    
    If TypeName(currentOutlookMailItem) = "MailItem" Then
        Set outlookMailItem = currentOutlookMailItem
    End If
End Sub

'發現outlookMailItem_Write事件並不會每次都觸發,所以改在BeforeCheckNames事件(檢查名稱前)
Private Sub outlookMailItem_BeforeCheckNames(Cancel As Boolean)
    On Error Resume Next
    
    If Not Application.ActiveInspector Is Nothing Then
        Set editor = Application.ActiveInspector.WordEditor
        
        For Each Picture In editor.InlineShapes
            '不處理簽名檔圖片(替代文字=簽名檔圖片匯入時的檔名)
            If Picture.AlternativeText <> "signature" Then
                If Picture.Width > 750 Then
                    Picture.Width = 750
                End If
                
                '樣式=實線(wdLineStyleSingle)
                '寬度=1pt(wdLineWidth100pt)
                With Picture.Borders
                    .OutsideLineStyle = 1
                    .OutsideLineWidth = 8
                    .OutsideColor = RGB(85, 142, 213)
                End With
            End If
        Next
    End If
End Sub
```

