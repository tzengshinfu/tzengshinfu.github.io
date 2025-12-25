---
layout: post
title: EFCore Scaffold-DbContext語法(PMC)
date: 2022-06-21 15:05:00
tags:
- entity framework
---

```
Scaffold-DbContext "連線字串" Microsoft.EntityFrameworkCore.SqlServer(Database Provider名稱) -ContextDir Models\Database(Database class[DbContext]路徑) -OutputDir Models\Database\Tables(Table classes[DbSet]路徑) -ContextNamespace Models.Database(Database class[DbContext]命名空間) -Namespace Models.Database.Tables(Table classes[DbSet]命名空間) -Force -UseDatabaseNames -DataAnnotations -NoPluralize(不要複數化) -StartupProject "專案名稱"
```
