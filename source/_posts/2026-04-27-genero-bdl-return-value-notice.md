---
title: Genero BDL函式回傳注意事項
date: 2026-04-27 11:09:44
tags:
- tiptop
---

## 問題

函式最後傳回一個拼接的字串如下:

```bdl
    ......
    RETURN p_field CLIPPED, "=", l_result CLIPPED, "; export ", p_field CLIPPED
END FUNCTION
```

執行時發生錯誤如下:  
[![](2.png)](2.png)

此錯誤代碼意為`函式回傳值的數量與預期不符`。
[![](3.png)](3.png)

另一個函式則會在編譯時發生錯誤如下，也是相同意思:

```bash
../42m/xxx.4gl:117:1:121:12:error:(-6611) Function 'concat_string': unexpected number of returned values.
The compilation was not successful.  Errors found: 1.
```

## 解法

1. 在函式先宣告STRING型態變數。

    ```bdl
    FUNCTION concat_string()
        # 宣告要回傳的STRING型態變數
        DEFINE l_result STRING
        ......
    ```

2. 在最後回傳時先將結果寫入這個變數即可。

   ```bdl
       ......
       # 拼接字串先寫入這個變數
       LET l_result = p_field CLIPPED, "=", l_result CLIPPED, "; export ", p_field CLIPPED
       # 回傳這個變數
       RETURN l_result
    END FUNCTION
   ```
