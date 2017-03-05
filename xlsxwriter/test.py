# coding=utf-8

import xlsxwriter
# 官方文档地址：http://xlsxwriter.readthedocs.io/contents.html

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()
