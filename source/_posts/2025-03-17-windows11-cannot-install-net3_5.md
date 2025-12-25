---
layout: post
title: Windows 11無法安裝.NET Framework 3.5
date: 2025-03-17 13:58:00
tags:
- ".net framework 3.5"
- windows 11
---

1. 在Windows 功能勾選**.NET Framework 3.5 (包括.NET 2.0和3.0)**

2. 在安裝進度完成後卻顯示Windows 無法完成要求的變更(錯誤碼: 0x80240021)

[![](devenv_20250317_105141.png)](devenv_20250317_105141.png )

  
  

3. 先勾選**SMB 1.0/CIFS 檔案共用支援**>確定>安裝完成(可先不重開機)。

[![](OptionalFeatures_20250317_134110.png)](OptionalFeatures_20250317_134110.png )

  

4. 再勾選**.NET Framework 3.5 (包括.NET 2.0和3.0)**>確定>安裝完成(**要重開機**)。

[![](devenv_20250317_114254.png)](devenv_20250317_114254.png )

  

5. 即可安裝相依.NET Framework 3.5的軟體。

6. 再取消勾選**SMB 1.0/CIFS 檔案共用支援**即可。

參考來源：[NET Framework 3.5 在Windows 11 下無法安裝](https://vocus.cc/article/6698fec7fd89780001c7d821 "https://vocus.cc/article/6698fec7fd89780001c7d821")

