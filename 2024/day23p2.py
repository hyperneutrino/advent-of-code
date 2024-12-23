edges = [line.strip().split("-") for line in open(0)]
conns = {}

for x, y in edges:
    if x not in conns: conns[x] = set()
    if y not in conns: conns[y] = set()
    conns[x].add(y)
    conns[y].add(x)

sets = set()

def search(node, req):
    key = tuple(sorted(req))
    if key in sets: return
    sets.add(key)
    for neighbor in conns[node]:
        if neighbor in req: continue
        if not all(neighbor in conns[query] for query in req): continue
        search(neighbor, {*req, neighbor})

for x in conns:
    search(x, {x})

print(",".join(sorted(max(sets, key=len))))