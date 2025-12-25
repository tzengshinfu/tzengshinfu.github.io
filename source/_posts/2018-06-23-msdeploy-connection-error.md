---
layout: post
title: msdeploy(web deploy)後顯示錯誤連線{"初始化字串的格式和開始於索引 0 的規格不相符"}
date: 2018-06-23 16:03:00
tags:
- asp.net
---
狀況:  
 部署後在web.config的連線字串會變成$(ReplacableToken\_連線字串名稱-Web.config Connection String\_0)  
   
 解法:  
 在專案的csproj檔,在各組態的<PropertyGroup>都加入  
 <AutoParameterizationWebConfigConnectionStrings>False</AutoParameterizationWebConfigConnectionStrings>  
   
 來源:  
 [https://docs.microsoft.c](https://www.blogger.com/# "https://www.blogger.com/#")[om/zh-tw/aspnet/web-forms/overview/deployment/visual-studio-web-deployment/troubleshooting#format-of-the-initialization-string-does-not-conform-to-specification-starting-at-index-0](https://docs.microsoft.com/zh-tw/aspnet/web-forms/overview/deployment/visual-studio-web-deployment/troubleshooting#format-of-the-initialization-string-does-not-conform-to-specification-starting-at-index-0 "https://docs.microsoft.com/zh-tw/aspnet/web-forms/overview/deployment/visual-studio-web-deployment/troubleshooting#format-of-the-initialization-string-does-not-conform-to-specification-starting-at-index-0")
