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

circuits = len(boxes)

for a, b in edges:
    if root(a) == root(b): continue
    merge(a, b)
    circuits -= 1
    if circuits == 1:
        print(boxes[a][0] * boxes[b][0])
        break