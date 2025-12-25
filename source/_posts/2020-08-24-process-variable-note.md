---
layout: post
title: 設定流程變數注意事項
date: 2020-08-24 14:32:00
tags:
- easyflow gp
---
1.流程字串型態變數無法從表單Js程式設定為空字串,若設定會拋出異常(【''=空字串】被用在流程初始值)。  
2.如果在formCreate/formOpen/formSave/formClose事件已設定變數內容,在控制項事件設定變數內容則無效。  
3.如果未在formCreate/formOpen/formSave/formClose事件設定變數內容,則以控制項事件設定變數內容為主。  
4.最好在formSave事件判斷並設定變數內容,可以如下設定:

```
function formOpen() {
    //設定流程變數預設內容
}

function formSave(){  
    if (符合條件) {
      //設定符合條件的流程變數內容(覆蓋預設值)
    }  

    return true;
}
```

5.流程設計師-流程變數雖然有字串/整數/浮點數/布林值/日期/XML型態,  
建議只使用字串/整數/浮點數/布林值型態。  
  
字串內容以單引號或雙引號包覆皆可,  
整數不可包含小數點,相反地浮點數可接受整數(無小數點),  
布林值在比較時不寫true/false,而是1/0。

(需符合Jython語法)  

[![](Image+006.png)](Image+006.png )

