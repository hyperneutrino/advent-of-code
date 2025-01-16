from collections import Counter

a = []
b = []

for line in open(0):
    x, y = map(int, line.split())
    a.append(x)
    b.append(y)

a_counts = Counter(a)
b_counts = Counter(b)

total = 0

for x in a_counts:
    total += x * a_counts[x] * b_counts[x]

print(total)