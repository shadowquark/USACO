"""
ID: gohit.y1
LANG: PYTHON3
TASK: friday
"""

import math
import functools as ft
import random as rnd

# g(f(x)) -> F([x, f, g, ...])
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fin = open("friday.in", 'r')
fout = open("friday.out", 'w')

n = int(fin.readline())
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day13 = lambda z: [13] + [
    ft.reduce(lambda x, y: x + y, z[:i + 1]) + 13
    for i in range(len(z) - 1)
]
month1 = day13(month)
month[1] -= 1
month2 = day13(month)
week = [0] * 7
shift = 0
for i in range(n):
    if i:
        shift = (shift + tot) % 7
    if (not i % 4 and i % 100) or i == 100:
        month, tot = month1, 366
    else:
        month, tot = month2, 365
    for j in month:
        week[(j + shift + 1) % 7] += 1
output = ''
for i in week:
    output += str(i) + ' '
fout.write(output[:-1] + '\n')
fout.close()

