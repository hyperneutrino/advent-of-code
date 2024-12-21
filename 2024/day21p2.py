from collections import deque
from functools import cache
from itertools import product

def compute_seqs(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r, c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            possibilities = []
            q = deque([(pos[x], "")])
            optimal = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
                    if keypad[nr][nc] is None: continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1: break
                        optimal = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break
            seqs[(x, y)] = possibilities
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