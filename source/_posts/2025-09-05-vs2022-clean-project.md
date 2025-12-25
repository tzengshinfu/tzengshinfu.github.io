---
layout: post
title: Visual Studio 2022 清除專案同時清空bin/obj資料夾
date: 2025-09-05 16:54:00
tags:
- visual studio 2022
---

 在專案.csproj檔新增

```
<Project>
```

...

<!-- #region 清理 bin 和 obj 資料夾 -->

  <Target Name="CleanBinObjFolders" AfterTargets="Clean">

<!-- Remove obj folder -->

    <RemoveDir Directories="$(BaseIntermediateOutputPath)" />

<!-- Remove bin folder -->

    <RemoveDir Directories="$(BaseOutputPath)" />

  </Target>

<!-- #endregion -->

</Project>

參考來源：[How to fully clean bin and obj folders within Visual Studio?](https://stackoverflow.com/a/12206011 "https://stackoverflow.com/a/12206011")
