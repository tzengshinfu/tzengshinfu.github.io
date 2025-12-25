---
layout: post
title: LimeSurvey特定問題依其他題目的答案而變更為選填或必填
date: 2024-04-17 19:07:00
tags:
- limesurvey
---

1.把特定問題(本例為Q02意見題)的**設定**>**一般化設置**>**必填**改為'關'(='選填')，用後續的公式來控制'選填'或'必填'。

[![](1.jpg)](1.jpg )

2.在Q02意見題的**設定**>**邏輯**>**問題驗證方程式**填入驗證公式：

(

Q01 >= 3                                    #當Q01等級大於等於3

or                                                 #或

(Q01 < 3 and !is\_empty(Q02))  #當Q01等級小於3 以及 Q02意見題 不得為空

)

並在**設定**>**邏輯**>**問題驗證提示**填入"Q01如果是3顆星以下則此題必填"。

[![](2.jpg)](2.jpg )

  

3.當不通過驗證公式時將會無法送出，如下圖：

[![](image_20240417_190331.png)](image_20240417_190331.png )

  

參考來源：[How Do I Make Question As Mandatory Based On Certain Answer Of Previous Question](https://forums.limesurvey.org/forum/can-i-do-this-with-limesurvey/121752-how-do-i-make-question-as-mandatory-based-on-certain-answer-of-previous-question "https://forums.limesurvey.org/forum/can-i-do-this-with-limesurvey/121752-how-do-i-make-question-as-mandatory-based-on-certain-answer-of-previous-question")

