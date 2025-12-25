---
layout: post
title: Windows右鍵選單的新增(W)項目增加檔案類型
date: 2023-01-04 11:50:00
tags:
- windows
---

新增文字檔，內容如下

Windows Registry Editor Version 5.00

```
[HKEY_CLASSES_ROOT\.<副檔名>]
@="<檔案類型>"
```

```
[HKEY_CLASSES_ROOT\.<副檔名>\ShellNew]  
"NullFile"=""

[HKEY_CLASSES_ROOT\<檔案類型>]  
@="<右鍵新增(W)要顯示的檔案類型文字>"
```

```

```

```
修改副檔名為.reg並合併到登錄檔即可。
```

```
參考來源：Can't add new items to Windows 7 "new" context menu
```
