# coding=utf-8

import datetime

print('UTC 时间:', datetime.datetime.utcnow())

today = datetime.date.today()
print('日期:', today)
print('日期元组:', today.timetuple())
print('年份:', today.year)
print('月份:', today.month)
print('日:', today.day)

d1 = datetime.date(2008, 3, 12)
print('修改年份前:', d1)
d2 = d1.replace(year=2009)
print('修改年份后:', d2)

d1 = datetime.date.today()
print('修改日期前:', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print('修改日期后:', d2)
print('判断修改前大？:', d1 > d2)

format = "%a %b %d %H:%M:%S %Y"
today = datetime.datetime.today()
print('格式修改前标准时间:', today)
s = today.strftime(format)
print('修改时间格式后:', s)
d = datetime.datetime.strptime(s, format)
print('将修改后转给实例对象:', d.strftime(format))
