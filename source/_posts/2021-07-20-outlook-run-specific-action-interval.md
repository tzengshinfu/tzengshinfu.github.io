---
layout: post
title: Outlook每隔特定時間區間自動執行特定動作
date: 2021-07-20 14:34:00
tags:
- vba
---
在ThisOutlookSession新增

[![](Image_20210720141952.png)](Image_20210720141952.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

```
Private Sub Application_Quit()

    If TimerID <> 0 Then Call DeactivateTimer '關閉定時器

End Sub



Private Sub Application_Startup()    

    Call ActivateTimer(10) '設定定時器(10秒啟動1次)

End Sub
```

在Module1新增

```
Declare PtrSafe Function SetTimer Lib "user32" (ByVal hwnd As LongLong, ByVal nIDEvent As LongLong, ByVal uElapse As LongLong, ByVal lpTimerfunc As LongLong) As LongLong
Declare PtrSafe Function KillTimer Lib "user32" (ByVal hwnd As LongLong, ByVal nIDEvent As LongLong) As LongLong

Public TimerID As LongLong

Public Sub TriggerTimer(ByVal hwnd As Long, ByVal uMsg As Long, ByVal idevent As Long, ByVal Systime As Long)
  <要執行的特定動作>
End Sub


Public Sub DeactivateTimer()
  lSuccess = KillTimer(0, TimerID)
  
  If lSuccess = 0 Then
    MsgBox "定時器無法停止"
  Else
    TimerID = 0
  End If
End Sub

Public Sub ActivateTimer(ByVal nSeconds As Long)
  nSeconds = nSeconds * 1000
  
  If TimerID <> 0 Then Call DeactivateTimer
  
  TimerID = SetTimer(0, 0, nSeconds, AddressOf TriggerTimer)
  
  If TimerID = 0 Then
    MsgBox "定時器無法啟動"
  End If
End Sub
```

參考來源：[https://stackoverflow.com/a/30064953](https://stackoverflow.com/a/30064953 "https://stackoverflow.com/a/30064953")

