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

def loops(grid, r, c):
    dr = -1
    dc = 0

    seen = set()

    while True:
        seen.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols: return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in seen:
            return True

count = 0

for cr in range(rows):
    for cc in range(cols):
        if grid[cr][cc] != ".": continue
        grid[cr][cc] = "#"
        if loops(grid, r, c):
            count += 1
        grid[cr][cc] = "."

print(count)