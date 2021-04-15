"""
ID: gohit.y1
LANG: PYTHON3
TASK: ride
"""

import math
import functools as ft
import random as rnd

# g(f(x)) -> F([x, f, g, ...])
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fin = open("ride.in", 'r')
fout = open("ride.out", 'w')

temp = fin.readline()
output1 = [(ord(i) - 64) for i in temp[:-1]]
output1 = ft.reduce(lambda x, y: x * y, output1) % 47
temp = fin.readline()
output2 = [(ord(i) - 64) for i in temp[:-1]]
output2 = ft.reduce(lambda x, y: x * y, output2) % 47

if output1 - output2:
    fout.write("STAY\n")
else:
    fout.write("GO\n")

fout.close()

