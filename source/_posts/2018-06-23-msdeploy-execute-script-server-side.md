---
layout: post
title: msdeploy執行script(Server端)
date: 2018-06-23 16:25:00
tags:
- dos command
- visual studio
---

```
 @ECHO OFF  
 SET APP=%1  
 ::此script檔執行需帶參數=%APP%  
   
   
 ::置換Web.config DB連線字串  
 powershell -command "(Get-Content <專案路徑>\Web.config) -replace ('initial catalog=[a-zA-Z0-9]+;', 'initial catalog=%APP%;') | Out-File <專案路徑>\Web.config"  
   
   
 ::建置專案  
 "MSBuild.exe" "<專案名稱>.csproj" /p:DeployOnBuild=true /property:Configuration=Debug  
   
  
 ::建立資料夾在伺服器的C槽  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create 'cmd.exe /c mkdir C:\%APP%'  
   
  
 ::建立應用程序在伺服器IIS  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create '%systemroot%\system32\inetsrv\appcmd.exe add APPPOOL /name:%APP% /managedRuntimeVersion:"v4.0" /managedPipelineMode:"Integrated" /startMode:AlwaysRunning /recycling.periodicRestart.time:00:00:00 /failure.rapidFailProtection:False /processModel.idleTimeoutAction:Suspend'  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create '%systemroot%\system32\inetsrv\appcmd.exe add APP /path:/%APP% /physicalPath:C:\%APP% /site.name:"Default Web Site" /applicationPool:%APP% /preloadEnabled:True'  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create '%systemroot%\system32\inetsrv\appcmd.exe set CONFIG "Default Web Site/%APP%" /section:urlCompression /doStaticCompression:True'  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create '%systemroot%\system32\inetsrv\appcmd.exe set CONFIG "Default Web Site/%APP%" /section:urlCompression /doDynamicCompression:True'  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create '%systemroot%\system32\inetsrv\appcmd.exe unlock CONFIG /section:anonymousAuthentication'  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create '%systemroot%\system32\inetsrv\appcmd.exe set CONFIG "Default Web Site/%APP%" /section:anonymousAuthentication /enabled:True'  
  
   
 ::設定應用程序的資料夾權限  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create 'cmd.exe /c icacls C:\%APP% /grant "IIS AppPool\%APP%:F"'  
   
  
 ::部署專案  
  
 "msdeploy.exe" -verb:sync -source:iisApp='<專案路徑>PackageTmp' -dest:iisApp='Default Web Site/%APP%',ComputerName='https://<主機名稱>:8172/msdeploy.axd',UserName='<主機名稱>\Administrator',Password='<管理者密碼>',AuthType='Basic',includeAcls='False' -disableLink:AppPoolExtension -disableLink:ContentExtension -disableLink:CertificateExtension -allowUntrusted  
   
  
 ::連線字串加密  
  
 wmic /node:'<主機名稱>' /user:<網域\管理者名稱> /password:'<管理者密碼>' process call create 'aspnet_regiis.exe -pef connectionStrings C:\%APP%'
```

  
   
  
