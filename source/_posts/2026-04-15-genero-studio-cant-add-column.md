---
title: GENERO_STUDIO_無法新增欄位
date: 2026-04-15 14:53:12
tags:
- tiptop
---

發現無法刪除元件。  
[![](GeneroStudio_20260415_110602.png)](GeneroStudio_20260415_110602.png)

### 解法

1. 先刪除上層元件(vbox或hbox)，點擊該元件然後再點擊工具列按鈕`Remove the selected Layout`。  
[![](Capture_20260415_144110.png)](Capture_20260415_144110.png)
2. 然後就能刪除元件。
3. 最後要將刪除的上層元件(vbox或hbox)加回去，用Ctrl+點擊選取原本vbox/hbox的所有元件，然後再點擊工具列按鈕`Create horizontal/vertical Layout`。  
[![](GeneroStudio_20260415_144147.png)](GeneroStudio_20260415_144147.png)
