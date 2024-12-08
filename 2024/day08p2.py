grid = [line.strip() for line in open(0)]

rows = len(grid)
cols = len(grid[0])

antennas = {}

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != ".":
            if char not in antennas: antennas[char] = []
            antennas[char].append((r, c))

antinodes = set()

for array in antennas.values():
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j: continue
            r1, c1 = array[i]
            r2, c2 = array[j]
            dr = r2 - r1
            dc = c2 - c1
            r = r1
            c = c1
            while 0 <= r < rows and 0 <= c < cols:
                antinodes.add((r, c))
                r += dr
                c += dc
            # antinodes.add((2 * r1 - r2, 2 * c1 - c2))
            # antinodes.add((2 * r2 - r1, 2 * c2 - c1))

print(len(antinodes))