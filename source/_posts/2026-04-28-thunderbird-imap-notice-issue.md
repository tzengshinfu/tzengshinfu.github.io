---
title: Thunderbird IMAP信箱不會跳顯通知
date: 2026-04-28 15:49:18
tags:
- thunderbird
---

1. 點選Tools─►Settings─►General─►Network & Disk Space─►Config Editor...  
[![](thunderbird_20260428_143754.png)](thunderbird_20260428_143754.png)

2. 在紅框處輸入鍵值:  
[![](Capture_20260428_160037.png)](Capture_20260428_160037.png)

3. 將`mail.server.default.check_all_folders_for_new`設為**true**。  
   (5.0之前則是`mail.check_all_imap_folders_for_new`)  

4. 將`mail.imap.use_status_for_biff`設為**false**。

5. 另外建議: 點選Tools─►Settings─►General─►Incoming Mails  
   取消選擇`Use the system notification`。  
   [![](thunderbird_20260428_143754.png)](thunderbird_20260428_143754.png)
   
   - 勾選時的通知，統一格式:  
   [![](Capture_20260428_165007.png)](Capture_20260428_165007.png)
   
   - 取消勾選時的通知，會顯示主旨:  
   [![](Capture_20260428_164813.png)](Capture_20260428_164813.png)

參考來源：[Check all folders for new messages](https://github.com/mendel5/thunderbird#check-all-folders-for-new-messages)
