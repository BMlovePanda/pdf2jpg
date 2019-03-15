# -*- coding: cp936 -*-
'''
    程序名:pdf_2_jpg.py
    功能：将PDF文件转化成单张图片
    作者：Paulownia    
    日期：2018.06.25
'''
import sys,os,glob,time,shutil,filetype
#import PyPDF2,PythonMagick,ghostscript
import PyPDF2,PythonMagick
reload(sys)
sys.setdefaultencoding('gb2312')
PDF_DIR = os.getcwd()
README = u'''此程序用于将pdf文件转换为单个图片文件;\n
作者：张大嘴;\n
说明：此程序对中文名称的pdf文件支持不够友好，建议将pdf文件名称修改为数字或英文！\n
'''
print README
print u"[%s]:程序开始运行!" %time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# 将pdf文件转为jpg图片文件
def pdf_to_jpg(PDF_FILE_NAME):  
    pdf_im = PyPDF2.PdfFileReader(file(PDF_FILE_NAME, "rb"))  
    PDF_PAGES = pdf_im.getNumPages()  
    print u"[%s]:该PDF文件共有%s页，正在转换，请稍等...\n" %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),PDF_PAGES)
    JPG_FILE_DIR = PDF_FILE_NAME.split('.')[0] + u'_图片目录'
    if not os.path.exists(JPG_FILE_DIR):
        os.makedirs(JPG_FILE_DIR)
    for jpg_file_num in range(PDF_PAGES):
        print u"[%s]:正在转换第%s页,剩余%s页,请稍后." %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),jpg_file_num+1,(PDF_PAGES-jpg_file_num-1))
        JPG_FILE_NAME = PDF_FILE_NAME.split('.')[0] + '_' + str(jpg_file_num+1)+'.jpg'
        im = PythonMagick.Image(PDF_FILE_NAME + '[' + str(jpg_file_num) +']')  
        im.density('300')  
        im.write(JPG_FILE_NAME)
        shutil.move(JPG_FILE_NAME,JPG_FILE_DIR) 
    print '\n' + 50*'-' + '\n'
#遍历与脚本程序在同一目录下的pdf文件
def pdf_list():
    pdf_file_list = []
    for files in glob.glob(PDF_DIR + r'/*.pdf'):
        if files:
            pdf_file_list.append(files)
        else:
            break
    return pdf_file_list
if __name__ == "__main__":
    for PDF_FILE_NAME in pdf_list():
        pdf_to_jpg(PDF_FILE_NAME)
    print u"[%s]:转换完成!" %time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    raw_input()
