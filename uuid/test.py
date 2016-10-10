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

u = uuid.uuid1()
print(u)
print(type(u))
print('bytes :', repr(u.bytes))
print('hex :', u.hex)
print('int :', u.int)
print('urn :', u.urn)
print('variant :', u.variant)
print('version :', u.version)
print('fields :', u.fields)
print('\ttime_low : ', u.time_low)
print('\ttime_mid : ', u.time_mid)
print('\ttime_hi_version : ', u.time_hi_version)
print('\tclock_seq_hi_variant: ', u.clock_seq_hi_variant)
print('\tclock_seq_low : ', u.clock_seq_low)
print('\tnode : ', u.node)
print('\ttime : ', u.time)
print('\tclock_seq : ', u.clock_seq)
