# coding=utf-8

import os
import mmap

filename = 'file'

fd = os.open(filename, os.O_RDWR)
buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)

i = 0

while 1:
    buf.seek(0)
    buf.write(str(i)+"\n")
    i += 1
    raw_input('ENTER')

buf.close()
os.close(fd)