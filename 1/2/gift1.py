"""
ID: gohit.y1
LANG: PYTHON3
TASK: gift1
"""

import math
import functools as ft
import random as rnd
import sys

# g(f(x)) -> F([x, f, g, ...])
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fin = open ("gift1.in", 'r')
fout = open ("gift1.out", 'w')

m = int(fin.readline())
names = [fin.readline()[:-1] for _ in range(m)]
names = {i: 0 for i in names}
while 1:
    name = fin.readline()[:-1]
    if name == '':
        break
    value, share = [int(i) for i in fin.readline().split(' ')]
    if not share:
        continue
    names[name] += value % share - value
    for _ in range(share):
        name = fin.readline()[:-1]
        names[name] += value // share
for name in names:
    fout.write(f"{name} {names[name]}\n")

fout.close()

