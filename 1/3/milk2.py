"""
ID: gohit.y1
LANG: PYTHON3
TASK: milk2
"""

import math
import functools as ft
import random as rnd

# g(f(x)) -> F([x, f, g, ...])
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fin = open("milk2.in", 'r')
fout = open("milk2.out", 'w')

n = int(fin.readline())
begin, end = [int(i) for i in fin.readline().split(' ')]
maxint, maxlen = 0, end - begin
for _ in range(n - 1):
    l, r = [int(i) for i in fin.readline().split(' ')]
    if l > end:
        maxint = max(maxint, l - end)
        begin, end = l, r
    else:
        end = max(end, r)
        maxlen = max(maxlen, end - begin)
#print(maxlen, maxint)
fout.write(str(maxlen) + ' ' + str(maxint) + '\n')
        
fout.close()

