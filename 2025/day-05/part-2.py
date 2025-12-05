ranges, _ = open(0).read().split("\n\n")
ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
ranges.sort()

last = None
count = 0

for lo, hi in ranges:
    if last is None:
        last = (lo, hi)
    elif last[1] < lo:
        count += last[1] - last[0] + 1
        last = (lo, hi)
    else:
        last = (last[0], max(last[1], hi))

count += last[1] - last[0] + 1

print(count)