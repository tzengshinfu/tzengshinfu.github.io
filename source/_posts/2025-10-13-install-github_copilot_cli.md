---
layout: post
title: 安裝GitHub Copilot CLI
date: 2025-10-13 15:22:00
tags:
- github copilot cli
---

 1.在[命令提示字元]執行以下指令以安裝Node.js  
winget install OpenJS.NodeJS.LTS

2.在[命令提示字元]執行以下指令以安裝Git  
winget install --id Git.Git -e --source winget

3.在[命令提示字元]執行GitHub Copilot CLI  
npm install -g @github/copilot@latest

4.(選用)在[命令提示字元]執行  
setx COPILOT\_ALLOW\_ALL true  
(會直接信任GitHub Copilot CLI，允許任何工具執行並不提出確認要求，有**安全性**問題，所以需評估便利與安全性的取捨。)

5.(選用)可在%USERPROFILE%\.copilot\copilot-instructions.md預寫入系統層級的提示詞，如  
PowerShell執行檔位置、檔案處理需以UTF-8(無BOM)行之等。

6.在[命令提示字元]執行  
copilot  
(會要求登入)
