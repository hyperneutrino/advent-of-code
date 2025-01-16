import re

memory = re.sub(r"don't\(\).*?(do\(\)|$)", "", open(0).read(), flags=re.DOTALL)

total = 0

for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory):
    total += int(x) * int(y)

print(total)