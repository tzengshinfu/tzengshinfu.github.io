---
layout: post
title: 移除Excel保護密碼(★★★僅供還原遺留原始碼,請勿用在非法用途!!!★★★)
date: 2018-02-09 16:47:00
tags:
- excel
---
場景1:  
前人遺留的Excel VBA專案,被密碼保護但沒人記得密碼  
  
解法1:  
1\_備份原始檔(很重要!)  
2\_在要解鎖的Excel VBA專案檔(以下簡稱[專案檔])按右鍵,用解壓縮軟體(本例用7-zip)開啟  
3\_進入 xl 目錄  
4\_編輯 vbaProject.bin 檔案(建議使用Notepad++)  
5\_尋找 DPB 這個字串  
6\_把它改成 DPx (或任一字串, 就是要改變它)  
7\_關閉編輯器後存檔  

[![](step1%60.png)](step1%60.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
8\_用Excel開啟修改後的[專案檔], 因為DPB被改成DPx,所以會顯示錯誤訊息如下,按[是]即可  

[![](step2.png)](step2.png )

  
  
  
  
  
  
  
  
  
  
9\_出現錯誤訊息,按[確定]即可  

[![](step3.png)](step3.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
10\_開啟[開發人員]→[Visual Basic編輯器]  
11\_開啟[工具]→[VBAProject屬性]→[保護]→[檢視專案屬性的密碼]→輸入新的密碼  
12\_按[儲存]  
13\_關閉Excel  

[![](step5.png)](step5.png )

  
  
  
  
  
  
  
  
  
  
  
  
14\_重新開啟修改後的專案檔,即可用新的密碼進入VBA專案。  
  
\*\*Worked in Excel 2016(64bit), Windows 10(xlsm, 啟用巨集的活頁簿)\*\*  
  
  
場景2:  
前人遺留純放資料的Excel,活頁簿(或工作表)被密碼保護但沒人記得密碼  
  
解法2:  
1\_備份原始檔(很重要!)  
2\_在要移除密碼的Excel檔按右鍵,用解壓縮軟體(本例用7-zip)開啟  
3\_進入 xl 目錄  
4\_活頁簿就編輯 workbook.xml 檔案,工作表就下一層worksheets→sheet1.xml(看第幾張表)  

[![](aaaa.png)](aaaa.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

[![](bb.png)](bb.png )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
5\_活頁簿就尋找 workbookProtection 這個Tag並移除,工作表就尋找 sheetProtection 這個Tag並移除之  
6\_重新開啟修改後的Excel檔可發現已密碼移除  

  
參考來源:  
(1)[Is there a way to crack the password on an Excel VBA Project? - Stack Overflow](https://stackoverflow.com/a/4107352/1472545 "https://stackoverflow.com/a/4107352/1472545")  
(2)[#1 How To Remove Password From Excel | Unprotect Excel Password Remover](https://yodalearning.com/tutorials/remove-password-from-excel-trick/ "https://yodalearning.com/tutorials/remove-password-from-excel-trick/")

