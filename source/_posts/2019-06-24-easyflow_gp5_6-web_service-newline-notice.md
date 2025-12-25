---
layout: post
title: 以web service起新流程時內容需換行的注意事項
date: 2019-06-24 14:39:00
---
1.情景:  
表單有TextArea控制項而且內容需換行,在呼叫invokeProcess起新流程時。  
  
2.測試:  
如果是獨立的TexArea控制項  
如:＜TextArea id="TextArea" dataType="java.lang.String" perDataProId=""＞(1)TTTTT\_換行\_(2)EEEEE\_換行\_(3)XXXXX\_換行\_(4)TTTTT＜/TextArea＞  
(1)**＆lt;br /＆gt;**→不會換行,直接變成純文字＜br /＞  
(2)**＆lt;br＆gt;**→不會換行,直接變成純文字＜br＞  
(3)**\n**→不會換行,直接變成純文字\n  
(4)**＆#xA;**→會換行  
  
如果是Grid內的與TexArea控制項連結的欄位  
如:＜Grid id="Grid"＞  
   ＜records＞  
    ＜record id="Grid"＞  
     ＜item id="TextArea" dataType="java.lang.String" perDataProId=""＞(1)TTTTT\_換行\_(2)EEEEE\_換行\_(3)XXXXX\_換行\_(4)TTTTT＜/item＞  
    ＜/record＞  
   ＜/records＞  
  ＜/Grid＞  
(1)**＆lt;br /＆gt;**→Grid欄位換行處會多一空白,點擊時顯示到TextArea也會換行(EasyFlow內部的標準做法)  

[![](Image_20190624124933.png)](Image_20190624124933.png )

(2)**＆lt;br＆gt;**→Grid欄位顯示換行,但點擊時顯示到TextArea卻是變成純文字＜br＞而不會換行  
(3)**\n**→Grid欄位換行處會多一空白,點擊時顯示到TextArea也會換行  
(4)**＆#xA;**→Grid資料完全無法載入顯示  
  
3.結論:  
獨立的TexArea控制項需使用**＆#xA;**換行;如果是Grid內的與TexArea控制項連結的欄位則使用**＆lt;br /＆gt;**換行。  
(本文是全形,實際是半形)

