# coding=utf-8

import os
from PIL import Image


def save_image(gif_file):
    save_dir = gif_file[:-4] + '/'
    os.mkdir(save_dir)
    gif_imgage = Image.open(gif_file)

    try:
        while True:
            current_image = gif_imgage.tell()
            gif_imgage.save(save_dir + str(current_image) + '.png')
            gif_imgage.seek(current_image + 1)
    except:
        pass


if __name__=='__main__':
    gif_file = 'test.gif'
    save_image(gif_file)
