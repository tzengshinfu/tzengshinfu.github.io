---
layout: post
title: EasyFlow GP 5.6使用jQuery插件
date: 2018-11-15 11:16:00
tags:
- easyflow gp
- jquery
---
在EFGP的架構下有些地方要注意:  
   
 發現只要引用其他來源的jQuery,   
 如document.write(''); 雖然起單時無任何問題, 但在第2關會有派送履歷無法顯示的異常。  
 [![](error1.png)](https://www.blogger.com/# "https://www.blogger.com/#")

而且就算想用jQuery的noConflict()方法也不可行, 因為:   
 1.jQuery物件在EFGP被改名, 根本找不到。   
 [![](problem2.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 2.$別名在EFGP已有別的用途。   
 [![](problem1.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
   
 解決方案:   
 查看EFGP的source code, 其本身也有jQuery library, 別名為【\_\_jQuery】,   
 所以只要撰寫當var textBox1 = $(“#TextBox1”);時  
 改為var textBox1 = \_\_jQuery(“#TextBox1”);即可正常使用。   
   
 而jQuery插件也要配合修改(以[jQuery Soap](https://www.blogger.com/# "https://www.blogger.com/#")為例),   
 [![](before.png)](https://www.blogger.com/# "https://www.blogger.com/#")

jQuery改為\_\_jQuery即可。   
 [![](after.png)](https://www.blogger.com/# "https://www.blogger.com/#")

