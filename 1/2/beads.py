"""
ID: gohit.y1
LANG: PYTHON3
TASK: beads
"""

import math
import functools as ft
import random as rnd

# g(f(x)) -> F([x, f, g, ...])
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fin = open ("beads.in", 'r')
fout = open ("beads.out", 'w')

n = int(fin.readline())
neck = fin.readline()[:-1]
neck += neck
maxlen = 0
for i in range(n):
    flag1, flag2 = neck[i], neck[i - 1]
    count1 = count2 = 1
    for j in range(1, n):
        # Only 'r' and 'b' are different, while 'r' - 'b' = 16.
        diff = lambda x, y: abs(ord(x) - ord(y)) == 16
        def check(flag, count, color):
            if not flag or diff(color, flag):
                flag = ''
            else:
                flag = flag if color == 'w' else color
                count += 1
            return flag, count
        flag1, count1 = check(flag1, count1, neck[i + j])
        flag2, count2 = check(flag2, count2, neck[i - j - 1])
        if not (flag1 or flag2):
            break
    maxlen = maxlen if count1 + count2 < maxlen else count1 + count2 
fout.write(str(maxlen if maxlen < n else n) + '\n')

fout.close()

