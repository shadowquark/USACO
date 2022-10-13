"""
ID: gohit.y1
LANG: PYTHON3
TASK:
"""

import sys
import math
from functools import partial as par
import random as rnd

# g(f(x)) -> F(x, f, g...)
# g(f([x1, x2...])) -> FF([x1, x2...], f, g...)
def F(*z):
    z = [*z]
    return [*reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*reduce(lambda x, y: map(y, x), z)]
# f(x1, x2..., y1, y2...) -> fyx(f, y1, y2...)(x1, x2...)
fyx = lambda f, *x: lambda *y: f(*y, *x)

fin = open(".in", 'r')
fout = open(".out", 'w')

fout.close()

