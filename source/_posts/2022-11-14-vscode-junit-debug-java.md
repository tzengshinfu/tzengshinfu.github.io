---
layout: post
title: VSCode使用JUnit對Java程式除錯並以Fiddler Classic擷取封包內容
date: 2022-11-14 20:26:00
tags:
- fiddler classic
- java
- visual studio code
---

 1.VSCode該Workspace的settings.json加上

```
"java.debug.settings.vmArgs": "-Dhttp.proxyHost=<Fiddler所在主機位址> -Dhttp.proxyPort=<Fiddler開啟Port號> -Dhttps.proxyHost=<Fiddler所在主機位址> -Dhttps.proxyPort=<Fiddler開啟Port號>",
"java.test.config": [{
	"name": "fiddler", // 測試時啟用Fiddler擷取封包的Profile名稱
	"vmArgs": [
		"-Dhttp.proxyHost=<Fiddler所在主機位址>",
		"-Dhttp.proxyPort=<Fiddler開啟Port號>",
		"-Dhttps.proxyHost=<Fiddler所在主機位址>",
		"-Dhttps.proxyPort=<Fiddler開啟Port號>"
	]
},{
	"name":"direct" // 測試時不啟用Fiddler擷取封包的Profile名稱
}
],
"java.test.defaultConfig": "fiddler", // 測試時啟用Fiddler擷取封包的Profile名稱
"testing.defaultGutterClickAction": "debug", //測試按鈕行為改成debug
```

 2.Fiddler Classic>Tools>Options>HTTPS

[![](img-20221114-201247.png)](img-20221114-201247.png )

[![](img-20221114-165229.png)](img-20221114-165229.png )

 3.Fiddler Classic>Tools>Options>Connections

[![](img-20221114-201301.png)](img-20221114-201301.png )

4.擷取成功畫面如下

[![](img-20221114-201430.png)](img-20221114-201430.png )

  

