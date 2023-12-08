from aoc_utils import *
from math import lcm
from aocd import get_data
from itertools import cycle


year=2023
day=8

dat = get_data(year=year, day=day, block=True)

# 6440
dat = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''
dat = parse(dat)

mapper = {inp[:3]: (inp[7:10], inp[12:15]) for inp in dat[2:]}

directions = dat[0]

new = [k for k in mapper if k.endswith('A')]

steps = []
for src in new:
    for ct, d in enumerate(cycle(directions), start=1):
        src = mapper[src][0 if d == 'L' else 1]
        if src.endswith('Z'): break
    steps.append(ct)

print(lcm(*steps))
