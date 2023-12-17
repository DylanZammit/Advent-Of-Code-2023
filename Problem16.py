from aocd import get_data
import time
import numpy as np
import os

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
dat = np.array([list(x) for x in dat])

print(dat)

dir2vec = {
    'N': np.array((-1, 0)),
    'S': np.array((1, 0)),
    'E': np.array((0, 1)),
    'W': np.array((0, -1)),
}

vec2dir = {tuple(v): k for k, v in dir2vec.items()}


def deco(s, i=0, space=True):
    z = 92 + i
    out = f' \033[{z}m{s}\033[0m '
    if not space: out = out.strip()
    return out


def dir2arrow(dir):
    if dir == 'N':
        arrow = '^'
    elif dir == 'S':
        arrow = 'V'
    elif dir == 'E':
        arrow = '>'
    elif dir == 'W':
        arrow = '<'
    return arrow


def draw_beams(dat, hist, lb=15):
    hists = {k: hist[k] for k in list(reversed(hist))[:lb]}
    out = '\n'
    for i in range(dat.shape[0]):
        for j in range(dat.shape[1]):
            if (i, j) in hists:
                tile = dat[i, j]
                dir = hists[(i, j)]
                arrow = dir2arrow(dir)
                out += deco(arrow if tile == '.' else tile, space=False)
            else:
                out += f'{dat[i, j]}'
        out += '\n'

    # print(out)
    print(out[:5000])
    # print(out, end='\033[F'*dat.shape[0])
    time.sleep(0.1)

    os.system('cls' if os.name == 'nt' else 'clear')

vis = {}
def get_path(i=0, j=-1, dir='E', first=False):

    while (i, j, dir) not in hist and (first or (0 <= i < dat.shape[0] and 0 <= i < dat.shape[1])):
        vec = dir2vec[dir]
        vis[(i, j)] = dir
        draw_beams(dat, vis)
        hist.add((i, j, dir))
        ens.add((i, j))
        ni, nj = vec + (i, j)
        if ni < 0 or ni >= dat.shape[0] or nj < 0 or nj >= dat.shape[1]: return
        tile = dat[ni, nj]
        if tile == '.' or (dir in 'NS' and tile in '|') or (dir in 'EW' and tile in '-'):
            i, j, dir = ni, nj, dir
        elif tile == '/':
            i, j, dir = ni, nj, vec2dir[tuple(vec[::-1] * -1)]
        elif tile == '\\':
            i, j, dir = ni, nj, vec2dir[tuple(vec[::-1])]

        elif tile in '|-':
            if tile == '|':
                get_path(ni, nj, 'N')
                get_path(ni, nj, 'S')
            elif tile == '-':
                get_path(ni, nj, 'W')
                get_path(ni, nj, 'E')


res = 0
for i in range(dat.shape[0]):
    ens = set()
    hist = set()
    get_path(i, -1, 'E', first=True)
    res = max(res, len(ens)-1)

    ens = set()
    hist = set()
    get_path(i, dat.shape[1], 'W', first=True)
    res = max(res, len(ens)-1)

for j in range(dat.shape[1]):
    ens = set()
    hist = set()
    get_path(-1, j, 'S', first=True)
    res = max(res, len(ens)-1)

    ens = set()
    hist = set()
    get_path(dat.shape[0], j, 'N', first=True)
    res = max(res, len(ens)-1)

vis = {}
hist = set()
ens = set()
get_path(0, -1, 'E', first=True)

print('Part 1', len(ens)-1)
print('Part 2', res)

