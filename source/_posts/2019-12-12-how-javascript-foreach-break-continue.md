---
layout: post
title: Javascript forEach函數的break及continue方式
date: 2019-12-12 18:54:00
tags:
- javascript
---

```
//forEach模擬continue
const items = [1, 2, 3, 4, 5];
const no = 3;

items.forEach(function (item) {
    if (item == no) {
        return false;
    }

    console.log(item);
});

//some模擬break
const items = [1, 2, 3, 4, 5];
const no = 3;

items.some(function (item) {
    if (item == no) {
        return true;
    }

    console.log(item);
});
```

參考來源:[Javascript Array forEach()中无法return和break，代替方法some()与every()](https://blog.csdn.net/lihefei_coder/article/details/76736296 "https://blog.csdn.net/lihefei_coder/article/details/76736296")
