import re
from itertools import combinations
from aocd import get_data

year=2023
day=11

dat = get_data(year=year, day=day, block=True)
dat2 = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''


dat = dat.split()

nrow, ncol = len(dat), len(dat[0])

dat_trans = [''] * nrow

for i in range(nrow):
    for j in range(ncol):
        dat_trans[j] += dat[i][j]

empty_rows = [i for i, r in enumerate(dat) if '#' not in r]
m = 1_000_000 - 1 # set this to 2 - 1 for part 1
# m=2-1
rcum = []
prev = 0
for i, er in enumerate(empty_rows):
    rcum += [i * m] * (er - prev)
    prev = er

rcum += [(i + 1) * m] * (nrow - len(rcum))

empty_cols = [i for i, r in enumerate(dat_trans) if '#' not in r]
ccum = []
prev = 0
for i, er in enumerate(empty_cols):
    ccum += [i * m] * (er - prev)
    prev = er

ccum += [(i + 1) * m] * (ncol - len(ccum))

gal_loc = [(i, x.start()) for i, r in enumerate(dat) for x in re.finditer('#', r)]

print(sum(abs(b[1] + ccum[b[1]] - a[1] - ccum[a[1]]) + abs(b[0] + rcum[b[0]] - a[0] - rcum[a[0]]) for a, b in
          combinations(gal_loc,2)))