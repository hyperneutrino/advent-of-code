a = list(map(list, zip(*[list(map(int, line.split())) for line in open(0).read().splitlines()])))

for k in a: k.sort()

print(sum(abs(x - y) for x, y in zip(*a)))