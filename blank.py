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
# f(x1, x2...) -> ff1(f)((x1, x2...))
# f((x1, x2...)) -> ff2(f)(x1, x2...)
# f(x1, x2..., y1, y2...) -> ff3(f, (y1, y2...))((x1, x2...))
# f(x1, x2..., y1, y2...) -> ff4(f, (y1, y2...))(x1, x2...)
# f(x1, x2..., y1, y2...) -> ff5(f, (x1, x2...))((y1, y2...))
# f(x1, x2..., y1, y2...) -> ff6(f, (x1, x2...))(y1, y2...)
ff1 = lambda f: lambda x: f(*x)
ff2 = lambda f: lambda *x: f(x)
ff3 = lambda f, x: lambda y: f(*y, *x)
ff4 = lambda f, x: ff2(ff3(f, x))
ff5 = lambda f, x: lambda y: f(*x, *y)
ff6 = lambda f, x: ff2(ff5(f, x))

fin = open(".in", 'r')
fout = open(".out", 'w')



fout.close()

