from aoc_utils import *
from aocd import get_data
from collections import defaultdict
import random, copy


year=2023
day=25

dat = get_data(year=year, day=day, block=True)

# 54
dat2 = '''jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr'''

dat = parse(dat, words)
print(dat)

G = defaultdict(list)
for r in dat:
    for c in r[1:]:
        G[r[0]].append(c)
        G[c].append(r[0])

# https://web.stanford.edu/class/archive/cs/cs161/cs161.1172/CS161Lecture16.pdf
# https://stackoverflow.com/questions/23825200/karger-min-cut-algorithm-in-python-2-7#:~:text=This%20algorithm%20chooses%20a%20node,between%20two%20high%20degree%20nodes.
def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2


def karger(G):
    length = []
    R = {v: set() for v in G}
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
        R[v1].add(v2)
        R[v1].update(R[v2])
        del R[v2]

        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    return length[0], prod([len(v)+1 for v in R.values()])


def operation():
    min_cut = -1
    while min_cut != 3:
        min_cut, res = karger(copy.deepcopy(G))
    return res


print(operation())
