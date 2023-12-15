import regex as re
from aocd import get_data
import re
from functools import cache

year=2023
day=12

dat = get_data(year=year, day=day, block=True)


# 525152
dat2 = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

dat = dat.split('\n')

dat = [tuple(r.split()) for r in dat]
dat = [(((x+'?')*5)[:-1], ((y+',')*5)[:-1]) for x, y in dat]
dat = [(x.strip('.'), tuple(int(g) for g in y.split(','))) for x, y in dat]


@cache
def g_next(part, grps):
    res = 0

    pattern = r'^\.*' + r'\.+'.join([rf'#{{{g}}}' for g in grps]) + r'\.*$'
    if len(grps) == 0 and '#' in part: return 0
    if re.match(pattern, part.replace('?', '.')) or re.match(pattern, part.replace('?', '#')):
        return 1

    grp = grps[0]
    pattern = rf'^\.*#{{{grp}}}\.'

    done_already = re.match(pattern, part)

    if done_already: return g_next(part[done_already.end():], grps[1:])

    pattern = rf'^[#?]{{{grp}}}([^#]|$)'

    if '?' not in part and '#' not in part: return 0
    next_q = part.index('?') if '?' in part else 10e100
    next_h = part.index('#') if '#' in part else 10e100

    if next_h < next_q:
        z = re.match(pattern, part[next_h:])
        return g_next(part[next_h + z.end():], grps[1:]) if z else 0

    for nq in re.finditer(r'\?', part):
        nqs = nq.start()
        if nqs > next_h:
            return res + g_next(part[next_h:], grps)
        z = re.match(pattern, part[nqs:])
        res += g_next(part[nqs + z.end():], grps[1:]) if z else 0

    return res


print(sum((g_next(x, y)) for x, y in dat))
