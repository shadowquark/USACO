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
    z = list(z)
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

sys.setrecursionlimit(10000)
def quicksort(l, r):
    if l > r:
        return
    i, j, x = l, r, a[(l + r) // 2]
    while (i <= j):
        while (i < r and a[i] < x):
            i += 1
        while (l < j and a[j] > x):
            j -= 1
        if i <= j:
            a[i], a[j], b[i], b[j], i, j = a[j], a[i], b[j], b[i], i + 1, j - 1
        if i < r:
            quicksort(i, r)
        if j > l:
            quicksort(l, j)
quicksort(0, n - 1)
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

