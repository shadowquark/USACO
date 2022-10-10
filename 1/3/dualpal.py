"""
ID: gohit.y1
LANG: PYTHON3
TASK: dualpal
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

fin = open("dualpal.in", 'r')
fout = open("dualpal.out", 'w')

n, s = fin.readline()[:-1].split(' ')
n, s = int(n), int(s)

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

while (n):
    score = 0
    s += 1
    for i in range(2, 11):
        if checkPAL(convertBase(s, i)):
            score += 1
    if score > 1:
        n -= 1
        fout.write(str(s) + '\n')
fout.close()

