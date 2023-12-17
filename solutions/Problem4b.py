fn = 'inputs/input4.txt'
with open(fn, 'r') as f:
    input = {int(x.split(':', 1)[0].strip().split()[1]): x.split(':', 1)[1].strip() for x in f.readlines()}
    input = {k: {'winning': set([int(x.strip()) for x in v.split('|')[0].split()]), 'showing': set([int(x.strip()) for x in v.split('|')[1].split()])} for k, v in input.items()}

matching = {k: len(v['winning'].intersection(v['showing'])) for k, v in input.items()}
scores = list(matching.values())
n = len(scores)
cards = {i: 1 for i in range(1, n + 1)}
scores = {i: score for i, score in enumerate(scores, start=1)}

out = len(scores)
for i, score in scores.items():
    for j in range(1, score + 1):
        if i + j in cards:
            cards[i + j] += cards[i]

print(sum(cards.values()))
