from aoc_utils import *
from aocd import get_data

year=2023
day=22

dat = get_data(year=year, day=day, block=True)

# 5
dat2 = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''

dat = parse(dat, ints)
dat = sorted(dat, key=lambda x: min(x[2], x[5]))
print(dat)

top2bot = {i: set() for i in range(len(dat))}
unchecked = set(dat)
settled = {}
def get_overlap(a, b): return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)


for i, (x11, y11, z11, x12, y12, z12) in enumerate(dat):
    max_z = 0
    for j, (x21, y21, z21, x22, y22, z22) in settled.items():
        x1 = min(x11, x12), max(x11, x12)
        x2 = min(x21, x22), max(x21, x22)
        y1 = min(y11, y12), max(y11, y12)
        y2 = min(y21, y22), max(y21, y22)
        z1 = min(z11, z12), max(z11, z12)
        z2 = min(z21, z22), max(z21, z22)
        if z1[0] > z2[1] and get_overlap(x1, x2) and get_overlap(y1, y2):
            if z2[1] == max_z:
                top2bot[i].add(j)
            elif z2[1] > max_z:
                top2bot[i] = {j}

            max_z = max(z2[1], max_z)
    if z11 > z12:
        settled[i] = (x11, y11, max_z + z11 - z12 + 1, x12, y12, max_z + 1)
    else:
        settled[i] = (x11, y11, max_z + 1, x12, y12, max_z + z12 - z11 + 1)

print(top2bot)
not_disintegrated = set(v.pop() for v in top2bot.values() if len(v) == 1)
print(not_disintegrated)
print(len(top2bot) - len(not_disintegrated))
