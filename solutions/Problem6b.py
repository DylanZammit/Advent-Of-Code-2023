from aoc_utils import *
from aocd import get_data

year=2023
day=6

dat = get_data(year=year, day=day, block=True)

# 288 = 4 * 8 * 9
dat2 = '''Time:      7  15   30
Distance:  9  40  200'''
dat = dat.replace(' ', '')
dat = parse(dat, ints)
print(dat)

def d(t, p): return (t - p) * p

out = []
for t, r in zip(*dat):
    p_record = int((t + sqrt(t**2 - 4 * r)) / 2)
    p_opt = (t / 2)
    if d(t, p_record) == r: p_record -= 1
    z = 1 + int(p_record - p_opt) * 2
    if t % 2 == 1: z += 1
    out.append(z)

print(prod(out))
