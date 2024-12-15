top, bottom = open(0).read().split("\n\n")

expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}

grid = [list("".join(expansion[char] for char in line)) for line in top.splitlines()]
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
    go = True
    for cr, cc in targets:
        nr = cr + dr
        nc = cc + dc
        if (nr, nc) in targets: continue
        char = grid[nr][nc]
        if char == "#":
            go = False
            break
        if char == "[":
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        if char == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))
    if not go: continue
    copy = [list(row) for row in grid]
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        grid[br][bc] = "."
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = copy[br][bc]
    r += dr
    c += dc

print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "["))