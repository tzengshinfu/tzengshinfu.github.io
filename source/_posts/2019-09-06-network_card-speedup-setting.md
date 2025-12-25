---
layout: post
title: 優化主機效能設定
date: 2019-09-06 14:45:00
---
網卡進階建議選項:  
Large Send Offload V2 (IPv4)→Disabled  
Large Send Offload V2 (IPv6)→Disabled  
IPv4 TSO Offload→Disabled  
IPv4 Checksum Offload→Disabled  
Offload IP Options→Disabled  
Offload tagged traffic→Disabled  
Offload TCP Options→Disabled  
TCP Checksum Offload (IPv4)→Disabled  
TCP Checksum Offload (IPv6)→Disabled  
UDP Checksum Offload (IPv4)→Disabled  
UDP Checksum Offload (IPv6)→Disabled  
如果有的話  
Recv Segment Coalescing(IPV4)→Disabled  
Recv Segment Coalescing(IPV6)→Disabled  
Large Receive Offload(IPV4)→Disabled  
Large Receive Offload(IPV6)→Disabled  
  
參考來源:  
 [https://support.rackspace.com/how-to/disabling-tcp-offloading-in-windows-server-2012/](https://www.blogger.com/# "https://www.blogger.com/#")  
 [http://lifeofageekadmin.com/network-performance-vmxnet3-windows-server-2012-r2/](https://www.blogger.com/# "https://www.blogger.com/#")  
 [http://www.peerwisdom.org/2013/04/03/large-send-offload-and-network-performance/](https://www.blogger.com/# "https://www.blogger.com/#")  
   
  
   
設定電源管理:平衡→高效能  
   
 參考來源:  
 [https://codeday.me/bug/20181119/396266.html](https://www.blogger.com/# "https://www.blogger.com/#")  
 [https://dotblogs.com.tw/jamesfu/2012/12/18/powercfg](https://www.blogger.com/# "https://www.blogger.com/#")  
 [https://www.netadmin.com.tw/netadmin/zh-tw/technology/A034BD3916454F388D9F03C9F1190FF3?page=3](https://www.blogger.com/# "https://www.blogger.com/#")  
