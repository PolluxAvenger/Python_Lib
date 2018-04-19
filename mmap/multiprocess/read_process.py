# coding=utf-8

import os
import time
import mmap

filename = 'file'

fd = os.open(filename, os.O_RDONLY)
buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ)

i = 0

while 1:
    buf.seek(0)
    i = int(buf.readline())
    print i
    time.sleep(3)

buf.close()
os.close(fd)