fn = 'inputs/input1.txt'
digits = '0123456789'

with open(fn, 'r') as f:
    input = [x.strip() for x in f.readlines()]

out = 0
for row in input:
    n = len(row)
    i1, d1 = next((i, d) for i, d in enumerate(row) if d in digits)
    i2, d2 = next((n-i, d) for i, d in enumerate(row[::-1]) if d in digits)
    if i1 is None:
        out = out
    elif i1 == i2:
        out += int(d1)
    else:
        out += int(d1) * 10 + int(d2)

print(out)
