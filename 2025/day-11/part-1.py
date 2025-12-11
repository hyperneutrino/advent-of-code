from functools import cache

graph = {}

for line in open(0):
    src, dsts = line.strip().split(": ")
    graph[src] = dsts.split()

@cache
def count(src, dst):
    if src == dst: return 1
    return sum(count(x, dst) for x in graph.get(src, []))

print(count("you", "out"))