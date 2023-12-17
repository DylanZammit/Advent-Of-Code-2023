def main(input):
    out = 0
    for game_id, res in input.items():

        min_cols = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for showing in res:
            for col in min_cols:
                min_cols[col] = max([min_cols[col], showing.get(col, 0)])
        power = (min_cols['red'] * min_cols['green'] * min_cols['blue'])

        out += power
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
