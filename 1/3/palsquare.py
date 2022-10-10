"""
ID: gohit.y1
LANG: PYTHON3
TASK: palsquare
"""

import sys
import math
import functools as ft
from functools import partial as par
import random as rnd

# g(f(x)) -> F(x, f, g...)
# g(f([x1, x2...])) -> FF([x1, x2...], f, g...)
def F(*z):
    z = list(z)
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
# f(x1, x2..., y1, y2...) -> fyx(f, y1, y2...)(x1, x2...)
fyx = lambda f, *x: lambda *y: f(*y, *x)

fin = open("palsquare.in", 'r')
fout = open("palsquare.out", 'w')

n = int(fin.readline())
def convertBase(x, n):
    s = ''
    digit = lambda x: str(x) if x < 10 else chr(55 + x)
    while x >= n:
        s = digit(x % n) + s
        x //= n
    s = digit(x) + s
    return s
def checkPAL(x):
    flag = True
    for i in range(len(x) // 2 + 1):
        if x[i] != x[-i - 1]:
            flag = False
    return flag
for i in range(1, 301):
    j = convertBase(i ** 2, n)
    if checkPAL(j):
        fout.write(convertBase(i, n) + ' ' + j + '\n')
fout.close()

