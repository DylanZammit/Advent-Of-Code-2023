from aocd import get_data
import regex as re

year=2023
day=14

dat = get_data(year=year, day=day, block=True)


# 136
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

dat = [''.join(x[::-1]) for x in list(zip(*dat))]

out = 0
n = len(dat[0])
for r in dat:
    for z in re.finditer(r'O', r):
        m = re.match(rf'.{{{z.start()}}}[O.]*((?=#)|$)', r)
        out += m.end() - m.string[z.start() + 1:m.end()].count('O') if m else 0

print(out)
