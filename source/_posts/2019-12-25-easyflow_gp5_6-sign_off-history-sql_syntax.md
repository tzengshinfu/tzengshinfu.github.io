---
layout: post
title: EasyFlow簽核履歷完整版SQL
date: 2019-12-25 14:43:00
tags:
- easyflow gp
- sql
---
1.包括轉派歷程  
 2.整合表單上方的履歷跟下方的意見  

```
DECLARE @processDefinitionId nvarchar(100) = N'[要搜尋的流程定義代號]';
DECLARE @formSerialNumber nvarchar(50) = N'[要搜尋的表單編號]';
DECLARE @rsrcType nvarchar(10) = N'zh_TW';
DECLARE @processNotStartedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.processInstance.state.notStarted' AND rsrcType = @rsrcType);
DECLARE @processRunningText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.processInstance.state.running' AND rsrcType = @rsrcType);
DECLARE @processSuspendedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.processInstance.state.suspended' AND rsrcType = @rsrcType);
DECLARE @processCompletedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.processInstance.state.completed' AND rsrcType = @rsrcType);
DECLARE @processAbortedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.processInstance.state.aborted' AND rsrcType = @rsrcType);
DECLARE @processTerminatedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.processInstance.state.terminated' AND rsrcType = @rsrcType);
DECLARE @notStartedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.notStarted' AND rsrcType = @rsrcType);
DECLARE @runningText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.running' AND rsrcType = @rsrcType);
DECLARE @suspendedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.suspended' AND rsrcType = @rsrcType);
DECLARE @completedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.completed' AND rsrcType = @rsrcType);
DECLARE @abortedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.aborted' AND rsrcType = @rsrcType);
DECLARE @terminatedText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.terminated' AND rsrcType = @rsrcType);
DECLARE @reexecuteText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.reexecute' AND rsrcType = @rsrcType);
DECLARE @addCustomActText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.addCustomAct' AND rsrcType = @rsrcType);
DECLARE @rollBackText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.rollBack' AND rsrcType = @rsrcType);
DECLARE @noticeText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.notice' AND rsrcType = @rsrcType);
DECLARE @executionText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.execution' AND rsrcType = @rsrcType);
DECLARE @automaticText nvarchar(MAX) = (SELECT CAST(labelValue AS nvarchar(MAX)) AS labelValue FROM DBRsrcBundle WHERE labelKey = 'label.workStep.state.automatic' AND rsrcType = @rsrcType);

SELECT CASE History.流程狀態
        WHEN 0
            THEN @processNotStartedText
        WHEN 1
            THEN @processRunningText
        WHEN 2
            THEN @processSuspendedText
        WHEN 3
            THEN @processCompletedText
        WHEN 4
            THEN @processAbortedText
        WHEN 5
            THEN @processTerminatedText
        END AS "流程狀態"
    ,History.處理者
    ,FORMAT(History.建立時間, 'yyyy/MM/dd HH:MM:ss') AS "建立時間"
    ,FORMAT(History.簽核時間, 'yyyy/MM/dd HH:MM:ss') AS "簽核時間"
    ,History.簽核意見
    ,History.關卡名稱
    ,History.狀態
FROM (
    SELECT ProcessState AS "流程狀態"
        ,CASE 
            WHEN newAssigneeOID IS NOT NULL
                THEN id + '-' + userName + '(代)'
            ELSE id + '-' + userName
            END AS "處理者"
        ,WorkItemData.createdTime AS "建立時間"
        ,WorkItemData.completedTime AS "簽核時間"
        ,CASE 
            WHEN WorkItemData.skipUserName <> ''
                THEN WorkItemData.executiveComment + N'(' + WorkItemData.skipUserName + ')'
            ELSE WorkItemData.executiveComment
            END AS "簽核意見"
        ,WorkItemData.workItemName AS "關卡名稱"
        ,CASE 
            WHEN WorkItemData.bypassPerformerOID IS NOT NULL
                THEN N'已跳過'
            WHEN currentState = 0
                THEN @notStartedText
            WHEN currentState = 1
                THEN @runningText
            WHEN currentState = 2
                THEN @suspendedText
            WHEN currentState = 4
                THEN @abortedText /**撤銷*/
            WHEN currentState = 3
                AND WorkItemData.performType = 'NOTICE'
                THEN @noticeText /**通知*/
            WHEN currentState = 3
                AND WorkItemData.performType = 'EXECUTION'
                THEN @executionText /**會辦*/
            WHEN currentState = 3
                AND WorkItemData.signoffState = 1
                THEN @automaticText /**自動簽核*/
            WHEN currentState = 3
                THEN @completedText
            WHEN currentState = 5
                AND WorkItemData.terminateReason = 0
                THEN @terminatedText /**終止*/
            WHEN currentState = 5
                AND WorkItemData.terminateReason = 1
                THEN @reexecuteText /**退回*/
            WHEN currentState = 5
                AND WorkItemData.terminateReason = 2
                THEN @addCustomActText /**向前加簽*/
            WHEN currentState = 5
                AND WorkItemData.terminateReason = 3
                THEN @rollBackText /**取回*/
            WHEN currentState = 5
                THEN @terminatedText /**終止*/
            END AS "狀態"
    FROM (
        SELECT ProcessInstance.currentState AS ProcessState
            ,CASE 
                WHEN WorkItem.performerOID IS NULL
                    AND WorkAssignment.assigneeOID IS NOT NULL
                    THEN WorkAssignment.assigneeOID
                ELSE WorkItem.performerOID
                END performerOID
            ,COALESCE(CAST(WorkItem.executiveComment AS NVARCHAR(MAX)), '') AS executiveComment
            ,WorkItem.workItemName
            ,WorkItem.createdTime
            ,WorkItem.completedTime
            ,WorkItem.currentState
            ,ParticipantActivityInstance.performType
            ,ReassignWorkItemAuditData.newAssigneeOID
            ,WorkItem.skipUserName
            ,WorkItem.signoffState
            ,ParticipantActivityInstance.terminateReason
        FROM WorkItem
        LEFT JOIN WorkAssignment
            ON WorkAssignment.workItemOID = WorkItem.OID
        INNER JOIN ProcessContext
            ON ProcessContext.OID = WorkItem.contextOID
        INNER JOIN ProcessInstance
            ON ProcessInstance.OID = ProcessContext.containerOID
        INNER JOIN LocalRelevantData
            ON LocalRelevantData.containerOID = ProcessInstance.contextOID
        INNER JOIN FormInstance
            ON FormInstance.OID = LocalRelevantData.valueOID
        INNER JOIN ParticipantActivityInstance
            ON ParticipantActivityInstance.OID = WorkItem.containerOID
        LEFT JOIN ReassignWorkItemAuditData
            ON ReassignWorkItemAuditData.currentProcessInstanceOID = ProcessInstance.OID
                AND ReassignWorkItemAuditData.currentActivityInstanceOID = ParticipantActivityInstance.OID
                AND ReassignWorkItemAuditData.sourceOID = WorkItem.OID
        WHERE ProcessInstance.processDefinitionId = @processDefinitionId
            AND FormInstance.serialNumber = @formSerialNumber
        ) AS WorkItemData
    INNER JOIN Users
        ON Users.OID = WorkItemData.performerOID
    
    UNION
    
    SELECT ProcessInstance.currentState AS "流程狀態"
        ,oldAssigneeId + '-' + oldAssigneeName AS "處理者"
        ,ReassignWorkItemAuditData.createdTime AS "建立時間"
        ,ReassignWorkItemAuditData.createdTime AS "簽核時間"
        ,CASE 
            WHEN oldAssigneeName <> reassignmentRequester
                THEN CAST(comments AS NVARCHAR(MAX)) + '(' + reassignmentRequester + ')'
            ELSE CAST(comments AS NVARCHAR(MAX))
            END AS "簽核意見"
        ,WorkItem.workItemName AS "關卡名稱"
        ,'已轉派' AS "狀態"
    FROM ReassignWorkItemAuditData
    INNER JOIN ProcessInstance
        ON ProcessInstance.OID = ReassignWorkItemAuditData.currentProcessInstanceOID
    INNER JOIN LocalRelevantData
        ON LocalRelevantData.containerOID = ProcessInstance.contextOID
    INNER JOIN FormInstance
        ON FormInstance.OID = LocalRelevantData.valueOID
    INNER JOIN WorkItem
        ON WorkItem.OID = ReassignWorkItemAuditData.sourceOID
    WHERE ProcessInstance.processDefinitionId = @processDefinitionId
        AND FormInstance.serialNumber = @formSerialNumber
    ) AS History
ORDER BY CASE 
        WHEN 簽核時間 IS NOT NULL
            THEN 簽核時間
        ELSE '9999-12-31 23:59:59.000'
        END /**未處理因無簽核時間,以最大值時間排序才正常*/
    ,建立時間;
```
