---
title: 置換Tiptop預設Shell
date: 2026-04-14 14:15:03
tags:
- tiptop
---

目前Tiptop的預設Shell是KSH，對於常用鍵(Backspace/Delete)支援相當不友善。

可以用指令改善支援狀況，分為2種情境：

1. 在Vtcp for TIPTOP  
   輸入`stty sane && set -o emacs && stty erase "^H" && bind "^I=complete" && bind "^?=delete-char-forward" && bind "^[B=backward-word" && bind "^[F=forward-word"`，  
   並在終端機選單`Setup[C]`>`Keyboard ...`>`Key maps ...`>`Ctrl_Key ...`新增對應按鍵組合  
   - *Ctl_Lft*輸入`<ESC>B`
   - *Ctl_Rgt*輸入`<ESC>F`
   [![](telnet32_20260415_095136.png)](telnet32_20260415_095136.png)

2. 在其他終端機  
   先輸入**bash**切換到BASH，  
   再輸入`stty sane && stty erase "^?"`。