grid = list(map(list, open(0).read().splitlines()))

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            break
    else:
        continue
    break

dr = -1
dc = 0

seen = set()

while True:
    seen.add((r, c))
    if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols: break
    if grid[r + dr][c + dc] == "#":
        dc, dr = -dr, dc
    else:
        r += dr
        c += dc

print(len(seen))