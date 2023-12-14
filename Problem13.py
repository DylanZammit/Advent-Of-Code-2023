from aocd import get_data

year=2023
day=13

dat = get_data(year=year, day=day, block=True)

# 400
dat2 = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''

dat = dat.split('\n' * 2)
dat = [d.split('\n') for d in dat]


def transpose(mat):
    nrow, ncol = len(mat), len(mat[0])

    mat_trans = [''] * ncol

    for i in range(nrow):
        for j in range(ncol):
            mat_trans[j] += mat[i][j]
    return mat_trans


def dist(x, y):
    diff = 0
    for a, b in zip(x, y):
        if a != b:
            diff += 1
            if diff > 1: return diff
    return diff


def check_reflect(pat, i):
    j = 0
    smudge = False  # set this to True for part 1
    while i - j >= 0 and i + j + 1 < len(pat):
        d = dist(pat[i - j], pat[i + j + 1])
        if d > 0:
            if smudge or d > 1: return False
            smudge = True
        j += 1
        if i + j + 1 >= len(pat) or i - j < 0:
            return smudge
    return False


def check(mat):
    for i, row in enumerate(mat):
        if check_reflect(mat, i):
            return i + 1
    return 0


print(sum((check(pat) * 100 + check(transpose(pat.copy()))) for pat in dat))