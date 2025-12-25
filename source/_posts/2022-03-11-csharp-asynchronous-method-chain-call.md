---
layout: post
title: C# 非同步方法鏈式呼叫
date: 2022-03-11 10:38:00
tags:
- c#
---
原本是巢式呼叫

```
var asyncCalculator= new AsyncCalculator(0);



var asyncCalculateResult =



(



await (



await (



await (



await asyncCalculator.PlusAsync(1)



).MinusAsync(2)



).MultiplyAsync(3)



).DivideAsync(4)



).CalculateResult;
```

改寫成鏈式呼叫，一目瞭然

```
var asyncCalculator= new AsyncCalculator(0);



var asyncCalculateResult = await asyncCalculator.PlusAsync(1)



.ContinueWith(t => t.GetAwaiter().GetResult().MinusAsync(2)).Unwrap()



.ContinueWith(t => t.GetAwaiter().GetResult().MultiplyAsync(3)).Unwrap()



.ContinueWith(t => t.GetAwaiter().GetResult().DivideAsync(4)).Unwrap()



.ContinueWith(t => t.GetAwaiter().GetResult().CalculateResult);



//因為t.Result的異常會被包裝在AggregateException異常裡，所以改成呼叫t.GetAwaiter().GetResult()方法。



//與JavaScript不同，會再多包一層Task回傳，所以要用Unwrap()方法剝掉。
```
