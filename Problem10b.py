import regex as re
from aoc_utils import *
from aocd import get_data
import numpy as np

year=2023
day=10

dat = get_data(year=year, day=day, block=True)

# 10
dat = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........'''
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
        if pipe in 'S.':
            break

        d1, d2 = pipe_direction[pipe]
        if tuple(curr + d1) != tuple(prev) and tuple(curr + d2) != tuple(prev):
            break
        if tuple(curr + d1) == tuple(prev):
            d1, d2 = d2, d1
        path.append(curr)
        prev = curr
        curr = curr + d1

    xx = dat.copy()
    # if xx[curr[0], curr[1]] == 'S':
    # print(path)
    # for r in path:
    #     xx[r[0], r[1]] = '*'
    # for r in xx:
    #     print(''.join(r))

    mask = dat.copy()
    for x in range(mask.shape[0]):
        for y in range(mask.shape[1]):
            # breakpoint()
            # print('asd')
            # print(list([tuple(z) for z in path]))
            if (x, y) not in list([tuple(z) for z in path]):
                # if dat[x, y] != '.':
                #     breakpoint()
                mask[x, y] = '.'
        # print(dat)
        # print(len(res) // 2 + 1 if len(res) % 2 == 1 else len(res) // 2)
        # break


ct = 0
# print(mask.shape)
# mask = mask[1:mask.shape[0]-1, 1:mask.shape[1]-1]
# print(mask.shape)
for row in range(mask.shape[0]):
    row_str = ''.join(mask[row])
    is_outside = True
    prev = ''
    for tile in row_str:
        # if row_str.startswith('L---J'): breakpoint()
        # print(row_str, is_outside, tile, ct)
        if tile in '|FJL7':
            is_outside = not is_outside

        if not is_outside and tile == '.':
            ct += 1
    print(row_str, ct)

    # for col in range(dat.shape[1]):
print(ct)
# breakpoint()