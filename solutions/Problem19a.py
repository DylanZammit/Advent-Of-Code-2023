from aoc_utils import *
from aocd import get_data
import regex as re

year=2023
day=19

dat = get_data(year=year, day=day, block=True)

# 19114
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
            instructions.append(('y', '<', 1, instruction))
            break
        r, sig, threshold, loc = z.groups()
        instructions.append((r, sig, int(threshold), loc))
    wint[wname] = instructions


ratings = [{z.split('=')[0]: int(z.split('=')[1]) for z in rating[1:-1].split(',')} for rating in ratings]
[d.update({'y': 0}) for d in ratings]


def get_score(rating, curr='in'):
    for r, sig, threshold, loc in wint[curr]:
        if eval(f'{rating.get(r, -1)}{sig}{threshold}'):
            if loc == 'A': return True
            if loc == 'R': return False
            return get_score(rating, loc)


print(sum(sum(rating.values()) if get_score(rating) else 0 for rating in ratings))
