---
layout: post
title: 發單時選錯部門導致跑到錯誤的直屬主管之解決方法
date: 2018-12-28 08:01:00
tags:
- easyflow gp
---
場景:   
 發單者有主(=TCM0131)部門及其他(=TCG0123)部門, 兩個部門直屬主管為不同人。   
 流程其中有關卡為發單者直屬主管。   
 [![](0_0_image002.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
[![](0_0_image003.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
  
 發單時選錯部門。   
  
   
 被退回重辦, 但發單者再次派送, 系統卻不會再詢問要用哪個單位進行派送導致又送錯主管。   
此時可以   
 1. 請User終止原流程, 重新發單。   
 或   
 2. 修正EasyFlow參考及發單部門欄位。   
   
 動作:   
 (1) 先退回發單者關卡。   
 (2) 修改DB:EFGP的Table:ProcessInstance流程資料, 把發單部門及參考部門都改為正確的部門。   
  
 SQL語法:   

```
     DECLARE @UNIT_OID char(32) = (SELECT OID FROM OrganizationUnit WHERE id = '<正確部門代號>');   
   
       UPDATE ProcessInstance   
       SET referOrganizationUnitOID = @UNIT_OID, /**改這個欄位, 流程引擎在派送到下一關卡時會依照這個欄位判斷流向。*/   
       invokeOrganizationUnitOID = @UNIT_OID  
 ,objectVersion = objectVersion + 1   
       WHERE serialNumber = <流程序號>;
```

  
   
 (3) 重新派送, 發現已可到正確的直屬主管。   
 [![](0_0_image004.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   

