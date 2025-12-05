ranges, numbers = open(0).read().split("\n\n")

ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
numbers = list(map(int, numbers.splitlines()))

count = 0

for number in numbers:
    for lo, hi in ranges:
        if lo <= number <= hi:
            count += 1
            break

print(count)