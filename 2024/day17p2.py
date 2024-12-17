import re

program = list(map(int, re.findall(r"\d+", open(0).read())[3:]))
assert program[-2:] == [3, 0], "program does not end with JNZ 0"

def find(target, ans):
    if target == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None
        adv3 = False

        def combo(operand):
            if 0 <= operand <= 3: return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c
            raise AssertionError(f"unrecognized combo operand {operand}")

        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 0:
                assert not adv3, "program has multiple ADVs"
                assert operand == 3, "program has ADV with operand other than 3"
                adv3 = True
            elif ins == 1:
                b = b ^ operand
            elif ins == 2:
                b = combo(operand) % 8
            elif ins == 3:
                raise AssertionError("program has JNZ inside expected loop body")
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                assert output is None, "program has multiple OUT"
                output = combo(operand) % 8
            elif ins == 6:
                b = a >> combo(operand)
            elif ins == 7:
                c = a >> combo(operand)
            if output == target[-1]:
                sub = find(target[:-1], a)
                if sub is None: continue
                return sub

print(find(program, 0))