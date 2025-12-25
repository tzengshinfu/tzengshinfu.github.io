---
layout: post
title: OpenAI Codex CLI另一種編寫提示詞的方式
date: 2025-09-20 21:39:00
tags:
- codex cli
---

其實在終端機編寫提示詞並不太方便，

大量文字新增修改貼上及移動鼠標位置等操作還是在文字編輯器最方便，

因為Codex有支援自訂提示詞功能，

我們可以在$CODEX\_HOME/prompts/

(Windows是%USERPROFILE%/.codex/prompts

Linux/WSL 2是~/.codex/prompts/)

新增自訂提示詞檔案，副檔名必須是.md，如my-prompt.md

甚至可以直接用IDE編輯該提示詞檔案，

編輯時Visual Studio 2202可以使用右鍵選單[Copy Full  Path]複製檔案路徑；

Visual Studio Code則能用[Copy Path]或[Copy Relative Path]複製檔案路徑。

重啟Codex(codex resume session\_id)並在Codex CLI輸入/<自訂提示詞檔名>，如/my-prompt

就能將檔案內容作為提示詞送給Codex。

參考來源：[Custom Prompts](https://github.com/openai/codex/blob/main/docs/prompts.md "https://github.com/openai/codex/blob/main/docs/prompts.md")
