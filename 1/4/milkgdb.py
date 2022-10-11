import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]

fout = open("milk.in", 'w')
fout.write(str(200000) + ' ' + str(1000) + '\n')
for i in range(1000):
    fout.write(str(1000 - i) + ' ' + str(200000) + '\n')

