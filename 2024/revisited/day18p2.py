from collections import deque

s = 71

walls = [tuple(map(int, line.split(","))) for line in open(0)]

wset = set(walls)
seen = set(wset)

parent_grid = [[None] * s for _ in range(s)]

for r in range(s):
    for c in range(s):
        if (r, c) in seen: continue
        search = {(r, c)}
        seen.add((r, c))
        while search:
            cr, cc = search.pop()
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if nr < 0 or nc < 0 or nr >= s or nc >= s: continue
                if (nr, nc) in seen: continue
                search.add((nr, nc))
                seen.add((nr, nc))
                parent_grid[nr][nc] = (r, c)

def find(r, c):
    parent = parent_grid[r][c]
    if parent is None:
        return (r, c)
    parent_grid[r][c] = find(*parent)
    return parent_grid[r][c]

def union(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)
    if (r1, c1) == (r2, c2): return
    parent_grid[r2][c2] = (r1, c1)

last_blocking_coords = None

for wr, wc in walls[::-1]:
    wset.remove((wr, wc))

    for nr, nc in [(wr - 1, wc), (wr + 1, wc), (wr, wc - 1), (wr, wc + 1)]:
        if nr < 0 or nc < 0 or nr >= s or nc >= s: continue
        if (nr, nc) in wset: continue
        union(wr, wc, nr, nc)
    
    if find(0, 0) == find(s - 1, s - 1):
        print(f"{wr},{wc}")
        break