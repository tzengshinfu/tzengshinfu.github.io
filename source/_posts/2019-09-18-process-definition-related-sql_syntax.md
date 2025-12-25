---
layout: post
title: 流程定義相關語法
date: 2019-09-18 14:00:00
tags:
- easyflow gp
- sql
---

```
/**流程序號*/  
DECLARE @SerialNumber nvarchar(50) = 'PKG1564733072307100000069';  
  
/**以序號找到流程定義OID*/  
DECLARE @ProcessDefinitionOID char(32) = (  
    SELECT ProcessDefinitionOID FROM ProcessPackage_ProcessDef WHERE ProcessPackageOID = (  
        SELECT processPackageOID FROM ProcessContext WHERE containerOID = (  
            SELECT OID FROM ProcessInstance WHERE serialNumber = @SerialNumber  
        )  
    )  
);  
  
/**列出流程定義所有活動*/  
SELECT * FROM ActivityDefinition WHERE containerOID = @ProcessDefinitionOID;  
  
  
/**以序號找到流程序號OID*/  
DECLARE @ProcessInstanceOID char(32) = (SELECT OID FROM ProcessInstance WHERE serialNumber = @SerialNumber);  
  
  
/**列出流程設定*/  
/*  
活動定義(ActivityDefinition):新流程會套用  
活動實體(ParticipantActivityInstance):進行中流程設定  
(如果要修改則上述兩個table都要修改,不然會有異常)  
加簽(addingActivityAuthority):1=前一活動/2=後一活動/3=前後/0=不允  
退回(ableToAskActivityReexecute):3=1.直接送回要求退件者/2=2.按流程定義送回要求退件者/0=3.不允許退件/4=允許1、2。預設直接送回要求退件者/1=允許1、2。預設按流程定義送回要求退件者  
轉他人處理(reassignable):1=允許/0=不允許  
取回重辦(regainable):1=允許/0=不允許(僅ActivityDefinition有)  
批次簽核(batchPerformable):1=允許/0=不允許  
活動類型(performType):NORMAL/NOTICE/EXECUTION  
參與者(performerIds):如果有多位以逗號區隔,只能寫入同一版流程定義的參與者定義ID(ParticipantDefinition),不然會異常無法派送(僅ActivityDefinition有)  
*/  
SELECT OID, activityDefinitionName, addingActivityAuthority, ableToAskActivityReexecute, reassignable, regainable, batchPerformable, performType, performerIds FROM ActivityDefinition WHERE containerOID = @ProcessDefinitionOID;  
SELECT OID, addingActivityAuthority, ableToAskActivityReexecute, reassignable, batchPerformable, performType FROM ParticipantActivityInstance WHERE containerOID = @ProcessInstanceOID;  
  
  
/**活動連接阜設定:joinType=合併限制條件/splitType=分流限制條件*/  
SELECT joinType, splitType FROM TransitionRestriction where containerOID = '{特定關卡的ActivityDefinition.OID}';
  
  
/**
關卡間的每條路徑,其名稱/型別/條件運算式
路徑定義(TransitionDefinition):即關卡間的每條路徑
條件定義(ConditionDefinition):路徑分支的條件
型別(conditionType):CONDITION=條件型別/OTHERWISE=否則型別/EXCEPTION=例外條件型別/DEFAULTEXCEPTION=預設例外型別
運算式(content):當conditionType=CONDITION則有值,其他型別為空字串
*/
SELECT id, transitionDefinitionName, conditionOID, conditionType, content
FROM TransitionDefinition
LEFT JOIN ConditionDefinition
ON TransitionDefinition.conditionOID = ConditionDefinition.OID
WHERE containerOID = @ProcessDefinitionOID;
  
  
/**  
核決權限表  
參考活動ID(referActivityId)  
單位主管核定(isManagerDecide)
*/
SELECT activityDefinitionName, referActivityId, isManagerDecide, decisionRuleListOID
FROM ActivityDefinition
INNER JOIN DecisionRuleList
ON ActivityDefinition.decisionRuleListOID = DecisionRuleList.OID
WHERE containerOID = @ProcessDefinitionOID;  
  
  
/**核決權限表規則  
運算式(content)  
判斷順序(showIndex):逐筆判斷的順位,由小到大
*/  
SELECT content, showIndex FROM DecisionRuleList  
INNER JOIN DecisionCondition ON DecisionRuleList.OID = DecisionCondition.containerOID  
WHERE DecisionRuleList.OID = '{特定核決權限關卡的ActivityDefinition.decisionRuleListOID}';
```
