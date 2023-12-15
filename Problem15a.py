from aocd import get_data

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


print(sum(hasher(s) for s in dat.split(',')))
