from aoc_utils import parse
from aocd import get_data
import numpy as np
import time


year=2023
day=21

dat = get_data(year=year, day=day, block=True)

# 16
dat2 = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''

dir2vec = {
    'N': np.array((-1, 0)),
    'S': np.array((1, 0)),
    'E': np.array((0, 1)),
    'W': np.array((0, -1)),
}

dat = [list(x) for x in parse(dat)]
dat = np.array(dat)
print(dat)


def print_garden(dat, s=0):

    out = '\n'
    for i in range(dat.shape[0]):
        for j in range(dat.shape[1]):
            out += dat[i, j]
        out += '\n'
    print(out)
    time.sleep(s)


n_steps = 64
ctiles = [tuple(np.argwhere(dat == 'S')[0])]

for i in range(n_steps):
    odat = dat.copy()
    ntiles = set()
    rocks = set()
    xxx = set()
    for tile in ctiles:
        for d, v in dir2vec.items():
            ntile = tuple(tile + v)
            if 0 <= ntile[0] < dat.shape[0] and 0 <= ntile[1] < dat.shape[1]:
                if dat[ntile] not in '#':
                    ntiles.add(ntile)
                    odat[ntile] = 'O'
                else:
                    rocks.add(ntile)
                xxx.add(ntile)
    ctiles = ntiles

print_garden(odat)
print(len(ctiles))
