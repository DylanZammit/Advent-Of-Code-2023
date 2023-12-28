from aoc_utils import *
from aocd import get_data
import numpy as np
import regex as re

# https://en.wikipedia.org/wiki/Shoelace_formula
# https://en.wikipedia.org/wiki/Pick%27s_theorem


def det(u, v):
    return int(u[0]) * int(v[1]) - int(u[1]) * int(v[0])


year=2023
day=18

dat = get_data(year=year, day=day, block=True)

# 952408144115
dat2 = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''

dat = parse(dat)

num2dir = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U',
}

num2vec = {
    3: np.array((-1, 0)),
    1: np.array((1, 0)),
    0: np.array((0, 1)),
    2: np.array((0, -1)),
}

b = 0
P = [(0, 0)]
for r in dat:
    hex = re.search(r'#(\w{6})', r).group(1)
    l = int(hex[:-1], 16)
    num = int(hex[-1])
    P.append(tuple(np.array(P[-1]) + l * num2vec[num]))
    b += l

n = len(P)

A = abs(sum(det(P[i], P[(i+1) % n])/2 for i in range(n)))  # shoelace formula

i = A - b / 2 + 1  # pick's theorem

print(int(i+b))
