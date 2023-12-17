# from aoc_utils import *
from aocd import get_data
import numpy as np
import os
import time

year=2023
day=17

dat = get_data(year=year, day=day, block=True)

# 102
dat2 = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''

dat = dat.split('\n')
dat = np.array([list(x) for x in dat])
dat = dat.astype(int)
# s = 500
# dat = dat[:s, :s]
print(dat)
print(dat.shape)

dir2vec = {
    'N': np.array((-1, 0)),
    'S': np.array((1, 0)),
    'E': np.array((0, 1)),
    'W': np.array((0, -1)),
}

vec2dir = {tuple(v): k for k, v in dir2vec.items()}

dir2num = {
    'N': 0,
    'S': 1,
    'E': 2,
    'W': 3,
}

num2dir = {v: k for k, v in dir2num.items()}


def min_dist(A):
    return np.unravel_index(A.argmin(), A.shape)


def deco(s, i=0, space=True, col=False):
    z = 92 + i
    out = f' \033[{z}m{s}\033[0m ' if col else f' {s} '
    if not space: out = out.strip()
    return out


def print_path(hist, pos):
    out = '\n'
    for i in range(dat.shape[0]):
        for j in range(dat.shape[1]):
            if (i, j) == pos:
                out += deco(dat[i, j], space=True, col=True, i=1)
            elif (i, j) in {(z[0], z[1]) for z in hist}:
                out += deco(dat[i, j], space=True, col=True, i=10)
            else:
                out += deco(dat[i, j], space=True)
        out += '\n'

    print(out)
    time.sleep(0.1)

    # os.system('cls' if os.name == 'nt' else 'clear')


def dijkstra(dat, dir='S'):
    # 0, 1, 2, 3 -> N, S, E, W
    tgt = (dat.shape[0] - 1, dat.shape[1] - 1, )
    Q = np.full((dat.shape[0], dat.shape[1], 4, ), False)
    dist = np.full((dat.shape[0], dat.shape[1], 4, ), np.inf)
    prev = np.full((dat.shape[0], dat.shape[1], 4, ), None)

    dist[0, 0, dir2num[dir]] = 0

    while not Q.all():
        tmpdist = dist.copy()
        tmpdist[Q] = np.inf
        u = min_dist(tmpdist)
        Q[u] = True
        dir = num2dir[u[-1]]
        vec = dir2vec[dir]

        for d in range(1, 4):
            npos = tuple(u[:2] + dir2vec[dir] * d)
            for ndir in [vec2dir[tuple(vec[::-1] * -1)], vec2dir[tuple(vec[::-1])]]:
                v = (npos[0], npos[1], dir2num[ndir])

                if not (0 <= npos[0] < dat.shape[0] and 0 <= npos[1] < dat.shape[1]): continue
                if Q[v]: continue

                all_npos = [tuple(u[:2] + dir2vec[dir] * dd) for dd in range(1, d + 1)]
                extra = sum(dat[p[0], p[1]] for p in all_npos)

                alt = dist[u] + extra

                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist, prev


tgt = (dat.shape[0] - 1, dat.shape[1] - 1)

dist, prev = dijkstra(dat, dir='S')
s_dist = min(dist[(tgt[0], tgt[1], i)] for i in range(4))

dist, prev = dijkstra(dat, dir='E')
e_dist = min(dist[(tgt[0], tgt[1], i)] for i in range(4))

S = []
for i in range(4):
    u = (tgt[0], tgt[1], i)
    if prev[u] is not None or u == tgt:
        while u is not None:
            S.append(u)
            u = prev[u]
    print_path(S, tgt)

print(int(s_dist), int(e_dist))
print('SOL = ', int(min(s_dist, e_dist)))
