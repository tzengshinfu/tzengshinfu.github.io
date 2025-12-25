---
layout: post
title: 試用大模型ChatGLM2-6B、Google Colab
date: 2023-07-19 16:03:00
tags:
- google colab
- llm
---

1.在Google Colab執行

```
from google.colab import drive  
drive.mount('/content/drive')
```

2.詢問"要允許這個筆記本存取你的 Google 雲端硬碟檔案嗎？"，點選[連線至 Google 雲端硬碟]按鈕→選擇連線帳戶→點選[Allow]按鈕

[![](image_20230719_155725.png)](image_20230719_155725.png )

  

3.在Google Drive新增GitHub資料夾以存放ChatGLM2-6B專案

```
%mkdir /content/drive/MyDrive/GitHub  
%cd /content/drive/MyDrive/GitHub
```

※每行Linux指令開頭需加上%符號

4.依[專案說明](https://github.com/THUDM/ChatGLM2-6B#%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F "https://github.com/THUDM/ChatGLM2-6B#%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F")執行

複製ChatGLM2-6B專案、安裝專案依賴、代碼調用

※每行Linux指令開頭需加上%符號

5.效果如下：

[![](image_20230719_153906.png)](image_20230719_153906.png )

  

