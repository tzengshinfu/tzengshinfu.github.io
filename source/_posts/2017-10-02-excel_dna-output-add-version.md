---
layout: post
title: Excel-DNA輸出的XLL檔加上版本
date: 2017-10-02 20:45:00
tags:
- excel-dna
---
1\_在設定檔<專案名稱>-AddIn.dna的節點  
加上屬性UseVersionAsOutputVersion="true"  

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
  
2\_專案屬性>應用程式>組件資訊>檔案版本，修改成現在的版次  

[![](step2.png)](step2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
3\_可利用類別FileVersionInfo的方法GetVersionInfo取得屬性FileVersion  

[![](step4.png)](step4.png )

  
  
PS\_可將XLL檔加上DLL副檔名，即可確認版本屬性是否設定正確。  

[![](step3.png)](step3.png )

  
  
  
  

