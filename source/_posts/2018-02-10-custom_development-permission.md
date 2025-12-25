---
layout: post
title: "[構想]自主開發系統 - 權限設計"
date: 2018-02-10 12:05:00
tags:
- 自主系統開發
---

權限設計
====

### (參考Apache Shiro權限功能)

1.管理者

| 角色 | 權限 |
| --- | --- |
| department1:role1 | \* |

說明:  
在demartment1的role1可使用任何功能。

2.針對各別功能設定權限

| 角色 | 權限 |
| --- | --- |
| department2:role2 | function1:\*;function2:add,view |

說明:  
在demartment2的role2 擁有function1的全部權限(新增/修改/刪除/觀看..等); 擁有function2的新增及觀看權限。

3.針對所有功能設定權限

| 角色 | 權限 |
| --- | --- |
| department3:role3 | \*:view |

說明:  
在demartment3的role3在所有function都擁有觀看權限。

4.針對所有角色設定權限

| 角色 | 權限 |
| --- | --- |
| \* | function3:view |

說明: 所有role都擁有function3的觀看權限。
