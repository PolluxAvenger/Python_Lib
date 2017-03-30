# coding=utf-8

import IPy

#
print(IPy.IP('10.0.0.0/8').version())
print(IPy.IP('::1').version())

#
ip = IPy.IP('192.168.1.20')
reverse_name = ip.reverseNames()
address_type = ip.iptype()
address_int = ip.int()
address_hex = ip.strHex()
address_bin = ip.strBin()
