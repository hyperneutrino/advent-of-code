file = open(0)

rules = []

for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

cache = {}

for x, y in rules:
    cache[(x, y)] = True
    cache[(y, x)] = False

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and not cache[key]:
                return False
    return True

total = 0

for line in file:
    update = list(map(int, line.split(",")))
    if is_ordered(update):
        total += update[len(update) // 2]

print(total)