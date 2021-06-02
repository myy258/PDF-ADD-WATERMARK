# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:00:38 2021

@author: Yiyu.Mo
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from PyPDF4 import PdfFileWriter, PdfFileReader
import os
import requests

class PDF_Add_Watermark:
    
    def __init__(self):
        pass
        
     # 将png水印文件制作成pdf文件
    def create_watermark(self,watermark_png,f_pdf,mark_type):
        # 参数1：水印图片
        # 参数2：生成水印pdf文件
        # 参数3：水印类型
        
        w_pdf = 25*cm
        h_pdf = 30*cm
              
        # 创建空白pdf                                                                            
        c = canvas.Canvas(f_pdf, pagesize = (w_pdf, h_pdf))
       
        # 设置透明度
        c.setFillAlpha(0.4)
        
        if mark_type == 1:
            # 倾斜20度
            c.rotate(20)            
            # 在页面上批量打上水印
            for i in range(5):
                for j in range(10):
                    x=12*(i-1)
                    y=6*(j-2)
                    c.drawImage(watermark_png, x*cm, y*cm, 6.5*cm, 3*cm, mask='auto')
            c.save()
            
        elif mark_type == 2:
            # 倾斜0度
            c.rotate(0)          
            # 在页面上批量打上水印
            for i in range(5):
                for j in range(10):
                    x=12*(i-1)
                    y=6*(j-2)
                    c.drawImage(watermark_png, x*cm, y*cm, 6.5*cm, 3*cm, mask='auto')
            c.save()
            
        elif mark_type == 3:
            # 倾斜0度
            c.rotate(-20)                   
            # 在页面上批量打上水印
            for i in range(5):
                for j in range(10):
                    x=12*(i-1)
                    y=6*(j-2)
                    c.drawImage(watermark_png, x*cm, y*cm, 6.5*cm, 3*cm, mask='auto')
            c.save()
        
        else:
            # 倾斜0度
            c.rotate(0)                 
            # 在页面上批量打上水印
            for i in range(5):
                for j in range(10):
                    x=12*(i-1)
                    y=6*(j-2)
                    c.drawImage(watermark_png, x*cm, y*cm, 6.5*cm, 3*cm, mask='auto')
            c.save()
            
        
    # pdf加水印
    def add_watermark(self,input_pdf,output_pdf,f_pdf,temp_file):
        # 参数1：输入pdf（二进制文件或者网址链接）
        # 参数2：输出pdf已添加水印文件
        # 参数3：水印pdf文件
        # 参数4：临时生成的文件（最后会自动清除）
        
        # 获取水印pdf
        watermark_obj = PdfFileReader(f_pdf)
        watermark_page = watermark_obj.getPage(0)
        
        # 判断是否为网址链接
        if 'http' in input_pdf:
            
            res = requests.get(input_pdf)
            with open(temp_file, 'wb') as f:
                f.write(res.content)
        
            # 获取源pdf
            pdf_reader = PdfFileReader(temp_file)
            pdf_writer = PdfFileWriter()
            
            # 逐页添加水印
            for page in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page)
                page.mergePage(watermark_page)
                pdf_writer.addPage(page)
            
            # 输出添加水印的pdf
            with open(output_pdf, 'wb') as out:    
                pdf_writer.write(out)    
                
        else:
                                 
            # 模拟传入二进制文件
            datafile = open(input_pdf,'rb')
            file = open(temp_file,'wb')
            for line in datafile:
                file.write(line)
            file.close()
                  
            # 获取源pdf
            pdf_reader = PdfFileReader(temp_file)
            pdf_writer = PdfFileWriter()
            
            # 逐页添加水印
            for page in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page)
                page.mergePage(watermark_page)
                pdf_writer.addPage(page)
            
            # 输出添加水印的pdf
            with open(output_pdf, 'wb') as out:    
                pdf_writer.write(out)
                
        #删除临时文件
        os.remove(f_pdf)
        os.remove(temp_file)

