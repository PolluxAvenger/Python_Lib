# coding=utf-8

import struct

# 定长打包
a = struct.pack("2I3sI", 12, 34, "abc", 56)
b = struct.unpack("2I3sI", a)