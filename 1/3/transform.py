"""
ID: gohit.y1
LANG: PYTHON3
TASK: transform
"""

import sys
import math
import functools as ft
import random as rnd

# g(f(x)) -> F([x, f, g, ...])
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fin = open("transform.in", 'r')
fout = open("transform.out", 'w')

n = int(fin.readline())
read = fin.readlines()
ori = [[read[:n][i][j] for j in range(n)] for i in range(n)]
final = [[read[n:][i][j] for j in range(n)] for i in range(n)]
def check(x, label):
    if x == final:
        fout.write(str(label) + '\n')
        sys.exit()
f1 = lambda x: [[x[n - i - 1][j] for i in range(n)] for j in range(n)]
f2 = lambda x: [[x[n - i - 1][n - j - 1] for j in range(n)] for i in range(n)]
f3 = lambda x: [[x[i][n - j - 1] for i in range(n)] for j in range(n)]
f4 = lambda x: [[x[i][n - j - 1] for j in range(n)] for i in range(n)]
check(f1(ori), 1)
check(f2(ori), 2)
check(f3(ori), 3)
check(f4(ori), 4)
check(F([ori, f4, f1]), 5)
check(F([ori, f4, f2]), 5)
check(F([ori, f4, f3]), 5)
check(ori, 6)
fout.write("7\n")

fout.close()

