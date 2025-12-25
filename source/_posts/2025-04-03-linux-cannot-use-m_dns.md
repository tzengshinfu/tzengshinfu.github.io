---
layout: post
title: Linux無法用.local域名連線
date: 2025-04-03 22:35:00
tags:
- linux
---

啟動AVAHI服務即可

```
systemctl start avahi-daemon
```

再將AVAHI服務設定為開機啟用

```
systemctl enable avahi-daemon
```
