import re

WIDTH = 101
HEIGHT = 103

robots = []

for line in open(0):
    robots.append(list(map(int, re.findall(r"-?\d+", line))))

initial = list(map(list, robots))

max_cluster = 0
best_iteration = None

for second in range(WIDTH * HEIGHT):
    coords = set((x, y) for x, y, _, _ in robots)

    while coords:
        x, y = coords.pop()
        cluster = 1
        search = {(x, y)}
        while search:
            x, y = search.pop()
            for nx in [x - 1, x, x + 1]:
                for ny in [y - 1, y, y + 1]:
                    if nx == x and ny == y: continue
                    if (nx, ny) in coords:
                        cluster += 1
                        search.add((nx, ny))
                        coords.remove((nx, ny))
        if cluster > max_cluster:
            max_cluster = cluster
            best_iteration = second

    for robot in robots:
        px, py, vx, vy = robot
        robot[0] = (px + vx) % WIDTH
        robot[1] = (py + vy) % HEIGHT

coords = []

for px, py, vx, vy in initial:
    coords.append(((px + vx * best_iteration) % WIDTH, (py + vy * best_iteration) % HEIGHT))

mx = max(x for x, _ in coords)
my = max(y for _, y in coords)

grid = [[" "] * (mx + 1) for _ in range(my + 1)]

for x, y in coords:
    grid[y][x] = "#"

print("\n".join(map("".join, grid)))

print(best_iteration)