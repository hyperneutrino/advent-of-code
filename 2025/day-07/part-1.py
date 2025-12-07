from collections import deque

grid = [list(line.strip()) for line in open(0)]

S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]
beams = deque([S])
seen = {S}

def add(r, c):
    if (r, c) in seen: return
    seen.add((r, c))
    beams.append((r, c))

count = 0

while len(beams) > 0:
    r, c = beams.popleft()
    if grid[r][c] == "." or grid[r][c] == "S":
        if r == len(grid) - 1: continue
        add(r + 1, c)
    elif grid[r][c] == "^":
        count += 1
        add(r, c - 1)
        add(r, c + 1)

print(count)