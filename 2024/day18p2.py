from collections import deque

s = 70

coords = [list(map(int, line.split(","))) for line in open(0)]

def connected(n):
    grid = [[0] * (s + 1) for _ in range(s + 1)]

    for c, r in coords[:n]:
        grid[r][c] = 1

    q = deque([(0, 0)])
    seen = {(0, 0)}

    while q:
        r, c = q.popleft()
        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr > s or nc > s: continue
            if grid[nr][nc] == 1: continue
            if (nr, nc) in seen: continue
            if nr == nc == s: return True
            seen.add((nr, nc))
            q.append((nr, nc))

    return False

lo = 0
hi = len(coords) - 1

while lo < hi:
    mi = (lo + hi) // 2
    if connected(mi + 1):
        lo = mi + 1
    else:
        hi = mi

print(*coords[lo], sep=",")