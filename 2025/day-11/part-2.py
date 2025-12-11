from functools import cache

graph = {}

for line in open(0):
    src, dsts = line.strip().split(": ")
    graph[src] = dsts.split()

@cache
def count(src, dst):
    if src == dst: return 1
    return sum(count(x, dst) for x in graph.get(src, []))

print(
    count("svr", "dac") * count("dac", "fft") * count("fft", "out") \
  + count("svr", "fft") * count("fft", "dac") * count("dac", "out")
)