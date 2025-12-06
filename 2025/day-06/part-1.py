lines = [line.strip().split() for line in open(0)]
cols = list(zip(*lines))

total = 0

for *nums, op in cols:
    total += eval(op.join(nums))

print(total)