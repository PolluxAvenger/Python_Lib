# coding=utf-8

import os
import sys
from PIL import Image

im = Image.open('1.jpg')
print(im.format, im.size, im.mode)
im.show()

def format(infile, format):
    # 第一个参数输入要转换的文件，第二个参数是转化文件的格式
    f, e = os.path.splitext(infile)
    print('您要将格式从' + e + '转换为' + format)
    outfile = f + format
    im.save(outfile)
    it = Image.open(outfile)
    print(it.format, it.size, it.mode)

format('1.jpg', '.png')
