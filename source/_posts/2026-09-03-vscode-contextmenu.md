---
title: VSCode用winget安裝時不會註冊右鍵選單
date: 2026-09-03 20:47:50
tags:
- visual studio code
---
情況：  
用`winget install --id Microsoft.VisualStudioCode`或`winget import --import-file {包括VSCode之前匯出的APP清單.json}`  
並不會註冊右鍵選單。

解法：
加上以下參數
`winget install Microsoft.VisualStudioCode --override "/verysilent /suppressmsgboxes /mergetasks='!runcode,addcontextmenufiles,addcontextmenufolders,associatewithfiles,addtopath'"`
如果是`{包括VSCode之前匯出的APP清單.json}`，
則加上屬性"InitialOverrideArguments"
```json
{
    ...........
	"Sources" :
	[
		{
			"Packages" :
			[
                ...........
				{
					"PackageIdentifier" : "Microsoft.VisualStudioCode",
					"InitialOverrideArguments": "/verysilent /suppressmsgboxes /mergetasks='!runcode,addcontextmenufiles,addcontextmenufolders,associatewithfiles,addtopath'"
				},
                ...........
			]
		}
	]
}
```

參考來源：  
[[Package Issue]: Microsoft.VisualStudioCode missing "Open with Code" actions in Windows Explorer file context menu](https://github.com/microsoft/winget-pkgs/issues/106091#issuecomment-1546713539)
