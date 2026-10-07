---
title: 取消雙開DBEaver時無法鎖定工作區的警告訊息
date: 2026-10-07 10:52:08
tags:
- dbeaver
---

情境：  
開啟1個以上的DBEaver會顯示以下警告訊息，有點煩人。

```log
┌─────────────────────────────────────────────────────────────────────┐
│DBeaver - Can't lock workspace                                       │
├─────────────────────────────────────────────────────────────────────┤
│⚠️Can't lock workspace at                                            │
│  {你的工作區路徑}.                                                    │
│  It seems that you have another DBeaver instance running.           │
│  You may ignore it and work without lock but it is recommended      │
│  to shutdown previous instance otherwise you may corrupt            │
│  workspace data.                                                    │
├─────────────────────────────────────────────────────────────────────┤
│                                      中止(A)     重試(R)     略過(I)  │
└─────────────────────────────────────────────────────────────────────┘
```

解法：  
在啟動參數加上`-reuseWorkspace`即可正常雙開。
