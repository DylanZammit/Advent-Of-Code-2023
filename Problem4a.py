fn = 'inputs/input4.txt'

with open(fn, 'r') as f:
    input = {int(x.split(':', 1)[0].strip().split()[1]): x.split(':', 1)[1].strip() for x in f.readlines()}
    input = {k: {'winning': set([int(x.strip()) for x in v.split('|')[0].split()]), 'showing': set([int(x.strip()) for x in v.split('|')[1].split()])} for k, v in input.items()}

output = {k: int(2**(len(v['winning'].intersection(v['showing']))-1)) for k, v in input.items()}
aoutput = {k: (v['winning'] - v['showing']) for k, v in input.items()}
print(sum(output.values()))
