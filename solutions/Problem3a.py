import regex as re


def main(data):
    out = 0
    for i, row in enumerate(data):
        matches = re.finditer(r'\d+', row)
        for match in matches:
            start = match.start() - 1
            end = match.end() + 1

            found = any([re.search(r'[^\d|\\.]', data[i-z][start:end]) for z in [-1, 0, 1]])
            if found:
                out += int(match.group())
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
