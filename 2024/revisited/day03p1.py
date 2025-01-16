import re

memory = open(0).read()

total = 0

for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory):
    total += int(x) * int(y)

print(total)