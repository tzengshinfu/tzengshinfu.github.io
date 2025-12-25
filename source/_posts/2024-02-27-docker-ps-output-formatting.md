---
layout: post
title: docker ps 輸出結果格式化
date: 2024-02-27 10:40:00
tags:
- docker
---
1.開啟~/.docker/config.json。(不存在則新增)

2.編輯內容，新增屬性"psFormat"，輸出欄位可參照[Format the output (--format)](https://docs.docker.com/reference/cli/docker/container/ls/#format "https://docs.docker.com/reference/cli/docker/container/ls/#format")。

{

"psFormat": "table {% raw %}{{.Names}}{% endraw %}\t{% raw %}{{.Image}}{% endraw %}\t{% raw %}{{.Status}}{% endraw %}\t{% raw %}{{.Ports}}{% endraw %}"

}

參考來源：[Docker CLI configuration file (config.json) properties](https://docs.docker.com/engine/reference/commandline/cli/#docker-cli-configuration-file-configjson-properties "https://docs.docker.com/engine/reference/commandline/cli/#docker-cli-configuration-file-configjson-properties")
