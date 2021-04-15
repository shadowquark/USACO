"""
ID: gohit.y1
LANG: PYTHON3
TASK:
"""

import math
import functools as ft
import random as rnd

# g(f(x)) -> F([x, f, g, ...])
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fin = open (".in", 'r')
fout = open (".out", 'w')



fout.close()

