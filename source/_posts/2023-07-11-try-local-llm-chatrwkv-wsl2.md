---
layout: post
title: 試用本地小模型ChatRWKV、WSL2、4GB顯卡NVIDIA Quadro P1000
date: 2023-07-11 10:51:00
tags:
- chatrwkv
- llm
---

1.在Windows安裝/更新NVIDIA Windows版[顯卡驅動](https://www.nvidia.com/Download/index.aspx "https://www.nvidia.com/Download/index.aspx")(重要！WSL2內勿安裝Linux版顯卡驅動)

2.在WSL2安裝Linux x86 CUDA Toolkit using WSL-Ubuntu Package([連結](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl-2 "https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl-2"))

3.複製ChatRWKV程式碼，執行git clone https://github.com/BlinkDL/ChatRWKV.git

4.變更現在路徑到ChatRWKV，執行pip install -r requirements.txt(預安裝Python必要套件)

5.下載本地小模型[RWKV-4-Pile-1B5-EngChn-test4-20230115.pth](https://huggingface.co/BlinkDL/rwkv-4-pile-1b5/blob/main/RWKV-4-Pile-1B5-EngChn-test4-20230115.pth "https://huggingface.co/BlinkDL/rwkv-4-pile-1b5/blob/main/RWKV-4-Pile-1B5-EngChn-test4-20230115.pth")到ChatRWKV

6.修改chat.py，

第40行改為 CHAT\_LANG = 'Chinese'

第48及58行改為args.MODEL\_NAME = '<實際路徑>/ChatRWKV/RWKV-4-Pile-1B5-EngChn-test4-20230115'(不須.pth副檔名)

7.執行python chat.py

8.效果如下：

[![](2023-07-11 10 43 05.png)](2023-07-11 10 43 05.png )

  

......😅 😂 🤣

