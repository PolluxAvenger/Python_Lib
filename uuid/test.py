# coding=utf-8

import uuid

'''
RFC 4211 定义了一个用于创建对应资源的通用唯一标识符，该标识符是去中心化的
UUID 长 128 位，可以生成可以保证时间和空间唯一性的序列
被用于需要辨别文档、主机、应用客户端或其他唯一性的情况
规范中有三种主要的算法：使用 IEEE 802 MAC 地址唯一性；使用伪随机数；使用知名字符串结合加密哈希
所有情况下的种子值都会和系统时钟、时钟序列值结合起来，保证即使时钟被倒回也能保持唯一性
'''

print(hex(uuid.getnode()))
print('如果主机拥有多块网卡可能返回任意一个值')

id1 = uuid.uuid1()
print('uuid3为:' + str(id1))

'''
UUID 的全部五种算法：
uuid1()——基于时间戳。由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。
         该函数有两个参数, 如果 node 参数未指定, 系统将会自动调用 getnode() 函数来获取主机的硬件地址. 如果 clock_seq  参数未指定系统会使用一个随机产生的14位序列号来代替.
uuid2()——基于分布式计算环境DCE（Python中没有这个函数）。算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。实际中很少用到该方法。
uuid3()——基于名字的MD5散列值。通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
uuid4()——基于随机数。由伪随机数得到，有一定的重复概率，该概率可以计算出来。
uuid5()——基于名字的SHA-1散列值。算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法。
'''

id3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'www.baidu.com')
id4 = uuid.uuid4()
id5 = uuid.uuid5(uuid.NAMESPACE_DNS, 'www.163.com')
print('uuid3为:' + str(id3))
print('uuid4为:' + str(id4))
print('uuid5为:' + str(id5))

uuid_object = uuid.UUID('5ba3009e-8f59-11e6-98b5-dc0ea1e130b2')
print('字符串转换成对象为:' + str(uuid_object))
