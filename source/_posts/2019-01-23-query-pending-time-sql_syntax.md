---
layout: post
title: 查詢線上特定流程流程的待處理關卡擱置時數的SQL語法
date: 2019-01-23 11:44:00
tags:
- easyflow gp
- sql
---

```
SELECT 
    ProcessInstance.serialNumber AS "流程序號" 
    ,ProcessInstance.processInstanceName AS "流程名稱" 
    ,ProcessInstance.subject AS "流程主旨" 
    ,ProcessInstance.createdTime AS "流程建立時間" 
    ,WorkItem.workItemName AS "關卡名稱" 
    ,CASE WHEN Performers.id IS NULL THEN Assignees.id END AS "關卡處理者工號" 
    ,CASE WHEN Performers.userName IS NULL THEN Assignees.userName END AS "關卡處理者姓名" 
    ,CASE WHEN Performers.leaveDate IS NULL THEN '是' ELSE CASE WHEN Assignees.leaveDate IS NULL THEN '是' ELSE '否' END END AS "關卡處理者在職狀態" 
    ,WorkItem.createdTime AS "關卡建立時間" 
    ,DATEDIFF(HOUR, ProcessInstance.createdTime, GETDATE()) AS "未處理時數" 
    ,DATEDIFF(HOUR, ProcessInstance.createdTime, GETDATE()) / 24 AS "未處理天數" 
    ,CASE
        WHEN WorkAssignment.assignmentType = 0 THEN '正常指派'
        WHEN WorkAssignment.assignmentType = 1 THEN '重新指派'
        WHEN WorkAssignment.assignmentType = 2 THEN '退件指派'
     END AS "指派類型" 
FROM WorkItem
INNER JOIN ProcessContext
    ON ProcessContext.OID = WorkItem.contextOID
INNER JOIN ProcessInstance
    ON ProcessInstance.OID = ProcessContext.containerOID
INNER JOIN ParticipantActivityInstance
    ON ParticipantActivityInstance.OID = WorkItem.containerOID
LEFT JOIN WorkAssignment
    ON WorkAssignment.workItemOID = WorkItem.OID
LEFT JOIN Users AS Performers
    ON WorkItem.performerOID = Performers.OID
LEFT JOIN Users AS Assignees
    ON WorkAssignment.assigneeOID = Assignees.OID
WHERE WorkItem.currentState IN (0, 1, 2)
AND ProcessInstance.processDefinitionId = '特定流程定義代號'
ORDER BY WorkItem.createdTime
```
