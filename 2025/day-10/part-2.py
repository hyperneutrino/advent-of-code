import re, z3

total = 0

for line in open(0):
    match = re.match(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$", line.strip())
    _, buttons, joltages = match.groups()
    buttons = [set(map(int, button[1:-1].split(","))) for button in buttons.split()]
    joltages = list(map(int, joltages.split(",")))
    o = z3.Optimize()
    vars = z3.Ints(f"n{i}" for i in range(len(buttons)))
    for var in vars: o.add(var >= 0)
    for i, joltage in enumerate(joltages):
        equation = 0
        for b, button in enumerate(buttons):
            if i in button:
                equation += vars[b]
        o.add(equation == joltage)
    o.minimize(sum(vars))
    o.check()
    total += o.model().eval(sum(vars)).as_long()

print(total)