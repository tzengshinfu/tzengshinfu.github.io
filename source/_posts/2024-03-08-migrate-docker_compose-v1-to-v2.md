---
layout: post
title: docker compose v1遷移到v2指令的變化
date: 2024-03-08 11:31:00
tags:
- docker
---

 影響：

docker-compose指令在v2版本改成docker compose(整合進docker變成副指令)

有些舊專案卻還是用v1版本的docker-compose造成執行異常(找不到指令)

解法：

1. 建立捷徑檔(user@host:~$ sudo touch /bin/docker-compose)

2. 編輯內容為docker compose --compatibility "$@"

3. 增加捷徑檔執行權限(user@host:~$ sudo chmod +x /bin/docker-compose)

4. docker compose與docker-compose都能執行成功

參考來源：[How to alias docker-compose to docker compose?](https://stackoverflow.com/a/72187587 "https://stackoverflow.com/a/72187587")
