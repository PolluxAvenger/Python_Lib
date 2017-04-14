# coding=utf-8

import pwn
pwn.asm("xor eax,eax")
pwn.asm('xor eax,eax', arch='arm')