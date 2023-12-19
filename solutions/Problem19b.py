from aoc_utils import *
from aocd import get_data
import regex as re
# import numpy as np

year=2023
day=19

dat = get_data(year=year, day=day, block=True)

# 167409079868000
dat2 = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''


workflows, ratings = parse(dat.split('\n\n')[0]), parse(dat.split('\n\n')[1])

wint = {}

for workflow in workflows:
    wname = workflow.split('{')[0]

    instructions = []
    for instruction in re.match(r'\w+{(.*)}', workflow).group(1).split(','):
        z = re.match(r'(\w+)([<>])(\d+):(\w+)', instruction)
        if not z:
            instructions.append(('y', '<', 4001, instruction))
            break
        r, sig, threshold, loc = z.groups()
        instructions.append((r, sig, int(threshold), loc))
    wint[wname] = instructions


def prod_ublb(d):
    return prod(max(0, ub - lb + 1) for k, (lb, ub) in d.items() if k != 'y')


def count_valid(ratings, curr='in'):
    if curr == 'A': return prod_ublb(ratings)
    if curr == 'R': return 0

    out = 0
    for r, sig, threshold, loc in wint[curr]:
        lb, ub = ratings.get(r, (1, m))

        if sig == '<':
            accepted = (lb, threshold - 1)
            rejected = (threshold, ub)
        elif sig == '>':
            rejected = (lb, threshold)
            accepted = (threshold + 1, ub)
        else:
            raise

        accepted_ratings = ratings.copy()
        accepted_ratings[r], ratings[r] = accepted, rejected
        out += count_valid(accepted_ratings.copy(), loc)

    return out


m = 4000
ratings = {'x': (1, m), 'm': (1, m), 'a': (1, m), 's': (1, m), }
out = count_valid(ratings)

print(out)
