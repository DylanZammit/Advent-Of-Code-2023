from aoc_utils import *
from aocd import get_data
import numpy as np
import os
import time
import regex as re

year=2023
day=18

dat = get_data(year=year, day=day, block=True)

# 62
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

mp = np.full((800, 800), '.')


dir2vec = {
    'U': np.array((-1, 0)),
    'D': np.array((1, 0)),
    'R': np.array((0, 1)),
    'L': np.array((0, -1)),
}

def print_path(dat):
    out = '\n'
    for i in range(dat.shape[0]):
        for j in range(dat.shape[1]):
            out += dat[i, j]
        out += '\n'
    print(out)
    # print(['\n'.join([''.join(x) for x in dat])])


pos = (400, 400)
npos = pos
mp[pos] = '#'
for inst in dat:
    dir, dist, col = inst.split()
    vec = dir2vec[dir]
    dist = int(dist)
    print(dir, dist, col, vec)
    for d in range(1, dist+1):
        npos = tuple(pos + vec * d)
        mp[npos] = '#'
    pos = npos

out = np.count_nonzero(mp == '#')
inside_ct = 0
for i, row in enumerate(mp):
    if i < 5 or i > 795: continue
    myrow = ''.join(row)

    startend = []
    for edge in re.finditer(r'#+', myrow):
        if edge.end() - edge.start() == 1:
            startend.append(edge.start())
            continue
        is_line = mp[i-1, edge.start()] == mp[i+1, edge.end() - 1] == '#' or mp[i+1, edge.start()] == mp[i-1, edge.end() - 1] == '#'

        if is_line: # NOT U
            startend.append(edge.end() - 1 if len(startend) % 2 == 0 else edge.start())
    for j in range(0, len(startend), 2):
        # print(myrow, startend, is_line, startend[j+1] - startend[j] - 1)
        # breakpoint()
        inside_ct += startend[j+1] - startend[j] - 1
        for k in range(startend[j] +1, startend[j+1]):
            mp[i, k] = 'O'

print_path(mp)
# print(mp)
print(np.count_nonzero(mp == '#'))
print(np.count_nonzero(mp == 'O'))
print('-----')
# print(out)
print(inside_ct)
print('-----')
print(np.count_nonzero(mp == '#') + np.count_nonzero(mp == 'O'))
# print(out + inside_ct)

# i = inside_ct
# # i = np.count_nonzero(mp == '#')
# b = np.count_nonzero(mp == 'O')
# A = i + b/2 - 1
# print(A)
