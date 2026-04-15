---
title: LOCKING_CURSOR鎖定及解除時機
date: 2026-03-24 10:55:00
tags:
- tiptop
---

```4gl
# 主程式
MAIN
    LET g_sql = "SELECT * FROM XXX_FILE WHERE XXX01 = 'OOO' FOR UPDATE NOWAIT"

    DECLARE l_cursor CURSOR FROM g_sql # 宣告LOCKING CURSOR

    BEGIN WORK

    OPEN l_cursor  # 鎖定開始(範圍:該筆紀錄)

    CLOSE l_cursor # 鎖定不會解除(其實在COMMIT/ROLLBACK WORK會自動關閉, 所以可以不用寫這行)

    FREE l_cursor  # 鎖定不會解除(其實在COMMIT/ROLLBACK WORK會自動關閉, 所以可以不用寫這行)

    COMMIT WORK     # 鎖定會解除

    ROLLBACK WORK   # 鎖定會解除

END MAIN            # 鎖定會解除
```
