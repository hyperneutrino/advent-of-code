total = 0

def can_obtain(target, array):
    if len(array) == 1: return target == array[0]
    if target % array[-1] == 0 and can_obtain(target // array[-1], array[:-1]): return True
    if target > array[-1] and can_obtain(target - array[-1], array[:-1]): return True
    s_target = str(target)
    s_last = str(array[-1])
    if s_target.endswith(s_last) and len(s_target) > len(s_last) and can_obtain(int(s_target[:-len(s_last)]), array[:-1]): return True
    return False

for line in open(0):
    l, r = line.split(": ")
    target = int(l)
    array = [int(x) for x in r.split()]
    if can_obtain(target, array):
        total += target

print(total)