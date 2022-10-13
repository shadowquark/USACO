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
    x7  x6  x5      
x10 x9  x8          
---------------
x14 x13 x12 x11
"""
def construct_x(x, out, p, q):
    if p == q:
        out.append(x)
        return out
    for y in a:
        if not (p or y):
            continue
        x += y * 10 ** (q - p - 1)
        out = construct_x(x, out, p + 1, q)
        x -= y * 10 ** (q - p - 1)
    return out
nums, b = [3, 2], []
for num in nums:
    b.append(construct_x(0, [], 0, num))
def check(x, version):
    if version:
        if (x < 10000 and x > 999 and x // 1000 in a
            and x // 100 % 10 in a and x // 10 % 10 in a and x % 10 in a):
            return 1
        else:
            return 0
    else:
        if (x < 1000 and x > 99
            and x // 100 in a and x // 10 % 10 in a and x % 10 in a):
            return 1
        else:
            return 0
def dfs(tot, x):
    if len(x) == 2:
        if (check(x[1] % 10 * x[0], 0)
            and check(x[1] // 10 * x[0], 0)
            and check(x[0] * x[1], 1)):
            return tot + 1, x[:-1]
        else:
            return tot, x[:-1]
    for y in b[len(x)]:
        x.append(y)
        tot, x = dfs(tot, x)
    return tot, x[:-1]
tot, _ = dfs(0, [])
fout.write(str(tot) + '\n')

