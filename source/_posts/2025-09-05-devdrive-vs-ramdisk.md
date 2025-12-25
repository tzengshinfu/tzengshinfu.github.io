---
layout: post
title: Dev Drive vs RamDisk
date: 2025-09-05 15:10:00
tags:
- dev drive
- ramdisk
---

純個人體感，RamDisk勝！

Windows form專案，在[Dev Drive](https://learn.microsoft.com/zh-tw/windows/dev-drive/ "https://learn.microsoft.com/zh-tw/windows/dev-drive/")編譯，未開啟Microsoft Defender，  
時不時會繞圈圈甚至卡死必須重啟Visual Studio；

用RamDisk([AIM Toolkit](https://sourceforge.net/projects/aim-toolkit/ "https://sourceforge.net/projects/aim-toolkit/")，新版ImDisk Toolkit)，編譯過程絲滑，  
單元測試也是亳無卡頓。

目前使用方法：

1.原始碼備份儲存在D:\Workspace。

2.開機時會複製至AIM Toolkit建立的R:\。

3.關機時會同步回D:\Workspace。

[![](RamDiskUI_20250911_084159.png)](RamDiskUI_20250911_084159.png )

  

4.為避免當機等意外造成進度消失，在開發過程須上傳到版控主機。  
5.亦可用同步軟體或腳本(如Robocopy)進行複製和偵測到檔案變更時回寫D:\Workspace。

網友AIM Toolkit使用心得：[AIM Toolkit(ImDisk Toolkitの後継)がリリースされたので使ってみた](https://otogeworks.com/blog/creation-ramdisk-using-aim-toolkit/ "https://otogeworks.com/blog/creation-ramdisk-using-aim-toolkit/")

