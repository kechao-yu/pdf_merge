#!/usr/bin/env python
# coding: utf-8


# 引入包
from PyPDF2 import PdfFileReader,PdfFileWriter

import os  

import datetime


# 读取目标pdf文件,并保存到列表
def file_name(file_dir):   
    pdf_file_list = []
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.pdf':  
                pdf_file_list.append(os.path.join(root, file))
    return pdf_file_list


# 合并pdf文件,并输出
def merge_pdfs(paths,output):
    pdf_writer = PdfFileWriter()
    
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))
        # Write out the merged PDF
        with open(output, 'wb') as out:
            pdf_writer.write(out)


if __name__ == '__main__':
    time_str = str(datetime.datetime.now())[:10]
    paths = file_name('../res/')
    target_file_name = '../res/合并'+time_str+'.pdf'
    merge_pdfs(paths, output=target_file_name)






