---
layout: post
title: Modified JavaScript value在Transformation的第1個Step無任何輸出
date: 2022-12-27 14:26:00
tags:
- kettle
---

 狀況：

Transformation內含2個Step，第1個Step產生SSH指令供第2個Stepg執行

(Step1)[Modified JavaScript value]→(Step2)[Run SSH commands]

[![](image-small.png)](image.png )

但並未產生任何可供SSH執行的指令。

(視窗下方Execution Results區域→Preview data頁籤→Fields欄位無任何內容)

修正：

在[Modified JavaScript value]前面加一個空的[Get variables]即可。

(Step1)[Get variables]→(Step2)[Modified JavaScript value]→(Step3)[Run SSH commands]

[![](image2-small.png)](image2.png )

