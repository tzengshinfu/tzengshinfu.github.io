---
layout: post
title: "[構想]自主開發系統 - 資料儲存格式"
date: 2018-02-10 12:05:00
tags:
- 自主系統開發
---

資料儲存格式
======

格式如下:  
資料1名稱:資料1型態=資料1內容;資料2名稱:資料2型態=資料2內容;資料3名稱:資料3型態=資料3內容;....

1.儲存一般資料  
column1:int=23;column2:varchar(50)="test";column3:datetime2(7)=2017-10-10 10:00:00.000;column4:bit=1;

2.儲存二進位資料  
column5:varbinary(max)=0x3C3F786D6C2076657273696F6E3D22312E302220656E636F646...;

3.儲存null  
column6:nvarchar(50)=null;
