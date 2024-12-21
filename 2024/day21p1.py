# NOTE: this solution is quite suboptimal; this is my initial approach and the one I showed in part 1 of my video
# for an optimal solution, just take part 2 and change the 25 to 2

from collections import deque
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

total = 0

for line in open(0).read().splitlines():
    robot1 = solve(line, num_seqs)
    next = robot1
    for _ in range(2):
        possible_next = []
        for seq in next:
            possible_next += solve(seq, dir_seqs)
        minlen = min(map(len, possible_next))
        next = [seq for seq in possible_next if len(seq) == minlen]
    total += len(next[0]) * int(line[:-1])

print(total)