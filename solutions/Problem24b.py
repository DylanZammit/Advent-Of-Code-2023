from aoc_utils import *
from aocd import get_data
import sympy as sp
from sympy.solvers import solve
from pprint import pprint

year=2023
day=24

dat = get_data(year=year, day=day, block=True)

# 2
dat2 = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''

dat = parse(dat, ints)


class Path:
    def __init__(self, dat):
        self.pos = dat[:3]
        self.dir = dat[3:]


paths = [Path(r) for r in dat]

paths = paths[:6]

syms = 'p1 p2 p3 v1 v2 v3 ' + ' '.join([f't{i+1}' for i in range(len(paths))])

syms = sp.symbols(syms)

eqns_x = [sp.Eq(syms[0] + syms[i+6] * syms[3], path.pos[0] + syms[i+6] * path.dir[0]) for i, path in enumerate(paths)]
eqns_y = [sp.Eq(syms[1] + syms[i+6] * syms[4], path.pos[1] + syms[i+6] * path.dir[1]) for i, path in enumerate(paths)]
eqns_z = [sp.Eq(syms[2] + syms[i+6] * syms[5], path.pos[2] + syms[i+6] * path.dir[2]) for i, path in enumerate(paths)]


eqns = eqns_x + eqns_y + eqns_z
out = solve(eqns, syms, dict=True)

pprint(eqns)
pprint(out)
print(out[0][syms[0]] + out[0][syms[1]] + out[0][syms[2]])
