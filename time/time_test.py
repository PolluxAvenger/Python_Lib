# coding=utf-8

import time

print('当前时间是:' + time.ctime())
print('当前的 UTC 时间:' + str(time.gmtime()))
print('当前的本地时间:' + str(time.localtime()))
print('当月的第几天:' + str(time.localtime().tm_mday))