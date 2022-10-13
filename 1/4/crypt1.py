"""
ID: gohit.y1
LANG: PYTHON3
TASK: crypt1
"""
import sys
from functools import partial as par
def F(*z):
    z = [*z]
    return [*reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*reduce(lambda x, y: map(y, x), z)] 
fyx = lambda f, *x: lambda *y: f(*y, *x)

fin = open("crypt1.in", "r")
fout = open("crypt1.out", "w")

n = int(fin.readline()[:-1])
a = [int(x) for x in fin.readline()[:-1].split(' ')]

sys.setrecursionlimit(10000)
"""
    x2  x1  x0      x[0]
        x4  x3      x[1]
---------------
    x7  x6  x5      x[2]
x10 x9  x8          x[3]
---------------
x14 x13 x12 x11     x[4]
"""
tot = 0
num = [3, 2, 3, 3, 4]
b = []
def construct_x(m, n):
    if m == n:
        return 
for i in num:
    temp1, temp2, temp3 = 0, 1, []
    for j in range(i):
        for k in a:
            temp1 +=
        temp2 *= 10
        temp3.append
            
x = []
def dfs(x):
    if len(x) == 5:
        if not ((x[1] % 10 * x[0] - x[2])
                or (x[1] // 10 * x[0] - x[3])
                or (x[3] * 10 + x[2] - x[4])):
            tot += 1
        return x[:-1]
    for i in range(n):
        x = dfs(x)
    return x[:-1]
dfs(x)
print(tot)

