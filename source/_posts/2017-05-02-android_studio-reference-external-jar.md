---
layout: post
title: Android Studio引用外部jar
date: 2017-05-02 16:33:00
tags:
- android studio
---
1.取得宣告連結  

[![](Image_20170502163145.jpg)](Image_20170502163145.jpg )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
2.在該項目的build.gradle增加  

[![](gradle.png)](gradle.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
3.如果建置時發生錯誤【Duplicate files copied in APK META-INF/LICENSE】如下圖示:  

[![](Image_20170508175212.png)](Image_20170508175212.png )

  
  
  
  
  
則需要再增加  

```
android {  
     packagingOptions {  
         exclude 'META-INF/DEPENDENCIES'  
         exclude 'META-INF/NOTICE'  
         exclude 'META-INF/LICENSE'  
         exclude 'META-INF/LICENSE.txt'  
         exclude 'META-INF/NOTICE.txt'  
     }  
 }
```

  
\*\*因為很多的第三方函式庫會拆解成多個(基本和擴充)，都擁有相同的版權宣告檔案，就會造成編譯時檔案衝突的錯誤而無法編譯。

