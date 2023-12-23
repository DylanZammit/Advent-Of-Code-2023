from aoc_utils import *
from functools import cache
from aocd import get_data
import regex as re
import numpy as np

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


def print_garden(dat):
    out = '\n'
    for i in range(dat.shape[0]):
        for j in range(dat.shape[1]):
            out += dat[i, j]
        out += '\n'
    print(out)


visited = set()


def start_search(start, n):
    ctiles = [start]
    for i in range(n):
        if i in [65, 131+65, 131*2+65]:
            print(i, len(ctiles))

        ntiles = set()
        for tile in ctiles:
            for d, v in dir2vec.items():
                ntile = tuple(tile + v)
                ntile_mod = (ntile[0] % dat.shape[0], ntile[1] % dat.shape[1])
                if dat[ntile_mod] != '#':
                    visited.add(ntile)
                    ntiles.add(ntile)
        ctiles = ntiles
    return ctiles


start = tuple(np.argwhere(dat == 'S')[0])
x, y = start

start_search(start, 131*3+66)

# (14860 x^2)/17161 + (23375 x)/17161 + 256807/17161 when x = 26501365


# (65, 3762)
# (196, 33547)
# (327, 93052)
# quadratic equation passing through above points using wolfram
def res(s): return (14860 * s ** 2)/17161 + (23375 * s)/17161 + 256807/17161

print(res(131 * 202300 + 65))

# breakpoint()
#
# dat_inner = dat.copy()
# dat_outer = dat.copy()
# for i in range(dat_inner.shape[0]):
#     for j in range(dat_inner.shape[1]):
#         dat_inner[i, j] = dat[i, j] if abs(i-x) + abs(j-x) <= x else '.'
#         dat_outer[i, j] = dat[i, j] if abs(i-y) + abs(j-y) >= y else '.'
#
# # print_garden(dat_inner)
# # breakpoint()
#
# def t(n): return n*(n+1) / 2
#
#
# @cache
# def myt(n):
#     return t(n) - myt(n-1) if n > 1 else 1
#
#
# def getres_inner(s=64):
#     # return 3697
#     return 3697 if s % 2 == 0 else 3762
#     # return myt(s-1)*4 + (4*s//2+1 - 526 - 2 if s % 2 == 0 else 4*(s//2+1) - 00 - 1)
#
#
# def getres_outer(s=64):
#     return 3700
#     # return 3738
#     return myt(s-1)*4 + (4*s//2+1 - 613 if s % 2 == 0 else 4*(s//2+1) - 00)
#
#
# def getres(s):
#     is_odd = s % 2 == 1
#     # is_odd = 0
#     nreps, rem = s // 131, s % 131
#     f = (((nreps+1)*2-1)**2 - 1) // 2  # indicates that it is quadratic
#     # print(f)
#
#     return f * (getres_outer(64) + getres_inner(64)) + getres_inner(64 + is_odd)
#
#
# inp = 64
# print(inp, getres(inp), '----> 3697', 3697 - getres(inp))
# inp = 65
# print(inp, getres(inp), '----> 3762', 3762 - getres(inp))
# inp = 131*1 + 65
# print(inp, getres(inp), '----> 33547', 33547 - getres(inp))
# inp = 131*2 + 65
# print(inp, getres(inp), '-----> 93052', 93052 - getres(inp))
# inp = 131*3 + 65
# print(inp, getres(inp), '-----> 182277', 182277 - getres(inp))
#
# inp = 131*202300+65  # 26501365
# print(inp, 'SOLUTION ------->', getres(inp))
# breakpoint()

