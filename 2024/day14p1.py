import re

WIDTH = 101
HEIGHT = 103

robots = []

for line in open(0):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

result = []

for px, py, vx, vy in robots:
    result.append(((px + vx * 100) % WIDTH, (py + vy * 100) % HEIGHT))

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

print(tl * bl * tr * br)