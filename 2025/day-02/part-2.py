ranges = [list(map(int, item.split("-"))) for item in input().split(",")]
numbers = sum((list(range(a, b + 1)) for a, b in ranges), [])

total = 0

for num in numbers:
    s = str(num)
    for i in range(2, len(s) + 1):
        if len(s) % i == 0 and s[:len(s) // i] * i == s:
            total += num
            break

print(total)