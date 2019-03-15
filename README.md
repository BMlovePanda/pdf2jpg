#### 操作系统及环境
环境：Python2.7

操作系统：win10、win7

#### requirement
PyPDF2==1.26.0

filetype==1.0.1

ghostscript==0.6

#### 几个需要注意的地方
1、需要使用ImageMagick以及ghostscripts（gs）；

2、ImageMagick安装版与操作系统版本（32 or 64）对应；

3、gs安装与Python版本对应（32 or 64）；

4、安装完ImageMagick软件后记得要创建一个MAGICK_HOME的系统变量，值就是ImageMagick软件安装之后的软件路径（否则会出现如下错误RuntimeError: python.exe: iCCP: Not recognizing known sRGB profile that has been edited `C:\Users\zhrui\AppData\Local\Temp\magick-8896lsDlpYZUDJWc1' @ warning/png.c/MagickPNGWarningHandler/1832）。
