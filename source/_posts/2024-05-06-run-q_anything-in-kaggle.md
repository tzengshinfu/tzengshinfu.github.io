---
layout: post
title: 在Kaggle執行QAnything(支援任意格式檔或資料庫的本地知識庫問答系統)
date: 2024-05-06 10:25:00
tags:
- kaggle
- qanything
---
1.複製QAnything倉庫

```
!git clone -b develop_for_v1.3.1 https://github.com/netease-youdao/QAnything.git
```

2.切換工作目錄

```
%cd '/kaggle/working/QAnything'
```

3.更新Kaggle vllm版本

```
!pip install vllm -U
```

4.更新Kaggle pydantic版本

```
!pip install -U pydantic
```

5.安裝QAnything所需元件

```
!pip install -e .
```

6.安裝ngrok執行檔

```
 !curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```

7.新增ngrok認證token(需預先註冊)

```
!ngrok config add-authtoken <ngrok認證token>
```

8.安裝pyngrok

```
!pip install pyngrok
```

9.執行完成後會顯示public\_url="<公開網址>"

```
from pyngrok import ngrok, conf

conf.get_default().auth_token = "<ngrok認證token>"
port = "8777"
public_url = ngrok.connect(port).public_url
print(f"public_url=\"{public_url}\"")
```

10.執行完成後即可連至<公開網址>/qanything/進行知識庫問答

```
!bash scripts/run_for_3B_in_Linux_or_WSL.sh
```
