---
layout: post
title: 在git worktree add後使用TortoiseGit查看log的錯誤(Windows)
date: 2025-10-08 10:44:00
tags:
- git
- windows
---

[![](2025-10-08_10-11-18.png)](2025-10-08_10-11-18.png )

  

原因

在Repo1使用git worktree add建立的資料夾Repo2，  
其擁有者是繼承上位資料夾Workspace，  
但上位資料夾擁有者和目前使用者並不是同一個人。

示意如下：  
Workspace(擁有者：Administrators)  
└Repo1(擁有者：User1)  
└Repo2(擁有者：Administrators)

解法

執行以下指令將Repo2擁有者改為目前使用者即可。

takeown /f  Workspace\Repo1\.git\worktrees\Repo2 /r /d y  
takeown /f  Workspace\Repo2 /r /d y

