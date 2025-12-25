---
layout: post
title: 用async/await避免UI無回應
date: 2017-07-18 10:24:00
tags:
- windows form
---
private **async** void buttonExportExcel\_Click(object sender, EventArgs e) {  
    Button button = (Button)sender;  
    button.Text = "請稍候...";  
    button.Enabled = false;  
    **await** Task.Run(() => {  
        /\*\*用迴圈產生Excel內容的耗時作業\*/  
    });  
    button.Text = "匯出Excel";  
    button.Enabled = true;  
    MessageBox.Show("儲存成功");  
}  
  
1.在Function新增async關鍵字,代表非同步作業。  
 2.在耗時作業的部份加上await關鍵字,就會另外開啟執行緒處理,UI不會無回應。   
   
 參考:[Using Async and Await to update the UI Thread](https://www.blogger.com/# "https://www.blogger.com/#")
