---
layout: post
title: C#背景操作Excel不會殘留執行緒的方式
date: 2021-09-10 15:21:00
tags:
- c#
- excel
---

Microsoft.Office.Interop.Excel.Application application = null;
Microsoft.Office.Interop.Excel.Workbooks workbooks = null;
Microsoft.Office.Interop.Excel.Workbook workbook = null;

try {

application = new Microsoft.Office.Interop.Excel.Application();

workbooks = application.Workbooks;

workbook = workbooks.Open(@"Excel檔案路徑", Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing, Type.Missing);

  

//workbook相關操作

}

catch (System.Exception ex) {

//異常處理動作

}

finally {

if (workbook != null) {

workbook.Close(false, Type.Missing, Type.Missing);

Marshal.ReleaseComObject(workbook);

}

  

if (workbooks != null) {

workbooks.Close();

Marshal.ReleaseComObject(workbooks);

}

  

if (application != null) {

application.Quit();

Marshal.ReleaseComObject(application);

}

}

參考來源：[https://stackoverflow.com/a/158752](https://stackoverflow.com/a/158752 "https://stackoverflow.com/a/158752")
