---
layout: post
title: 安裝OpenAI Codex CLI
date: 2025-09-12 18:31:00
tags:
- openai codex cli
---

1.在[命令提示字元]執行以下指令以安裝Node.js  
winget install OpenJS.NodeJS.LTS

2.在[命令提示字元]執行以下指令以安裝Git  
winget install --id Git.Git -e --source winget

3.在[命令提示字元]執行Codex CLI  
npm install -g @openai/codex@latest

4.(選用)在[命令提示字元]執行  
mkdir "%USERPROFILE%\.codex" 2>nul & (echo approval\_policy = "**never**" & echo sandbox\_mode = "**danger-full-access**" & echo web\_search\_request = **true**) > "%USERPROFILE%\.codex\config.toml"

(會直接信任codex，允許不提出任何提升權限要求，有**安全性**問題，所以需評估便利與安全性的取捨。)

5.在[命令提示字元]執行  
codex  
(會要求登入)
