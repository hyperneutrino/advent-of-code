from functools import cache

lines = open(0).read().splitlines()

patterns = set(lines[0].split(", "))
maxlen = max(map(len, patterns))

@cache
def num_possibilities(design):
    if design == "": return 1
    count = 0
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns:
            count += num_possibilities(design[i:])
    return count

print(sum(num_possibilities(design) for design in lines[2:]))