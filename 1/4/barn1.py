"""
ID: gohit.y1
LANG: PYTHON3
TASK: barn1
"""
import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)

fin = open("barn1.in", "r")
fout = open("barn1.out", "w")

m, s, n = fin.readline()[:-1].split(' ')
m, s, n = int(m), int(s), int(n)
a = [int(x[:-1]) for x in fin.readlines()]

def quicksort(l, r, obj):
    if not l < r:
        return obj
    i, j, x = l, r, obj[r]
    while (i < j):
        while (i < j and obj[i] <= x):
            i += 1
        obj[j] = obj[i]
        while (i < j and obj[j] > x):
            j -= 1
        obj[i] = obj[j]
    obj[i] = x
    quicksort(l, i - 1, obj)
    quicksort(i + 1, r, obj)
    return obj
def bucketsort(obj):
    if not obj:
        return []
    bucket8bit = [[[] for _ in range(256)] for _ in range(4)]
    for x in obj:
        bucket8bit[0][x & 0xff].append(x)
    for bucket in bucket8bit[0]:
        for x in bucket:
            bucket8bit[1][(x & 0xffff) >> 8].append(x)
    for bucket in bucket8bit[1]:
        for x in bucket:
            bucket8bit[2][(x & 0xffffff) >> 16].append(x)
    for bucket in bucket8bit[2]:
        for x in bucket:
            bucket8bit[3][x >> 24].append(x)
    obj = []
    for bucket in bucket8bit[3]:
        for x in bucket:
            obj.append(x)
    return obj

a = quicksort(0, n - 1, a)
#a = bucketsort(a)

num, tot, last, diff = 1, 1, a[0], []
for x in a[1:]:
    if x - last - 1:
        diff.append(x - last - 1)
        num += 1
    tot += 1
    last = x
diff = quicksort(0, len(diff) - 1, diff)
#diff = bucketsort(diff)
for i in range(num - m):
    tot += diff[i]
fout.write(str(tot) + '\n')

