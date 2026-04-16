---
title: 設定工作排程器的工作2開始於工作1的結束
date: 2026-04-16 09:39:23
tags:
- windows
---

## 情境

想在工作站解除鎖定時執行數個特定工作，其中工作2必須在工作1完成後執行，  
已設定延遲但因工作1執行時間不確定而造成工作2啟動失敗。

工作1 = FinishThunderbird  
工作2 = StartThunderbird  
[![](Capture_20260416_095923.png)](Capture_20260416_095923.png)

## 作法

1. 在工作排程器的*歷程記錄*取得工作1的資訊。  
[![](mmc_20260416_084554.png)](mmc_20260416_084554.png)

XML格式如下:
```xml
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
    - <System>
        <Provider Name="Microsoft-Windows-TaskScheduler" Guid="{de7b24ea-73c8-4a09-985d-5bdadcfa9017}" />
        <EventID>102</EventID>
        <Version>0</Version>
        <Level>4</Level>
        <Task>102</Task>
        <Opcode>2</Opcode>
        <Keywords>0x8000000000000001</Keywords>
        <TimeCreated SystemTime="2026-04-16T00:17:11.8174463Z" />
        <EventRecordID>813268</EventRecordID>
        <Correlation ActivityID="{aaa091d3-94d9-4a25-863f-e6b06aea9901}" />
        <Execution ProcessID="3648" ThreadID="36188" />
        <Channel>Microsoft-Windows-TaskScheduler/Operational</Channel>
        <Computer>localhost</Computer>
        <Security UserID="S-1-5-18" />
    </System>
    - <EventData Name="TaskSuccessEvent">
        <Data Name="TaskName">\Localhost\FinishThunderbird</Data>
        <Data Name="UserContext">user</Data>
        <Data Name="InstanceId">{aaa091d3-94d9-4a25-863f-e6b06aea9901}</Data>
    </EventData>
</Event>
```

2. 編輯工作2的*觸發程序*為`事件發生時`，*設定*為`自訂`。  
[![](mmc_20260416_085525.png)](mmc_20260416_085525.png)

3. 事件篩選器，選取*依來源*，*事件來源*選擇`TaskScheduler`。  
[![](mmc_20260416_090552.png)](mmc_20260416_090552.png)

4. 上方的*事件記錄檔*只選`Microsoft-Windows-TaskScheduler/Operational`。  
[![](mmc_20260416_090139.png)](mmc_20260416_090139.png)

5. 點擊上方的*XML*頁籤，點擊下方的*手動編輯查詢*，再點擊對話框的`是(Y)`。  
[![](mmc_20260416_090242.png)](mmc_20260416_090242.png)

6. 將XML資料替換成以下模版文字：  
```xml
<QueryList>
    <Query Id="0" Path="Microsoft-Windows-TaskScheduler/Operational">
        <Select Path="Microsoft-Windows-TaskScheduler/Operational">*[EventData[@Name='TaskSuccessEvent'][Data[@Name='TaskName']='Task1's name']]</Select>
    </Query>
</QueryList>
```

7. 再將`Task1's name`置換成實際工作名稱。  
[![](Code_20260416_102841.png)](Code_20260416_102841.png)

8. 最後再儲存工作2變更即可。  

參考來源：[How to daisy chain tasks in the Windows Task Scheduler to run consecutively?](https://superuser.com/a/1735734)