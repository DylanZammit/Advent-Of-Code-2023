from aoc_utils import *
from aocd import get_data
import numpy as np
from functools import cache
from collections import defaultdict

year=2023
day=23

dat = get_data(year=year, day=day, block=True)

# 154
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


G = defaultdict(dict)


def print_path(z):
    ccc = dat.copy()
    for i in range(dat.shape[0]):
        for j in range(dat.shape[0]):
            if (i, j) in z:
                ccc[(i, j)] = '+'

    print('\n'.join([''.join(r) for r in ccc]))


def find_junctions(u=(0, 1), dir='v', tgt=(dat.shape[0]-1, dat.shape[1]-2)):
    j1 = u
    u = tuple(u + dir2vec[dir])
    if min(u) < 0 or max(u) >= dat.shape[0] or dat[u] == '#': return
    d = 1
    path = [j1]
    while True:
        path.append(u)
        possibilities = []
        for dir, vec in dir2vec.items():
            v = tuple(u + vec)
            if v in path or min(v) < 0 or max(v) >= dat.shape[0] or dat[v] == '#': continue
            possibilities.append(v)

        if len(possibilities) > 1:
            G[j1][u] = d

            if u not in G:
                for ndir in dir2vec:
                    find_junctions(u, ndir, tgt)
            return

        elif len(possibilities) == 0:
            return

        u = possibilities[0]
        if u in [tgt, (0, 1)]:
            G[j1][u] = d
            find_junctions(u, '^', tgt)
            return
        d += 1


@cache
def get_path(u=(0, 1), visited=None, d=0, tgt=(dat.shape[0]-1, dat.shape[1]-2)):

    if not visited: visited = (u,)
    if u == tgt: return d
    av = [(v, nd) for v, nd in G[u].items() if v not in visited]
    return max(get_path(v, visited + (v,), d+nd, tgt) for v, nd in av) if len(av) else 0


find_junctions()
print_path(G.keys())
print(get_path() + 1)
