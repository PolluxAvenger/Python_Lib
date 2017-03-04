# coding=utf-8

import pycurl

c = pycurl.Curl() #创建一个curl对象
c.getinfo(pycurl.HTTP_CODE) #返回的HTTP状态码
c.getinfo(pycurl.TOTAL_TIME) #传输结束所消耗的总时间
c.getinfo(pycurl.NAMELOOKUP_TIME) #DNS解析所消耗的时间
c.getinfo(pycurl.CONNECT_TIME) #建立连接所消耗的时间
c.getinfo(pycurl.PRETRANSFER_TIME) #从建立连接到准备传输所消耗的时间
c.getinfo(pycurl.STARTTRANSFER_TIME) #从建立连接到传输开始消耗的时间
c.getinfo(pycurl.REDIRECT_TIME) #重定向所消耗的时间
c.getinfo(pycurl.SIZE_UPLOAD) #上传数据包大小
c.getinfo(pycurl.SIZE_DOWNLOAD) #下载数据包大小
c.getinfo(pycurl.SPEED_DOWNLOAD) #平均下载速度
c.getinfo(pycurl.SPEED_UPLOAD) #平均上传速度
c.getinfo(pycurl.HEADER_SIZE) #HTTP头部大小
