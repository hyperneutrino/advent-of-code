ranges = [list(map(int, item.split("-"))) for item in input().split(",")]
numbers = sum((list(range(a, b + 1)) for a, b in ranges), [])

total = 0

for num in numbers:
    s = str(num)
    if len(s) % 2 == 0 and s[:len(s) // 2] * 2 == s:
        total += num

print(total)