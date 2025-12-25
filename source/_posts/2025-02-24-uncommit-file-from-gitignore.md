---
layout: post
title: 已加入gitignore的檔案移出版控並保留本機檔案
date: 2025-02-24 11:51:00
tags:
- git
---

Windows

1.開啟命令列

2.修改目前路徑到該repo

3.執行chcp 65001

- 65001=UTF-8，避免路徑字串與命令列語系不同導致fatal: pathspec '檔案路徑' did not match any files的亂碼問題。

4.執行for /f "delims=" %f in ('git ls-files -i -c --exclude-from=.gitignore') do git rm --cached "%f"

- `for /f "delims=" %f`：使用 `delims=` 避免空格導致的分割問題，確保整個檔名被正確處理。
- `in ('git ls-files -i -c --exclude-from=.gitignore')`：執行 `git ls-files` 並將輸出逐行存入變數 `%f`。
- `git rm --cached "%f"`：用雙引號包住變數，確保帶空格的檔案名稱能被正確處理。

Linux

1.開啟命令列

2.修改目前路徑到該repo

3.執行git ls-files -i -c --exclude-from=.gitignore -z | xargs -0 git rm --cached

- `-z`：讓 `git ls-files` 以 NUL (`\0`) 分隔檔名，防止空格或特殊字符導致問題。
- `xargs -0`：讓 `xargs` 以 NUL 分隔來處理檔名，確保帶空格的檔案能被正確傳遞給 `git rm --cached`。

參考來源：ChatGPT
