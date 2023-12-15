from aocd import get_data
from collections import OrderedDict

year=2023
day=15

dat = get_data(year=year, day=day, block=True)

dat2 = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''


def hasher(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res


hm = {i: {} for i in range(256)}

for s in dat.split(','):
    if '-' in s:
        ss = s[:-1]
        hm[hasher(ss)].pop(ss, None)
    else:
        ss, val = s.split('=')
        hm[hasher(ss)][ss] = val

print(sum((k+1) * (i+1) * int(fl) for k, v in hm.items() for i, (ss, fl) in enumerate(v.items())))
