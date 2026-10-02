---
title: 在commit前偵測硬編碼的密鑰
date: 2026-10-02 16:55:43
tags:
- git
---

目的：
在git commit前利用hooks呼叫pre-commit(Python)並使用betterleaks(Golang)進行程式碼有無硬編碼的密鑰的檢測，如果發現則阻止git commit。

手順：

1. 安裝Python及Golang。
2. 安裝pre-commit。

   ```bash
   pip install pre-commit
   ```

3. 安裝beterleaks。

   ```bash
   go install github.com/betterleaks/betterleaks/v2@latest
   ```

4. 在要掃描專案根目錄新增空白檔案`.pre-commit-config.yaml`。
   內容為

   ```yaml
    repos:
    -   repo: local
        hooks:
        -   id: betterleaks-system
            name: 偵測硬編碼中
            entry: betterleaks --redact # 將密碼顯示為"REDACT"
            language: system
    ```

5. 安裝precommit hook。

   ```bash
   $ pre-commit install
   pre-commit installed at .git/hooks/pre-commit
   ```

6. commit時如果偵測到硬編碼的密鑰會顯示如以下錯誤訊息並中止commit。

   ```log
   ┌─github-pat──○
   │
   │ 1 │  ⟨binary⟩ string xxxToken = "REDACTED";
   │   │                           ^^^^^^^^
   │
   │   path ............ Program.cs
   │   confidence ...... HIGH
   │ attributes:
   │   resource ...... fs.content
   └○
   ```
