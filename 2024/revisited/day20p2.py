grid = [list(line.strip()) for line in open(0)]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break

path = [(r, c)]

while grid[r][c] != "E":
    grid[r][c] = "#"
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
        if grid[nr][nc] == "#": continue
        path.append((nr, nc))
        r = nr
        c = nc

count = 0

for i, (r, c) in enumerate(path):
    for j, (nr, nc) in enumerate(path[i + 101:]):
        radius = abs(r - nr) + abs(c - nc)
        if radius > 20: continue
        if j + 1 >= radius: count += 1

print(count)