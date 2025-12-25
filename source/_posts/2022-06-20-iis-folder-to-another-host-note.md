---
layout: post
title: IIS資料夾搬移至其他主機注意事項
date: 2022-06-20 09:35:00
tags:
- internet information server
---

1.資料夾內容搬移至另一台檔案主機。

2.原本資料夾刪除，使用MKLINK指令建立連結如下：

```
MKLINK /D "原本資料夾名稱" "另一台檔案主機路徑"
```

3.IIS→原本資料夾(現在是MKLINK捷徑)→驗證→匿名驗證→編輯...

啟用[特定使用者]，輸入有權限存取另一台檔案主機的帳號。

[![](Image_20220620092639.png)](Image_20220620092639.png )

  

4.如果其他AP主機有存取此資料夾的需求，需在該AP主機執行：

```
fsutil behavior set SymlinkEvaluation R2R:1
```

