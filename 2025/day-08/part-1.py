import math

boxes = [list(map(int, line.split(","))) for line in open(0)]
edges = [(i, j) for i in range(len(boxes)) for j in range(i + 1, len(boxes))]
edges.sort(key=lambda x: math.hypot(*[a - b for a, b in zip(boxes[x[0]], boxes[x[1]])]))

parent = list(range(len(boxes)))

def root(x):
    if parent[x] == x: return x
    parent[x] = root(parent[x])
    return parent[x]

def merge(a, b):
    parent[root(a)] = root(b)

for a, b in edges[:1000]:
    merge(a, b)

sizes = [0] * len(boxes)

for box in range(len(boxes)):
    sizes[root(box)] += 1

sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])