---
layout: post
title: C# FileSystemWatcher Changed會偵測2次的解決方式
date: 2021-09-15 14:52:00
tags:
- c#
---

namespace FileSystemWatcherTest {

class Program {

private static ConcurrentDictionary<string, DateTime> dic = new ConcurrentDictionary<string, DateTime>();

static void Main(string[] args) {

var watcher = new FileSystemWatcher {

// 設定要監看的資料夾

Path = @"監看路徑",

// 設定要監看的變更類型(修改=LastWrite/新增&刪除=FileName/更名=Attributes)

NotifyFilter = NotifyFilters.LastWrite | NotifyFilters.FileName | NotifyFilters.Attributes,

// 設定要監看的檔案類型

Filter = "\*.txt",

// 設定是否監看子資料夾

IncludeSubdirectories = true,

// 設定是否啟動元件，必須要設定為 true，否則監看事件是不會被觸發

EnableRaisingEvents = true

};

  

// 設定監看事件對應的處理邏輯

watcher.Changed += new FileSystemEventHandler(OnChanged);

watcher.Created += new FileSystemEventHandler(OnCreated);

watcher.Deleted += new FileSystemEventHandler(OnDeleted);

  

Console.ReadLine();

}

  

private static void OnDeleted(object sender, FileSystemEventArgs e) {

//只會偵測1次

Console.WriteLine("檔案變更: " + e.FullPath + " " + e.ChangeType);

}

  

private static void OnCreated(object sender, FileSystemEventArgs e) {

//只會偵測1次

Console.WriteLine("檔案變更: " + e.FullPath + " " + e.ChangeType);

}

  

private static void OnChanged(object source, FileSystemEventArgs e) {

//會偵測2次

#region 以最後更新時間判斷是否重複偵測變更(參考來源 https://www.cnblogs.com/jzywh/archive/2008/07/23/filesystemwatcher.html)

var currentModifyTime = File.GetLastWriteTime(e.FullPath);

var previousModifyTime = new Func<DateTime>(() => {

DateTime funcResult = DateTime.MinValue;

  

dic.TryGetValue(e.FullPath, out funcResult);

return funcResult;

})();

if (currentModifyTime == previousModifyTime) {

return;

}

  

dic.TryRemove(e.FullPath, out previousModifyTime);

dic.TryAdd(e.FullPath, currentModifyTime);

#endregion

  

Console.WriteLine("檔案變更: " + e.FullPath + " " + e.ChangeType);

}

}

}
