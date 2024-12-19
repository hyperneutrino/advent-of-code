from functools import cache

lines = open(0).read().splitlines()

patterns = set(lines[0].split(", "))
maxlen = max(map(len, patterns))

@cache
def can_obtain(design):
    if design == "": return True
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns and can_obtain(design[i:]):
            return True
    return False

print(sum(1 if can_obtain(design) else 0 for design in lines[2:]))