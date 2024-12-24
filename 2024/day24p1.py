file = open(0)

known = {}

for line in file:
    if line.isspace(): break
    x, y = line.split(": ")
    known[x] = int(y)

formulas = {}

for line in file:
    x, op, y, z = line.replace(" -> ", " ").split()
    formulas[z] = (op, x, y)

operators = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
}

def calc(wire):
    if wire in known: return known[wire]
    op, x, y = formulas[wire]
    known[wire] = operators[op](calc(x), calc(y))
    return known[wire]

z = []
i = 0

while True:
    key = "z" + str(i).rjust(2, "0")
    if key not in formulas: break
    z.append(calc(key))
    i += 1

print(int("".join(map(str, z[::-1])), 2))