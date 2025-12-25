---
layout: post
title: SSIS設定需特別注意之處
date: 2017-04-24 12:08:00
tags:
- ssis
---
SSISDB的[作業記錄檔]>>[保留週期]預設為365天， 在運行一段時期後，排程週期 x 執行專案數量 x 專案的元件數 所產生的log  
 會使該DB容量激增，  
 所以在初期規劃時就要注意該設定必須設在一個合理值。

[![](1.png)](1.png )

  
  
  
記錄層次設為【效能】(只記錄錯誤事件)  

[![](2.png)](2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
定期壓縮ldf檔(因[作業記錄檔]>[定期清除記錄檔]刪除動作會產生大量log)  
→可加入到[SSIS Server Maintenance Job]的最後1個步驟。  

[![](step1.png)](step1.png )

  
  
  
  
  
  
  
  
  
  
  
指令如下圖示:  

[![](step2.png)](step2.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
需另外設定權限:  

[![](step3.png)](step3.png )

  

