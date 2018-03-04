# coding=utf-8

import inspect

# 检查是否为模块
inspect.ismodule(inspect)
# 检查是否为函数
inspect.isfunction(len)
# 得到 dcostring
inspect.getdoc(len)
# 得到模块的全部函数
inspect.getmembers(inspect, inspect.isfunction)