#### 操作系统及环境
环境：Python2.7

操作系统：win10、win7

#### requirement
Wand==0.5.1

#### 需要注意的地方
1、需要使用ImageMagick以及ghostscripts（gs），并且需要安装32bit的；

2、该软件使用Wand而没使用PythonMagick，主要是PM无法调整转换后的图片质量（使用density参数未生效），Wand对CPU要求挺高，这个程序在一些老CPU上执行，可能会导致CPU利用率100%
