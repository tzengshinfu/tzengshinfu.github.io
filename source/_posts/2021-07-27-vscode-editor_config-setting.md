---
layout: post
title: VS Code使用EditorConfig設定
date: 2021-07-27 11:35:00
tags:
- visual studio code
---

[![](Image_20210727105733.png)](Image_20210727105733.png )

  

1.新增.editorconfig及omnisharp.json 2個檔案。

2.omnisharp.json內容如下：

```
{
    "RoslynExtensionsOptions": {
        "enableAnalyzersSupport": true,
        "enableMsBuildLoadProjectsOnDemand": true
    },
    "FormattingOptions": {
        "enableEditorConfigSupport": true
    }
}
```

```
3..editorconfig內容如下：
```

```

```

```
#### C# Formatting Rules ####

  


# New line preferences



csharp_new_line_before_catch = true



csharp_new_line_before_else = true



csharp_new_line_before_finally = true



csharp_new_line_before_members_in_anonymous_types = true



csharp_new_line_before_members_in_object_initializers = true



csharp_new_line_before_open_brace = none



csharp_new_line_between_query_expression_clauses = true
```

