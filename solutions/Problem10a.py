from aoc_utils import *
from math import lcm
from aocd import get_data
from itertools import cycle
import numpy as np

year=2023
day=10

dat = get_data(year=year, day=day, block=True)

# 8
dat2 = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''
dat = [list(x) for x in parse(dat)]
dat = np.array(dat)

dat = np.pad(dat, 1, constant_values='.')

pipe_direction = {
    'F': [(1, 0), (0, 1)],
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'J': [(0, -1), (-1, 0)],
    'L': [(-1, 0), (0, 1)],
    '7': [(0, -1), (1, 0)],
    '.': -1
}

start = np.array(np.where(dat == 'S')).flatten()

for s1 in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
    new_dir = s1
    curr = start + new_dir
    prev = start
    path = [start]
    while True:
        pipe = dat[curr[0], curr[1]]
        if pipe in 'S.': break

        d1, d2 = pipe_direction[pipe]
        if tuple(curr + d1) != tuple(prev) and tuple(curr + d2) != tuple(prev): break
        if tuple(curr + d1) == tuple(prev): d1, d2 = d2, d1
        path.append(curr)
        prev = curr
        curr = curr + d1

    if dat[curr[0], curr[1]] == 'S':
        res = path
        print(len(res) // 2 + 1 if len(res) % 2 == 1 else len(res) // 2)
        break
