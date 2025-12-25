---
layout: post
title: iis express允許外部連線
date: 2019-04-17 10:21:00
tags:
- internet information server
---

1.IIS Express工作列圖示->右鍵->顯示所有應用程式

[![](image_20241230_105822.png)](image_20241230_105822.png )

  

2.修改applicationhost.config，位置如下圖，依序點擊即可。

[![](image_20241230_110520.png)](image_20241230_110520.png )

  

3.編輯sites區段，新增

  

[![](image_20241230_110749.png)](image_20241230_110749.png )

  

