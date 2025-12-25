---
layout: post
title: GitHub Copilot CLI在Windows Terminal按Shift+Enter換行
date: 2025-10-23 17:02:00
tags:
- github copilot cli
- windows terminal
---

目前v0.0349仍無法直接設定，但可修改Windows Terminal設定檔以達成相同目的。

```
{

    "actions":



    [



        //#region 新增這段



        {



            "command":



            {



                "action": "sendInput",



                "input": "\n"



            },



            "id": "linefeed"



        }



        //#endregion



    ],



    "keybindings":



    [



        //#region 新增這段



        {



            "id": "linefeed",



            "keys": "shift+enter"



        }



        //#endregion



    ]



}
```

參考來源：[CLI should support multi-line mode in input box](https://github.com/github/copilot-cli/issues/14#issuecomment-3399405101 "https://github.com/github/copilot-cli/issues/14#issuecomment-3399405101")
