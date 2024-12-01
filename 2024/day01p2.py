l, r = list(map(list, zip(*[list(map(int, line.split())) for line in open(0).read().splitlines()])))
print(sum(x * r.count(x) for x in l))