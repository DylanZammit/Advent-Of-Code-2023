from aoc_utils import *
from aocd import get_data
import numpy as np
from itertools import product

year=2023
day=23

dat = get_data(year=year, day=day, block=True)

# 94
dat2 = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''

dat = parse(dat)
dat = np.array([list(x) for x in dat])

dir2vec = {
    '^': np.array((-1, 0)),
    'v': np.array((1, 0)),
    '>': np.array((0, 1)),
    '<': np.array((0, -1)),
}
vec2dir = {tuple(v): k for k, v in dir2vec.items()}


def get_path(u=(0, 1), tgt=(dat.shape[0]-1, dat.shape[1]-2), path=None):
    path.add(u)
    while tgt not in path:
        if dat[u] in dir2vec:
            u = tuple(u + dir2vec[dat[u]])
            if u in path: return []
            path.add(u)
            continue

        possibilities = []
        for dir, vec in dir2vec.items():
            v = tuple(u + dir2vec[dir])
            if v in path or dat[v] == '#' or min(v) < 0 or max(v) >= dat.shape[0]: continue
            possibilities.append(v)

        if len(possibilities) > 1:
            return max((get_path(p, tgt, path.union({u})) for p in possibilities), key=lambda x: len(x))
        elif len(possibilities) == 0:
            return []
        u = possibilities[0]
        path.add(u)
    return path


path = get_path(path={(0, 1)})
for i in range(dat.shape[0]):
    for j in range(dat.shape[0]):
        if (i, j) in path and dat[(i, j)] == '.':
            dat[(i, j)] = '+'

print('\n'.join([''.join(r) for r in dat]))

print(len(path)-1)
