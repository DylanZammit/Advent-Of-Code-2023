from aocd import get_data
import regex as re
from aoc_utils import *
from aocd import get_data
import numpy as np
from functools import cache
import os
import sys
os.system('color')
np.set_printoptions(threshold=sys.maxsize)

import sys
sys.setrecursionlimit(2000)

year=2023
day=16

dat = get_data(year=year, day=day, block=True)

# 46
dat2 = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''

dat = dat.split('\n')
# dat = np.array(dat)
dat = np.array([list(x) for x in dat])


print(dat)

ens = set()

dirs = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
}


def draw_beams(dat, a=None, b=None):
    dd = dat.copy()
    for i in range(len(dd)):
        for j in range(len(dd[0])):
            if (i, j) in ens and dd[i, j] == '.':
                dd[i, j] = '#'

            if (a, b) == (i, j):
                # dd[i, j] = '\033[92m' + dd[i, j]
                dd[i, j] = 'O'

    return dd

hist = set()

@cache
def ene(i=0, j=-1, dir='E', first=False):
    while True:
        if (i, j, dir) in hist:
            return
        if not first and (i < 0 or i >= dat.shape[0] or j < 0 or j >= dat.shape[1]):
            break
        hist.add((i, j, dir))
        ens.add((i, j))
        ni, nj = i+dirs[dir][0], j+dirs[dir][1]
        if ni < 0 or ni >= dat.shape[0] or nj < 0 or nj >= dat.shape[1]: return
        tile = dat[ni, nj]

        ndir = dir
        if tile == '.' or (dir in 'NS' and tile in '|') or (dir in 'EW' and tile in '-'):
            ndir = dir
            i, j, dir = ni, nj, ndir
        elif tile == '/':
            if dir == 'E':
                ndir = 'N'
            elif dir == 'W':
                ndir = 'S'
            elif dir == 'N':
                ndir = 'E'
            elif dir == 'S':
                ndir = 'W'

            i, j, dir = ni, nj, ndir
        elif tile == '\\':
            if dir == 'E':
                ndir = 'S'
            elif dir == 'W':
                ndir = 'N'
            elif dir == 'N':
                ndir = 'W'
            elif dir == 'S':
                ndir = 'E'

            i, j, dir = ni, nj, ndir

        elif tile in '|-':
            if tile == '|':
                ndir='N'
                ene(ni, nj, ndir)
                ndir='S'
                ene(ni, nj, ndir)
            elif tile == '-':
                ndir='W'
                ene(ni, nj, ndir)
                ndir='E'
                ene(ni, nj, ndir)


ene(first=True)


print(draw_beams(dat))
print(len(ens)-1)
