---
layout: post
title: 如何除錯時在空區塊或方法最後1個陳述式設定中斷點不被跳過
date: 2023-06-21 13:25:00
tags:
- java
---
在空區塊內或方法最後1個陳述式之後，新增陳述式"".isBlank();並在其設定中斷點(作用類似JavaScript的debugger)，如下：

```
public void test() {
    List variables = new ArrayList<>(List.of("A", "B", "C"));

    for (String variable: variables) {
      // 這是一個空區塊
      "".isBlank(); // 在這裡設定IDE中斷點，以查看變數variable的內容
    }

    // 這是方法最後1個陳述式
    String variable2 = "D";
    "".isBlank(); // 在這裡設定IDE中斷點，以查看變數variable2的內容
}
```

參考來源：[python - Java do nothing - Stack Overflow](https://stackoverflow.com/a/60399943 "https://stackoverflow.com/a/60399943")
