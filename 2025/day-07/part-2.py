from functools import cache

grid = [list(line.strip()) for line in open(0)]

S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]

@cache
def solve(r, c):
    if r >= len(grid): return 1
    
    if grid[r][c] == "." or grid[r][c] == "S":
        return solve(r + 1, c)
    elif grid[r][c] == "^":
        return solve(r, c - 1) + solve(r, c + 1)

print(solve(*S))