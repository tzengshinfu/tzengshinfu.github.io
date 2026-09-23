---
title: 移除Docker Desktop on Windows並在Windows與WSL2安裝原生Docker
date: 2026-09-22 16:25:30
tags:
- wsl2
- windows
- visual studio code
---

原文是保哥的[如何移除 Docker Desktop 並在 Windows 與 WSL 2 改安裝 Docker Engine](https://blog.miniasp.com/post/2025/06/14/How-to-remove-Docker-Desktop-and-install-Docker-Engine-on-Windows-with-WSL-2)，  
因為每次重灌OS又要設定，求人不如求己，針對自己的環境，用自己的筆觸記錄下來。

1. 移除Docker Desktop on Windows
   1. 在Windows應用程式移除Docker Desktop on Windows。
   2. 在WSL2移除以下兩個符號連結檔案。

      ```bash
      rm -f ~/.docker/contexts ~/.docker/features.json
      ```

   3. 在WSL2刪除所有cli-plugins檔案。

      ```bash
      sudo rm /usr/local/lib/docker/cli-plugins/docker-*
      ```

   4. 在Windows重啟WSL2服務。

      ```dos
      wsl.exe --shutdown
      ```

   5. 在Windows升級WSL2。

      ```dos
      wsl --update
      ```

2. 在WSL2安裝Docker/Docker Compose
   1. 在WSL2下載Docker/Docker Compose安裝腳本。

      ```bash
      curl -fsSL https://get.docker.com -o get-docker.sh
      ```

   2. 執行安裝腳本。

      ```bash
      sudo sh get-docker.sh
      ```

   3. 安裝腳本get-docker.sh有一段邏輯，會建議你按Ctrl+C中止此腳本並安裝Docker Desktop on Windows，等20秒即可跳過繼續執行。

      ```bash
      if is_wsl; then
          echo
          echo "WSL DETECTED: We recommend using Docker /Desktop for Windows."
          echo "Please get Docker Desktop from https://www.docker.com/products/docker-desktop/"
          echo
          cat >&2 <<-'EOF'
   
                  You may press Ctrl+C now to abort this script.
          EOF
          ( set -x; sleep 20 )
      fi
      ```

   4. 將登入WSL2帳號加入docker群組。

      ```bash
      sudo usermod -aG docker $USER
      ```

3. 透過WSL2的systemd服務啟動Docker
   安裝腳本get-docker.sh會安裝Docker服務(docker.service)，可以用以下指令確認。

   ```bash
   systemctl status docker.service
   ```

4. 讓dockerd同時監聽Unix socket file與TCP連線
  
   可在Windows下管理WSL2的Docker，  
   在Windows的VSCode也能直接連到Docker進行管理。

   1. 讓dockerd同時監聽Unix與TCP  
      在WSL2的/etc/docker/daemon.json加入：

      ```json
      {
        ......
        "hosts": [
          "unix:///var/run/docker.sock",
          "tcp://127.0.0.1:2375"
        ]
        ......
      }
      ```

   2. 編輯systemd服務設定(Docker服務)  
      編輯/etc/systemd/system/docker.service.d/override.conf

      ```ini
      [Service]
      ExecStart=
      ExecStart=/usr/bin/dockerd --containerd=/run/containerd/containerd.sock
      ```

   3. 套用變更

      ```bash
      sudo systemctl daemon-reload
      sudo systemctl restart docker
      ```

   4. 驗證，看到 LISTEN 狀態代表成功。

      ```bash
      $ ss -lntp | grep 2375
      LISTEN 0      4096                *:2375            *:*
      ```

5. 在Windows命令提示字元下也能使用docker指令

   在Windows安裝docker-cli和docker compose

   ```dos
   winget install --id Docker.DockerCLI && winget install --id Docker.DockerCompose
   ```

   設定環境變數

   ```dos
   setx DOCKER_HOST 127.0.0.1:2375
   ```

6. 讓Windows的VSCode的Container Tools也能管理Docker

   在設定檔的JSON加入：

   ```json
   {
       ......
       "containers.environment": {
           "DOCKER_HOST": "tcp://127.0.0.1:2375"
       }
       ......
   }
   ```
