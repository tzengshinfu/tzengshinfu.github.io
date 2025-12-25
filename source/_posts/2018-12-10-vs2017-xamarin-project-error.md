---
layout: post
title: Visual Studio 2017新增Xamarin專案異常
date: 2018-12-10 08:57:00
tags:
- visual studio
- xamarin
- 踩坑
---
參照此[連結](https://forums.xamarin.com/discussion/90309/the-resolvelibraryprojectimports-task-failed-unexpectedly "https://forums.xamarin.com/discussion/90309/the-resolvelibraryprojectimports-task-failed-unexpectedly")的解決方案, 都無效。  
但將所有相關元件都更新完成後, 就已無異常。  
  
新增專案(Cross-platform→行動應用程式→.NET standard)會顯示以下錯誤訊息。  

[![](pro1.png)](pro1.png )

  
  
  
  
  
  
  
  
  
  
  
  
1.更新Android專案的NuGet套件, Xamarin相關都要更新。  

[![](pro5.png)](pro5.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
2.Android→Android SDK管理員, 更新Android SDK。  
(先確認好要安裝到哪些版本的Android, 下載對應的SDK。)  

[![](pro4.png)](pro4.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

