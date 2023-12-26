from aoc_utils import *
from aocd import get_data
from itertools import combinations
import numpy as np


year=2023
day=24

dat = get_data(year=year, day=day, block=True)

# 2
dat2 = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''

dat = parse(dat, ints)


class Path:
    def __init__(self, dat):
        self.pos = dat[:3]

        self.dir = dat[3:] / np.linalg.norm(dat[3:])
        self.dirxy = dat[3:5] / np.linalg.norm(dat[3:5])

        self.grad = dat[4] / dat[3]
        self.intercept = dat[1] - self.grad * dat[0]


def intersect(path1, path2):
    a, c = path1.grad, path1.intercept
    b, d = path2.grad, path2.intercept
    if a == b: return None

    p = ((d - c) / (a - b), a * (d - c) / (a - b) + c)
    return p


def normalise(vec):
    vec = np.array(vec)
    return vec / np.linalg.norm(vec)


def does_collide(path1, path2, min_range, max_range):

    p = intersect(path1, path2)
    if not p: return False

    ndir1 = normalise((p[0] - path1.pos[0], p[1] - path1.pos[1]))
    ndir2 = normalise((p[0] - path2.pos[0], p[1] - path2.pos[1]))

    if np.allclose(ndir1, path1.dirxy) and np.allclose(ndir2, path2.dirxy) \
            and min_range <= p[0] <= max_range and min_range <= p[1] <= max_range:
        return True

    return False


paths = [Path(r) for r in dat]

min_range = 200000000000000
max_range = 400000000000000

print(sum(1 for i, j in combinations(range(len(dat)), 2) if does_collide(paths[i], paths[j], min_range, max_range)))
