# -*- coding: utf-8 -*-
import glob,time,shutil,sys,os
from wand.image import Image
reload(sys)
sys.setdefaultencoding('utf-8')
PDF_DIR = os.getcwd()
print 80*'#' + '\n'
file_number = 1
def pdf_to_jpg(PDF_FILE_NAME):  
    JPG_FILE_DIR = PDF_FILE_NAME.split('.')[0] + u'_图片目录'
    #如果图片目录存在，则先删除，再创建空目录，否则直接创建空目录
    if not os.path.exists(JPG_FILE_DIR):
        os.makedirs(JPG_FILE_DIR)
    else:
        shutil.rmtree(JPG_FILE_DIR)    
        os.makedirs(JPG_FILE_DIR)
    #读取pdf文件，分辨率值设置越大，打开文件越慢，可根据自己情况调整
    image_pdf = Image(filename = PDF_FILE_NAME,resolution=300)
    image_jpeg = image_pdf.convert('jpg')
    #print u"[%s]:文件正在转换..." %time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    req_image = []
    #print u"[%s]:该PDF文件有%s页，正在转换，请稍等...\n" %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),len(image_jpeg.sequence))
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpg'))   
    jpg_file_num = 1
    # 遍历req_image,保存为图片文件      
    for img in req_image:
        #print u"[%s]:正在转换第%s页,请稍后." %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),jpg_file_num)
        JPG_FILE_NAME = PDF_FILE_NAME.split('.')[0] + '_' + str(jpg_file_num)+'.jpg'
        ff = open(JPG_FILE_NAME,'wb')
        ff.write(img)
        ff.close()
        shutil.move(JPG_FILE_NAME,JPG_FILE_DIR)
        jpg_file_num += 1
#遍历与脚本程序在同一目录下的pdf文件
def pdf_list():
    pdf_file_list = []
    for files in glob.glob(PDF_DIR + r'/*.pdf'):
        pdf_file_list.append(files)
    print len(pdf_file_list)
    print 80*'#' + '\n'
    return pdf_file_list
#ImageMagick软件会产生大量临时文件，会占用C盘较多空间
def tmp_file_del():
    TMP_DIR = os.environ.get("TMP")
    for tmp_files in glob.glob(TMP_DIR + r'\magick*'):
        try:
            os.remove(tmp_files)
        except:
            continue
if __name__ == "__main__":
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    for PDF_FILE_NAME in pdf_list():
        print "Converting File No.%s\n" %file_number
        PDF_FILE_SIZE = float(os.path.getsize(PDF_FILE_NAME))/float(1024)/float(1024)
        print u"FileSize is :%.2fMB,Please wait......!\n" %PDF_FILE_SIZE
        pdf_to_jpg(PDF_FILE_NAME)
        print u"\nSuccess:File No.%s is done!" %file_number
        file_number += 1
        print 80*'#' + '\n'
    tmp_file_del()
    print u"[%s]:Mission Complete!" %time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print "\npress 'Enter' key to quit.....!"
    raw_input()
