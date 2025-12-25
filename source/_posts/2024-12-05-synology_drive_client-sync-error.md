---
layout: post
title: Synology Drive Client同步Git資料夾失敗
date: 2024-12-05 09:03:00
tags:
- git
- synology drive client
---

問題：Synology Drive Client同步時間過長，發現Git資料夾下的子資料夾(.git/objects) 同步異常。

[![](image_20241205_082724.png)](image_20241205_082724.png )

  

解法：將.git/objects資料夾的唯讀屬性取消即可。

[![](image_20241205_082411.png)](image_20241205_082411.png )

  

參考來源：[Drive client gets stuck with .git directory](https://community.synology.com/enu/forum/1/post/142847 "https://community.synology.com/enu/forum/1/post/142847")

