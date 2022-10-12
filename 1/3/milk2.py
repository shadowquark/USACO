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
read = fin.readlines()
read = [[int(i) for i in j.split(' ')] for j in read]
def quicksort(l, r, obj):
    if not l < r:
        return obj
    i, j, x = l, r, obj[r]
    while (i < j):
        while (i < j and obj[i][0] <= x[0]):
            i += 1
        obj[j] = obj[i]
        while (i < j and obj[j][0] > x[0]):
            j -= 1
        obj[i] = obj[j]
    obj[i] = x
    quicksort(l, i - 1, obj)
    quicksort(i + 1, r, obj)
    return obj
read = quicksort(0, n - 1, read)
begin, end, maxlen, maxint = read[0][0], read[0][1], read[0][1] - read[0][0], 0
for i in range(1, n):
    l, r = read[i]
    if l > end:
        maxint = max(maxint, l - end)
        begin, end = l, r
    else:
        end = max(end, r)
        maxlen = max(maxlen, end - begin)
print(maxlen, maxint)
fout.write(str(maxlen) + ' ' + str(maxint) + '\n')
        
fout.close()

