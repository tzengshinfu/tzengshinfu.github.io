---
layout: post
title: web deploy第1次都會失敗
date: 2019-03-28 17:38:00
tags:
- visual studio
- 踩坑
---

在部署時都會顯示失敗

[![](Image_20190328133916.png)](Image_20190328133916.png )

但第2次又正常

[![](Image_20190328133929.png)](Image_20190328133929.png )

原因為Microsoft.Net.Compilers,移除即可。

[![](Image_20190328134241.png)](Image_20190328134241.png )

參考來源:[https://stackoverflow.com/a/48583412](https://stackoverflow.com/a/48583412 "https://stackoverflow.com/a/48583412")

