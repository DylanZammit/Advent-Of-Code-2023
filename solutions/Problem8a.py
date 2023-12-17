from aoc_utils import *
from itertools import cycle
from aocd import get_data

year=2023
day=8

dat = get_data(year=year, day=day, block=True)

# 6440
dat2 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''
dat = parse(dat, words)

mapper = {a: (b, c) for a, b, c in dat[2:]}

directions = dat[0][0]

src = 'AAA'
ct = 0
for d in cycle(directions):
    side = 0 if d == 'L' else 1
    src = mapper[src][side]
    ct += 1
    if src == 'ZZZ': break

print(ct)