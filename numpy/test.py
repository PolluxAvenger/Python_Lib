import numpy as np
a = np.array([1, 2, 3])
# 查看 ndarray 的数据类型
print(a.dtype)
# 数组的维度
print(a.ndim)
# 数组长度
print(a.size)
# 数组的型
print(a.shape)

arr = np.arange(12).reshape((3, 4))
slice_one = arr[0:2, 1:3]
print(slice_one)
