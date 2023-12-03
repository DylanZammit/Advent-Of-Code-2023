digits = '0123456789'
number_digit_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def replace_first_digit(word, rev=False):
    temp_number_digit_map = number_digit_map
    if rev:
        word = word[::-1]
        temp_number_digit_map = {k[::-1]: v for k, v in number_digit_map.items()}

    number_digit_pos = {}

    for number, digit in temp_number_digit_map.items():
        pos = word.find(number)
        if pos >= 0:
            number_digit_pos[number] = pos

    if not len(number_digit_pos):
        return word[::-1] if rev else word

    min_val = min(number_digit_pos.values())

    first_num = list(filter(lambda x: number_digit_pos[x] == min_val, number_digit_pos))[0]
    word = word.replace(first_num, temp_number_digit_map[first_num], 1)

    return word[::-1] if rev else word


def main(input):

    out = 0
    for orig_row in input:
        row = orig_row

        n = len(row)

        i1, d1 = next(((i, d) for i, d in enumerate(row) if d in digits), (n, ''))
        i2, d2 = next(((n-i, d) for i, d in enumerate(row[::-1]) if d in digits), (0, ''))

        left = replace_first_digit(orig_row[:i1])
        right = replace_first_digit(orig_row[i2:], rev=True)
        row = left + orig_row[i1:i2] + right

        i1, d1 = next(((i, d) for i, d in enumerate(row) if d in digits), (0, ''))
        i2, d2 = next(((n-i, d) for i, d in enumerate(row[::-1]) if d in digits), (n, ''))

        if i1 is None:
            num = 0
        elif i1 == i2:
            num = int(d1)
        else:
            num = int(d1) * 10 + int(d2)

        print(orig_row, row, num)
        out += num

    return out


if __name__ == '__main__':
    fn = 'inputs/input1.txt'
    # fn = 'inputs/input1_sample.txt'

    with open(fn, 'r') as f:
        input = [x.strip() for x in f.readlines()]

    res = main(input)
    print(res)
