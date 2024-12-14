import re

WIDTH = 101
HEIGHT = 103

robots = []

for line in open(0):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

min_sf = float("inf")
best_iteration = None

for second in range(WIDTH * HEIGHT):
    result = []

    for px, py, vx, vy in robots:
        result.append(((px + vx * second) % WIDTH, (py + vy * second) % HEIGHT))

    tl = bl = tr = br = 0

    VM = (HEIGHT - 1) // 2
    HM = (WIDTH - 1) // 2

    for px, py in result:
        if px == HM or py == VM: continue
        if px < HM:
            if py < VM:
                tl += 1
            else:
                bl += 1
        else:
            if py < VM:
                tr += 1
            else:
                br += 1

    sf = tl * bl * tr * br
    
    if sf < min_sf:
        min_sf = sf
        best_iteration = second

print(best_iteration)