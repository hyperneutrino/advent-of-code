grid = [list(line.strip()) for line in open(0)]

count = 0

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != "@": continue
        region = [subrow[max(0, c - 1):c + 2] for subrow in grid[max(0, r - 1):r + 2]]
        if sum(row.count("@") for row in region) <= 4:
            count += 1

print(count)