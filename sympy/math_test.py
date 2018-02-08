# coding=utf-8

from sympy import *

x = Symbol('x')
y = Symbol('y')

print(solve([3 * y + 5 * y - 1, 2 * x - 3 * y - 1],[x,y]))

