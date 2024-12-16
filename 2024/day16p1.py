import heapq

grid = [list(line.strip()) for line in open(0)]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

pq = [(0, sr, sc, 0, 1)]
seen = {(sr, sc, 0, 1)}

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        print(cost)
        break
    for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == "#": continue
        if (nr, nc, ndr, ndc) in seen: continue
        heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))