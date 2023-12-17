import regex as re
import numpy as np


def main(data):
    out = 0
    for i, row in enumerate(data[:-1]):
        matches = re.finditer(r'\*', row)
        for match in matches:
            start = match.start() - 1
            end = match.end() + 1

            digits_above = [m for m in re.finditer(r'\d+', data[i-1])]
            digits_same = [m for m in re.finditer(r'\d+', data[i])]
            digits_below = [m for m in re.finditer(r'\d+', data[i+1])]

            match_above = [int(m.group()) for m in digits_above if len(range(max(start, m.start()), min(end, m.end())))]
            match_same = [int(m.group()) for m in digits_same if len(range(max(start, m.start()), min(end, m.end())))]
            match_below = [int(m.group()) for m in digits_below if len(range(max(start, m.start()), min(end, m.end())))]

            all_matches = match_above + match_below + match_same
            if len(all_matches) == 2:
                print(all_matches)
                out += np.prod(all_matches)

    return out


if __name__ == '__main__':
    fn = 'inputs/input3.txt'
    # fn = 'inputs/input3_sample.txt'

    with open(fn, 'r') as f:
        data = ['.' + x.strip() + '.' for x in f.readlines()]
        n = len(data[0])
        data = ['.' * n] + data + ['.' * n]

    res = main(data)
    print(res)
