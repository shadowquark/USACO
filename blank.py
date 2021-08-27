"""
ID: gohit.y1
LANG: PYTHON3
TASK:
"""

import sys
import math
import functools as ft
import random as rnd

# g(f(x)) -> F([x, f, g...])
# g(f([x1, x2...])) -> FF([x1, x2...], f, g...)
F = lambda z: [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
# f(x1, x2..., y1, y2...) -> fxy(f, x1, x2...)(y1, y2...)
# f(x1, x2..., y1, y2...) -> fyx(f, y1, y2...)(x1, x2...)
# f(x1, x2..., y1 = y1, y2 = y2...) -> fYx(f, y1 = y1, y2 = y2...)(x1, x2...)
fxy = lambda f, *x: lambda *y: f(*x, *y)
fyx = lambda f, *x: lambda *y: f(*y, *x)
fYx = lambda f, **x: lambda *y: f(*y, **x)

fin = open(".in", 'r')
fout = open(".out", 'w')



fout.close()

