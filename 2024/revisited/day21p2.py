from collections import deque
from functools import cache
from itertools import product

def compute_seqs(keypad):
    pos = []
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is None: ir, ic = r, c
            else: pos.append((r, c))
    seqs = {}
    for rx, cx in pos:
        for ry, cy in pos:
            x = keypad[rx][cx]
            y = keypad[ry][cy]
            dr = ry - rx
            dc = cy - cx
            usd = "^" * -dr + "<" * -dc + ">" * dc + "v" * dr + "A"
            dsu = "v" * dr + "<" * -dc + ">" * dc + "^" * -dr + "A"
            ap, sp = (usd, dsu) if keypad == num_keypad else (dsu, usd)
            seqs[(x, y)] = [ap]
            if dr != 0 and dc != 0 and (rx != ir and cx != ic or ry != ir and cy != ic):
                seqs[(x, y)].append(sp)
    return seqs

def solve(string, seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]

num_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

num_seqs = compute_seqs(num_keypad)

dir_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

dir_seqs = compute_seqs(dir_keypad)
dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}

@cache
def compute_length(seq, depth=25):
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(compute_length(subseq, depth - 1) for subseq in dir_seqs[(x, y)])
    return length

total = 0

for line in open(0).read().splitlines():
    inputs = solve(line, num_seqs)
    length = min(map(compute_length, inputs))
    total += length * int(line[:-1])

print(total)