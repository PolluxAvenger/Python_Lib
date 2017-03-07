# coding=utf-8

from scapy.all import *

data = 'University of Texas at San Antonio'
a = IP(dst='10.5.100.50')/TCP()/Raw(load=data)
sendp(a)