---
layout: post
title: Linux無法啟動Eclipse
date: 2023-09-20 15:15:00
tags:
- eclipse
- linux
---

命令列顯示錯誤

SWT OS.java Error: Failed to load swt-pi3, loading swt-pi4 as fallback.

Eclipse:

An error has occurred. See the log file

/mnt/d/eclipse/configuration/xxxxxxxxxxxxx.log.

Log內容為

java.lang.UnsatisfiedLinkError: Could not load SWT library. Reasons:   
 no swt-pi4-gtk-4962r3 in java.library.path: /usr/java/packages/lib:/usr/lib64:/lib64:/lib:/usr/lib  
 no swt-pi4-gtk in java.library.path: /usr/java/packages/lib:/usr/lib64:/lib64:/lib:/usr/lib  
 no swt-pi4 in java.library.path: /usr/java/packages/lib:/usr/lib64:/lib64:/lib:/usr/lib  
 Can't load library: /root/.swt/lib/linux/x86\_64/libswt-pi4-gtk-4962r3.so  
 Can't load library: /root/.swt/lib/linux/x86\_64/libswt-pi4-gtk.so  
 Can't load library: /root/.swt/lib/linux/x86\_64/libswt-pi4.so

解法：

安裝libswt-gtk-4-java元件(sudo apt install libswt-gtk-4-java)

參考來源：[Issue after installing openxava - can't locate gtk3-3.22.30-5.el7.x86\_64](https://sourceforge.net/p/openxava/discussion/419690/thread/bf34a4c810/#21bf "https://sourceforge.net/p/openxava/discussion/419690/thread/bf34a4c810/#21bf")
