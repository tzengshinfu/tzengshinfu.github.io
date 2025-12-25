---
layout: post
title: "(筆記)部署.Net Core 3.1到IIS 8.5在Windows 2012 R2"
date: 2020-09-10 09:23:00
tags:
- ".net core"
---

**1.安裝.Net Core Runtime**A.ASP.NET Core 3.1 Runtime (v3.1.8) - Windows Hosting Bundle Installer(dotnet-hosting-3.1.8-win.exe)  
↓相依元件↓  
B.Microsoft Visual C++ Redistributable for Visual Studio 2015-2019(VC\_redist.x64.exe)  
↓相依hotfix↓  
C.Windows8.1-KB2999226-x64.msu  
↓相依hotfix↓  
D.Windows8.1-KB2919355-x64.msu(很大,快700MB,要等)  
↓相依hotfix↓  
E.Windows8.1-KB2975061-x64.msu + 1.Windows8.1-KB2939087-x64.msu  
(所以安裝順序為E→D→C→B→A)

參考:[https://dotblogs.com.tw/dog0416/2016/09/05/152344](https://dotblogs.com.tw/dog0416/2016/09/05/152344 "https://dotblogs.com.tw/dog0416/2016/09/05/152344")

**2.重啟IIS服務**在命令列輸入  
net stop was /y  
net start w3svc

**3.新增站台**應用程式集區將CLR版本改成【沒有 Managed 程式碼】  
網站資料夾的安全性需新增【IIS\_IUSRS】群組,並賦予"完全控制"權限

參考:[https://blog.johnwu.cc/article/iis-run-asp-net-core.html](https://blog.johnwu.cc/article/iis-run-asp-net-core.html "https://blog.johnwu.cc/article/iis-run-asp-net-core.html")

**4.發行(透過Web Deploy)**Visual Studio 2019→建置→發佈  
目標→網頁伺服器(IIS)→Web Deploy→輸入伺服器連線資訊→完成→發佈  
※在發佈前,下方的摘要LastUsedBuildConfiguartion右邊有編輯圖示(一支筆)  
點下去會出現傳統的Web Deploy設定畫面,記得點最下方的【驗證連線】,  
等下發行才不會有驗證問題。(錯誤如下)

Web deployment task failed. (已連線到使用指定之處理程序 ("Web Management Service") 的遠端電腦 ("192.168.100.102")，但是無法驗證伺服器的憑證。如果您信任該伺服器，請再次連線，並允許未受信任的憑證。

參考:[https://stackoverflow.com/questions/33088371/msdeploy-getting-error-certificate-validation-failed-allowuntrusted-being-ignor](https://stackoverflow.com/questions/33088371/msdeploy-getting-error-certificate-validation-failed-allowuntrusted-being-ignor "https://stackoverflow.com/questions/33088371/msdeploy-getting-error-certificate-validation-failed-allowuntrusted-being-ignor")
