total = 0

for line in open(0):
    bank = list(map(int, line.strip()))
    tens = max(bank[:-1])
    ones = max(bank[bank.index(tens) + 1:])
    total += tens * 10 + ones

print(total)