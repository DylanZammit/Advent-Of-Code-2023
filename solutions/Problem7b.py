from aoc_utils import *
from aocd import get_data
from collections import Counter

year=2023
day=7

dat = get_data(year=year, day=day, block=True)

# 5905
dat2 = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
dat = parse(dat, atom)


cards = 'AKQT98765432J'
cards = {c: i for i, c in enumerate(cards[::-1], start=2)}

ranks = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]

def hand_val(hand):
    return sum([cards[h] * 13 ** i for i, h in enumerate(hand[::-1])])


ranking = {i: [] for i in range(len(ranks))}

for hand_bid in dat:
    hand, bid = hand_bid.split()
    bid = int(bid)

    c = Counter(hand)

    if c.get('J') not in [None, 5]:
        js = c.pop('J')
        c[max(c, key=c.get)] += js

    val = ranks.index(sorted(c.values()))
    ranking[val].append((hand, hand_val(hand), bid))

final_ranking = []
for i in range(7):
    final_ranking += sorted(ranking[i], key=lambda x: x[1], reverse=True)

print(sum([i * x[2] for i, x in enumerate(final_ranking[::-1], start=1)]))
