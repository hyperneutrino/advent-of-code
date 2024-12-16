from collections import deque
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
lowest_cost = {(sr, sc, 0, 1): 0}
backtrack = {}
best_cost = float("inf")
end_states = set()

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    if cost > lowest_cost.get((r, c, dr, dc), float("inf")): continue
    if grid[r][c] == "E":
        if cost > best_cost: break
        best_cost = cost
        end_states.add((r, c, dr, dc))
    for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == "#": continue
        lowest = lowest_cost.get((nr, nc, ndr, ndc), float("inf"))
        if new_cost > lowest: continue
        if new_cost < lowest:
            backtrack[(nr, nc, ndr, ndc)] = set()
            lowest_cost[(nr, nc, ndr, ndc)] = new_cost
        backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
        heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

states = deque(end_states)
seen = set(end_states)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen: continue
        seen.add(last)
        states.append(last)

print(len({(r, c) for r, c, _, _ in seen}))