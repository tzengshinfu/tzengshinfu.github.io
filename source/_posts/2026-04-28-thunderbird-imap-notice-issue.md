---
title: Thunderbird IMAP信箱不會跳顯通知
date: 2026-04-28 15:49:18
tags:
- thunderbird
---

1. Tools─►Settings─►General─►Config Editor...  
[![](thunderbird_20260428_143754.png)](thunderbird_20260428_143754.png)

2. 在紅框處輸入鍵值:  
[![](Capture_20260428_160037.png)](Capture_20260428_160037.png)

3. 將`mail.server.default.check_all_folders_for_new`設為**true**。  
   (5.0之前則是`mail.check_all_imap_folders_for_new`)  

5. 將`mail.imap.use_status_for_biff`設為**false**。

參考來源：[Check all folders for new messages](https://github.com/mendel5/thunderbird#check-all-folders-for-new-messages)
