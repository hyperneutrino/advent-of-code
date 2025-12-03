total = 0

for line in open(0):
    bank = list(map(int, line.strip()))
    jolts = 0
    for index in range(11):
        digit = max(bank[:index - 11])
        bank = bank[bank.index(digit) + 1:]
        jolts = (jolts * 10) + digit
    jolts = (jolts * 10) + max(bank)
    total += jolts

print(total)