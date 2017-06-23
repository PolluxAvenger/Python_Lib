# coding=utf-8

import datetime


if __name__ == '__main__':
	# Java PHP JS 可以获得到十三位的时间戳，而 Python 默认处理十位
	# 一个 13 位的时间戳，用 Python 转换成 string 型
    timestamp_with_ms = 1493126127995
    dt = datetime.datetime.fromtimestamp(timestamp_with_ms / 1000)
    formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(formatted_time)
