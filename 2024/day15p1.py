top, bottom = open(0).read().split("\n\n")

grid = [list(line) for line in top.splitlines()]
moves = bottom.replace("\n", "")

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            break
    else:
        continue
    break

for move in moves:
    dr = {"^": -1, "v": 1}.get(move, 0)
    dc = {"<": -1, ">": 1}.get(move, 0)
    targets = [(r, c)]
    cr = r
    cc = c
    go = True
    while True:
        cr += dr
        cc += dc
        char = grid[cr][cc]
        if char == "#":
            go = False
            break
        if char == "O":
            targets.append((cr, cc))
        if char == ".":
            break
    if not go: continue
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = "O"
    r += dr
    c += dc

print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "O"))