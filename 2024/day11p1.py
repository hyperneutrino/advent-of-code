stones = [int(x) for x in input().split()]

for _ in range(25):
    output = []
    for stone in stones:
        if stone == 0:
            output.append(1)
            continue
        string = str(stone)
        length = len(string)
        if length % 2 == 0:
            output.append(int(string[:length // 2]))
            output.append(int(string[length // 2:]))
        else:
            output.append(stone * 2024)
    stones = output

print(len(stones))