from aoc_utils import *
from aocd import submit, get_data

year=2023
day=5

dat = get_data(year=year, day=day, block=True)

# 35
dat = '''seeds: 1, 2, 3, 4, 5, 6, 7, 8, 9, 48, 49, 50, 51, 52, 53, 54

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


dat = parse(dat, atoms)

seeds = dat[0][1:]

maps = {}
map_from = ''
map_to = ''
from_to = {}
for inp in dat[2:]:
    if not len(inp): continue
    if inp[1] == 'to':
        map_from = inp[0]
        map_to = inp[2]
        maps[map_to] = []

        from_to[map_from] = map_to
    else:

        dest = range(inp[0], inp[0] + inp[2] + 1)
        src = range(inp[1], inp[1] + inp[2] + 1)

        maps[map_to].append((inp[0], inp[1], inp[2]))


def get_map(dest, val):
    return next((d + (val - s) for d, s, r in maps[dest] if s <= val < s + r), val)

print(maps)
src = 'seed'
out = 10e100000


def get_loc(src, v):

    if src == 'location':
        return v
    dest = from_to[src]

    return get_loc(dest, get_map(dest, v))


for seed in seeds:
    res = get_loc('seed', seed)
    if out > res:
        out = res

print(out)
