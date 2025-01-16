a = []
b = []

for line in open(0):
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()

total = 0

for x, y in zip(a, b):
    total += abs(x - y)

print(total)