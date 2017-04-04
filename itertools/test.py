# coding=utf-8

import itertools

# 累加
x = itertools.accumulate(range(10))
print(list(x))

# 联结
x = itertools.chain(range(3), range(4), [1, 2, 3])
print(list(x))

# 迭代器内指定元素个数不重复的所有组合
x = itertools.combinations(range(5), 4)
print(list(x))

# 迭代器内指定元素个数可重复的所有组合
x = itertools.combinations_with_replacement('ABCD', 2)
print(list(x))

# 按照真值表筛选元素
x = itertools.compress(range(5), (True, False, True, True, False))
print(list(x))

# 计数器，起始位置与步长
x = itertools.count(start=30, step=-1)
# 丈量切片，后面三个参数指定小标尺，总共多长，步长多少
print(list(itertools.islice(x, 0, 10, 2)))

# 循环的迭代器
x = itertools.cycle('ABC')
print(list(itertools.islice(x, 0, 10, 1)))

# 按照真值函数丢弃掉列表和迭代器前面的元素
x = itertools.dropwhile(lambda e: e < 5, range(10))
print(list(x))

# 与 dropwhile 函数相反，保留元素直至真值函数值
x = itertools.takewhile(lambda e: e < 5, range(10))
print(list(x))


# 保留对应真值为 False 的元素
x = itertools.filterfalse(lambda e: e < 5, (1, 5, 3, 6, 9, 4))
print(list(x))

# 按照分组函数的真值状态对元素进行分组
x = itertools.groupby(range(10), lambda x: x < 6 or x > 8)
for condition, numbers in x:
    print(condition, list(numbers))

# 产生指定数目的元素的所有排列(顺序有关)
x = itertools.permutations(range(3), 3)
print(list(x))

# 产生多个列表和迭代器的(积)
x = itertools.product('ABC', range(3))
print(list(x))

# 生成一个拥有指定数目元素的迭代器
x = itertools.repeat(0, 5)
print(list(x))

# 类似 map
x = itertools.starmap(str.islower, 'aBCDefGhI')
print(list(x))

# 生成指定数目的迭代器
x = itertools.tee(range(10), 2)
for letters in x:
    print(list(letters))

# 基于给定的迭代器输出指定个数的迭代器
x = itertools.tee(range(10), 2)
for letters in x:
    print(list(letters))

# 类似于 zip，以较长的列表和迭代器的长度为准
x = itertools.zip_longest(range(3), range(5))
print(list(x))
