---
layout: post
title: 檢查XLL版本一直是舊版
date: 2017-11-06 16:09:00
tags:
- excel-dna
---
**狀況**  
使用FileVersionInfo類別的GetVersionInfo方法，  
所得的FileVersion屬性一直是修改前的舊值(1.0.4)而不會更新(1.0.10)。  

[![](oldversion.png)](oldversion.png )

  
  
  
  
  
  
  
  
1\_專案屬性>應用程式>組件資訊>檔案版本確實是1.0.10。  

[![](step2.png)](step2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
2\_<專案名稱>-AddIn.dna設定檔有加上UseVersionAsOutputVersion="true"。  

[![](step3.png)](step3.png )

  
  
  
  
  
  
  
  
**解法**  
將該檔案路徑停用共享，再重新開啟即正常。

