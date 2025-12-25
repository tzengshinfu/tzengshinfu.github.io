---
layout: post
title: 加速Android Studio/Gradle建置
date: 2017-04-26 17:15:00
tags:
- android studio
---
1.在gradle.properties新增  
 #守護進程，改善Gradle的啟動和執行時間  
 org.gradle.daemon=true  
 #並行編譯  
 org.gradle.parallel=true  
 #按需配置，大型多項目的構建速度更快  
 org.gradle.configureondemand=true  
 #依主機配罝調整  
 org.gradle.jvmargs=-Xms2048m -Xmx2048m -XX:PermSize=512m -XX:MaxPermSize=512m  
 參考:[Xms Xmx PermSize MaxPermSize 区别](https://www.blogger.com/# "https://www.blogger.com/#")  
  
  
2.Gradle設定Use local gradle distribution和Offline work→避免編譯前更新  

[![](%E5%9C%96%E7%89%8720170506_180043.png)](%E5%9C%96%E7%89%8720170506_180043.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
3.Compiler新增命令列參數--offline  

[![](%E5%9C%96%E7%89%8720170506_033139.png)](%E5%9C%96%E7%89%8720170506_033139.png )

  
  
4.SDK選21以上  
  
5.修改studio64.exe.vmoptions設定檔(與執行檔同一目錄)  
新增(或修改)以下字段  
-Xms2048m  
 -Xmx2048m  
 -XX:PermSize=512m  
 -XX:MaxPermSize=512m  
 -XX:ReservedCodeCacheSize=512m

6.停用Android Studio未使用插件  
**1.CVS Integration**  
**2.Git Integration**  
**3.GitHub**  
**4.Google Cloud Tools for Android Studio**  
**5.Subversion Integration**  

[![](%E5%9C%96%E7%89%8720170506_023218.png)](%E5%9C%96%E7%89%8720170506_023218.png )

