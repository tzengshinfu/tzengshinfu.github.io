---
layout: post
title: Web Deploy成功後執行指令
date: 2018-05-22 14:57:00
tags:
- visual studio
---
1.卸載專案  
 [![](step1.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
  
   
 2.編輯專案組態檔  
 [![](step2.png)](https://www.blogger.com/# "https://www.blogger.com/#")

3.在最下面加上

```
<Target Name="{自訂Task名稱}" AfterTargets="MSDeployPublish" Condition="{在哪種組態下執行}">  
     <Exec Command="{自訂命令}" />  
   </Target>
```

[![](step4.png)](https://www.blogger.com/# "https://www.blogger.com/#")

