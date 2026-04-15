---
title: 表單欄位TABLE_COLUMN_vs_FORM_ONLY
date: 2026-04-02 14:22:00
tags:
- tiptop
---

當表單欄位的類型為`FORM_ONLY`  
[![](GeneroStudio_20260402_112502.png)](GeneroStudio_20260402_112502.png )

```xml
<FormField colName="tc_cxx01" fieldtype="FORM_ONLY" name="tc_cxx01" sqlTabName="formonly">
    <ButtonEdit action="controlp" autoNext="--------" case="NONE" century="R" color="black" comment="KEY Field, No Blank/Repeated!, &lt;^P&gt;Qry Employee" data_type="VARCHAR" fontPitch="default" formfieldname="formfield0" gridWidth="10" height="1" hidden="--------" image="zoom" imagetype="Select File" invisible="--------" lstrcomment="false" lstrtitle="false" name="tc_cxx01" noEntry="--------" notNull="true" posX="22" posY="0" required="true" reverse="--------" scroll="--------" sizePolicy="initial" tabIndex="1" verify="--------" width="14" zeroFill="--------"/>
</FormField>
```

用以下語法顯示內容，把l_tc_cxx01值顯示在表單tc_cxx01欄位
```4gl
DISPLAY l_tc_cxx01 TO FORMONLY.tc_cxx01
```

當表單欄位的類型為`TABLE_COLUMN`  
[![](GeneroStudio_20260402_112535.png)](GeneroStudio_20260402_112535.png )

```xml
<FormField colName="azb01" fieldId="0" fieldtype="TABLE_COLUMN" hrecindex="-1" name="azb01" sqlDBName="ds" sqlTabName="azb_file">
    <ButtonEdit action="controlp" autoNext="--------" case="NONE" century="R" color="black" comment="KEY Field, No Blank/Repeated!, &lt;^P&gt;Qry Employee" data_type="VARCHAR" fontPitch="default" formfieldname="formfield0" gridWidth="10" height="1" hidden="--------" image="zoom" imagetype="Select File" invisible="--------" lstrcomment="false" lstrtitle="false" name="azb01" noEntry="--------" notNull="true" posX="22" posY="0" required="true" reverse="--------" scroll="--------" sizePolicy="initial" tabIndex="1" verify="--------" width="10" zeroFill="--------"/>
</FormField>
```

用以下語法顯示內容，把資料庫欄位g_azb.azb01值顯示在表單同名欄位(azb01)
```4gl
DISPLAY BY NAME g_azb.azb01
```
