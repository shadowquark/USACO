"""
ID: gohit.y1
LANG: PYTHON3
TASK: milk
"""

import sys
import math
import functools as ft
from functools import partial as par
import random as rnd

# g(f(x)) -> F(x, f, g...)
# g(f([x1, x2...])) -> FF([x1, x2...], f, g...)
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
# f(x1, x2..., y1, y2...) -> fyx(f, y1, y2...)(x1, x2...)
fyx = lambda f, *x: lambda *y: f(*y, *x)

fin = open("milk.in", 'r')
fout = open("milk.out", 'w')

m, n = fin.readline()[:-1].split(' ')
m, n = int(m), int(n)
a, b = [], []
for line in fin.readlines():
    temp1, temp2 = line.split(' ')
    temp1, temp2 = int(temp1), int(temp2)
    a.append(temp1)
    b.append(temp2)

def quicksort(l, r, *obj):
    if not l < r:
        return obj
    i, j, x, y = l, r, obj[0][r], obj[1][r]
    while (i < j):
        while (i < j and obj[0][i] <= x):
            i += 1
        obj[0][j], obj[1][j] = obj[0][i], obj[1][i]
        while (i < j and obj[0][j] > x):
            j -= 1
        obj[0][i], obj[1][i] = obj[0][j], obj[1][j]
    obj[0][i], obj[1][i] = x, y
    quicksort(l, i - 1, *obj)
    quicksort(i + 1, r, *obj)
    return obj
def bucketsort():
    obj = [*zip(a, b)]
    if not obj:
        return [], []
    bucket8bit = [[[] for _ in range(256)] for _ in range(4)]
    for x in obj:
        bucket8bit[0][x[0] & 0xff].append(x)
    for bucket in bucket8bit[0]:
        for x in bucket:
            bucket8bit[1][(x[0] & 0xffff) >> 8].append(x)
    for bucket in bucket8bit[1]:
        for x in bucket:
            bucket8bit[2][(x[0] & 0xffffff) >> 16].append(x)
    for bucket in bucket8bit[2]:
        for x in bucket:
            bucket8bit[3][x[0] >> 24].append(x)
    obj = []
    for bucket in bucket8bit[3]:
        for x in bucket:
            obj.append(x)
    obj = [*zip(*obj)]
    return obj
#sys.setrecursionlimit(10000)
#a, b = quicksort(0, n - 1, a, b)
a, b = bucketsort()
tot = 0
for x, y in zip(a, b):
    if m > y:
        tot += x * y
        m -= y
    else:
        tot += x * m
        break
fout.write(str(tot) + '\n')
fout.close()

