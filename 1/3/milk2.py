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
def quicksort(l, r):
    if l > r:
        return
    i, j, x = l, r, read[(l + r) // 2][0]
    while (i <= j):
        while (i < r and read[i][0] < x):
            i += 1
        while (j > l and read[j][0] > x):
            j -= 1
        if i <= j:
            read[i], read[j], i, j = read[j], read[i], i + 1, j - 1
    if i < r:
        quicksort(i, r)
    if j > l:
        quicksort(l, j)
quicksort(0, n - 1)
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

