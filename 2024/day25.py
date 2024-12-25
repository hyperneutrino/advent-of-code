locks = []
keys = []

for block in open(0).read().split("\n\n"):
    grid = list(zip(*block.splitlines()))
    if grid[0][0] == "#":
        locks.append([row.count("#") - 1 for row in grid])
    else:
        keys.append([row.count("#") - 1 for row in grid])

total = 0

for lock in locks:
    for key in keys:
        if all(x + y <= 5 for x, y in zip(lock, key)):
            total += 1

print(total)