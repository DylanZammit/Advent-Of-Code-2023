digits = '0123456789'
cols = ['blue', 'red', 'green']


def main(input):
    max_cols = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    out = 0
    for game_id, res in input.items():
        possible = True
        for showing in res:
            for col in max_cols:
                if showing.get(col, 0) > max_cols[col]:
                    possible = False
                    break
        if possible:
            out += game_id
    return out


if __name__ == '__main__':
    fn = 'inputs/input2.txt'
    # fn = 'inputs/input2_sample.txt'

    with open(fn, 'r') as f:
        input = {int(x.split(':', 1)[0].strip().split()[1]): x.split(':', 1)[1].strip().split(';') for x in f.readlines()}
        input = {k: [showing.strip().split(',') for showing in v] for k, v in input.items()}
        input = {k: [{col_ct.split()[1]: int(col_ct.split()[0].strip()) for col_ct in showing} for showing in v] for k, v in input.items()}

    res = main(input)
    print(res)
