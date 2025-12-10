points = [list(map(int, line.split(","))) for line in open(0)]
print(max((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) for i, (x1, y1) in enumerate(points) for x2, y2 in points[:i]))