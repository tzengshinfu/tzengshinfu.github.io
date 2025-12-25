---
layout: post
title: 退回重辦後無法向後加簽
date: 2020-01-31 10:04:00
tags:
- easyflow gp
---
狀況:  
 顯示錯誤訊息如下  
 [![](at1.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
  
  
原因:  
 此為EasyFlow系統邏輯;   
 因為退回重辦有2種方式,   
 下圖藍色是主管退回,在修正後送出仍要重跑每一關才到主管,   
 下圖紅色是主管退回,在修正後送出就直接回到主管,   
 [![](at2.png)](https://www.blogger.com/# "https://www.blogger.com/#")   
   
如果選擇上圖紅色(=略過之前已經執行過的關卡,直接回傳給我),   
 系統會限制重新修正後派送的下一關就是主管而無法向後加簽,   
   
   
 做法:   
 1.可先派送回主管,再請主管重新選擇上圖藍色再退回重辦則能向後加簽。   
 或   
 2.以SQL語法修改狀態。  

```
SELECT OID --被退回的關卡的OID
,comeBackActivityInstOID ,definitionId ,createdTime
FROM ParticipantActivityInstance
WHERE contextOID = ( SELECT contextOID
    FROM ProcessInstance
    WHERE serialNumber = '流程序號' ) AND definitionId = '目前被退回的關卡代號'
ORDER BY createdTime DESC OFFSET 0 ROWS FETCH FIRST 1 ROWS ONLY

--2.將comeBackActivityInstOID設為NULL
UPDATE ParticipantActivityInstance SET comeBackActivityInstOID = NULL WHERE OID = '被退回的關卡的OID'
```

  
即可向後加簽。(會變成一關一關派送。)

