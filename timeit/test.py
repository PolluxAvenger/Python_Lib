# coding=utf-8

import timeit

# python -m timeit -s"import mymodele as m" "m.myfunction()" 对某个函数来计时

print(timeit.timeit("x = 2 + 2"))
# timeit 函数会通过多次运行相关代码来提高计时精度，如果先执行的操作影响后面的运行，其结果就并不准确
# 比如运行排序函数，第一排序过后的每次都是已排好的列表，则时间极不精确
