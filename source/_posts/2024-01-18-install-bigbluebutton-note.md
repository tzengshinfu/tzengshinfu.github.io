---
layout: post
title: 安裝BigBlueButton(白板系統)注意事項
date: 2024-01-18 13:12:00
tags:
- bigbluebutton
---

安裝
--

1. 主機OS版本需為Ubuntu 20.04。
2. 將SSL憑證上傳到/local/certs/目錄下，並將 `STAR_<公司名稱>_com.pem`更名為 `fullchain.pem`、`private.key`更名為 `privkey.pem`。
3. 執行安裝腳本 `wget -qO- https://raw.githubusercontent.com/bigbluebutton/bbb-install/v2.7.x-release/bbb-install.sh | bash -s -- -v focal-270 -s <主機FQDN> -g -k -d`。
4. 執行cd greenlight-v3。
5. 修改設定檔 `.env`### SMTP CONFIGURATION設定。
6. 修改設定檔 `.env`### EXTERNAL AUTHENTICATION METHODS(參照[External Authentication](https://docs.bigbluebutton.org/greenlight/v3/external-authentication "https://docs.bigbluebutton.org/greenlight/v3/external-authentication"))。
7. 執行 `docker-compose down && docker-compose up -d`重啟容器即可。

注意
--

* 升級BigBlueButton：

1. 不可直接升級套件(`apt upgrade` or `apt dist-upgrade`)會造成設定檔設定錯誤而無法正常使用。
2. 升級需再次執行安裝腳本 `wget -qO- https://raw.githubusercontent.com/bigbluebutton/bbb-install/v2.7.x-release/bbb-install.sh | bash -s -- -v focal-270 -s <主機FQDN> -g -k -d`，將會進行套件升級及BigBlueButton升級。

* 將GreenLight使用者提升為管理員：

1. 執行 `docker exec -it greenlight-v3 /bin/bash`進入GreenLight容器。
2. 在GreenLight容器執行 `rails console`進入RoR控制台。
3. 執行 `mail="<使用者信箱>"`。
4. 執行 `user = User.find_by(email: mail, provider: "greenlight")`。
5. 執行 `user.role = Role.find_by(name: "Administrator", provider: "greenlight")`。
6. 執行 `user.save!`。
7. 連續執行 `exit`斷開連線。
8. 重新登入BigBlueButton+GreenLight即為管理者。
