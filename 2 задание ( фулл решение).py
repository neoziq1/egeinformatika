from itertools import *
def f(x, y, z, w):
    return ((x <= y) or (y == w)) and ((x or z) == w)

for a in product([0, 1], repeat=4):
    table = [(1, 0, 0, 1), (0, a[0], a[1], 1), (a[2], 1, 0, a[3])]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
        print(p)
