---
layout: post
title: 批次修改流程代理人啟用結束時間
date: 2018-12-28 12:41:00
tags:
- easyflow gp
---

```
UPDATE ProcessSubstituteDefinition
SET startSubstituteTime = '<開始代理 年年年年-月月-日日 時時:分分:秒秒.000>'
,endSubstituteTime = '<結束代理 年年年年-月月-日日 時時:分分:秒秒.000>'
,substituteOID = (SELECT OID FROM Users WHERE id = '<代理者工號>')
,objectVersion = objectVersion + 1
WHERE ownerOID = (SELECT OID FROM Users WHERE id = '<被代理者工號>');![](pro1.png)
```

