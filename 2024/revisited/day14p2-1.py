import re

WIDTH = 101
HEIGHT = 103

robots = []

for line in open(0):
    robots.append(list(map(int, re.findall(r"-?\d+", line))))

initial = list(map(list, robots))

min_variance = float("inf")
best_iteration = None

for second in range(WIDTH * HEIGHT):
    mean_x = sum(px for px, _, _, _ in robots) / len(robots)
    mean_y = sum(py for _, py, _, _ in robots) / len(robots)

    sos = 0

    for px, py, _, _ in robots:
        sos += (px - mean_x) ** 2 + (py - mean_y) ** 2

    var = sos / len(robots)

    if var < min_variance:
        min_variance = var
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