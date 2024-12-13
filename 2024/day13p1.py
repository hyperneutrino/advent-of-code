import re

total = 0

for block in open(0).read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
    if ca % 1 == cb % 1 == 0:
        if ca <= 100 and cb <= 100:
            total += int(ca * 3 + cb)

print(total)