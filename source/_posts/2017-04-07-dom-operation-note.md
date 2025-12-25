---
layout: post
title: DOM操作注意事項
date: 2017-04-07 14:34:00
tags:
- javascript
---
前提是要減少relayout及repaint。  
  
1.不逐一改變node屬性,用className或是cssText一次設定。  
2.先設定node屬性,最後再一次插入childNode到DOM前。  
3.使用DocumentFragment。  
4.把要改變的node複製出來，設定好再取代舊的node。  
5.或用display：none屬性把node隱藏，設定好再顯示。  
6.如果要逐一改變屬性，則可快取屬性值，亦能提升效能。  
  
  
參考：[【翻译】浏览器渲染Rendering那些事：repaint、reflow/relayout、restyle](http://www.cnblogs.com/ihardcoder/p/3927709.html "http://www.cnblogs.com/ihardcoder/p/3927709.html")
