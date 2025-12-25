---
layout: post
title: JavaScript 非同步方法鏈式呼叫
date: 2022-03-11 10:05:00
tags:
- javascript
---
原本是巢式呼叫

```
let asyncCalculator = new AsyncCalculator(0);



let asyncCalculateResult =



(



await (



await (



await (



await asyncCalculator.plusAsync(1)



).minusAsync(2)



).multiplyAsync(3)



).divideAsync(4)



).calculateResult
```

改寫成鏈式呼叫，一目瞭然

```
let asyncCalculator = new AsyncCalculator(0);



let asyncCalculateResult = await asyncCalculator.plusAsync(1)



.then(c => c.minusAsync(2))



.then(c => c.multiplyAsync(3))



.then(c => c.divideAsync(4))



.then(c => c.calculateResult)
```

參考來源：[https://es.discourse.group/t/await-postfix-operator/1244/4](https://es.discourse.group/t/await-postfix-operator/1244/4 "https://es.discourse.group/t/await-postfix-operator/1244/4")

(分享此用法的該名網友是位JS大師，真的學到了。)
