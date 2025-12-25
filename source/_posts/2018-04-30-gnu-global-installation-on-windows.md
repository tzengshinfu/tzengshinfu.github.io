---
layout: post
title: GNU GLOBAL安裝/使用(for Windows)
date: 2018-04-30 13:32:00
tags:
- gnu global
- windows
---

1. 下載GNU GLOBAL，解壓縮到C:\GLOBAL。
2. 下載Python 3並安裝。
3. 我的電腦→右鍵→內容→進階系統設定→環境變數→系統變數→Path→新增C:\GLOBAL\bin。
4. 系統變數→新增變數名稱GTAGSCONF，變數值C:\GLOBAL\share\gtags\gtags.conf。
5. 系統變數→新增變數名稱GTAGSLABEL，變數值pygments。
6. 使用gtags --debug驗證安裝是否正常。
7. 使用gtags產生索引檔GTAGS,GRTAGS,GPATH
8. 使用htags產生索引網站，命令列參數：--alphabet --other --symbol --tree-view --frame --fixed-guide --line-number --verbose --warning

  
  
