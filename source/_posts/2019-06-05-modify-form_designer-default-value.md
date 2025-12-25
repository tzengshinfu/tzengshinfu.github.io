---
layout: post
title: 修改表單設計師/設定輔助格線/格線大小的預設值
date: 2019-06-05 15:37:00
tags:
- easyflow gp
---
檔案路徑:[EasyFlow系統目錄]\server\default\deploy\NaNaWeb.war\WMS\FormDesigner\FormDesignerMain.jsp  
  
編輯內容如下:  

```
gVarParent.txtQueryElement.dblclick(function () {
    this.value = "";
});

//產生被選取到的元件ID清單.
$("#btn-selected-elements").click(function () {
    showSelectedElementIdsDialog();
});

//----------加上這段script----------
//在IE直接執行無反應,必須異步執行
setTimeout(function () {
    gVarParent.formBuilder.gridHeight = 10;
    gVarParent.formBuilder.gridWidth = 10;
    gVarParent.currContent.gVar.grid.width(1360);
    gVarParent.currContent.gVar.grid.height(1520);
    gVarParent.formBuilder.drawLayoutGrid(gVarParent.currContent, 2);
}, 500);
//----------加上這段script----------
```
