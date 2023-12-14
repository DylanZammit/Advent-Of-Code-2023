from aocd import get_data
import regex as re
import numpy as np

year=2023
day=14

dat = get_data(year=year, day=day, block=True)


# 64
dat2 = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

dat = dat.split('\n')
dat = np.array([list(x) for x in dat])

out = 0
n = len(dat[0])

def get_score(mat, k=1):
    out = 0
    mat = np.rot90(mat, k=k)
    n = len(mat[0])
    for i, r in enumerate(mat):
        out += (n - i) * np.count_nonzero(r == 'O')
    return out

n_cycles = 400
for nc in range(n_cycles):
    for k in range(4):
        dat = np.rot90(dat, axes=(1, 0))
        dat_new = dat.copy()
        overwritten = set()
        for i, rr in enumerate(dat):
            r = ''.join(rr)
            for z in re.finditer(r'O', r):
                m = re.match(rf'.{{{z.start()}}}[O.]*((?=#)|$)', r)

                new_loc = m.end() - m.string[z.start() + 1:m.end()].count('O') - 1
                if (i, z.start()) not in overwritten:
                    dat_new[i, z.start()] = '.'
                dat_new[i, new_loc] = 'O'
                overwritten.add((i, new_loc))
        dat = dat_new.copy()
    print(nc, get_score(dat, k=0))

M = 1_000_000_000
print('Notice that a cycle of length C begins at some point N. Get the value at position (M _ N) % C')
