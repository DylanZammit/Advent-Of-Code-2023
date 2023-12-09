from aoc_utils import *
from aocd import get_data
import numpy as np

year=2023
day=9

dat = get_data(year=year, day=day, block=True)

# 114
dat2 = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
dat = parse(dat, ints)


def get_diff(seq):
    out = np.diff(seq)
    return seq[0] if all([o == 0 for o in out]) else seq[0] - get_diff(out)

print(sum([get_diff(row) for row in dat]))
