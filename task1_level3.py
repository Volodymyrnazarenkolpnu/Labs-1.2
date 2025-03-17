"""lab2, task1, level3, variant3"""
import random
# N = random.randint(2,100)
# free_spaces = []
# for sec in range(N):
#     xN = random.randint(0, 1000)
#     if not xN in free_spaces:
#         free_spaces.append(xN)
# c = random.randint(0, N)
# print(N)
# print(free_spaces)
# print(c)
def find_min_spaces(lst: list, cw):
    """finds a smallest amount of spaces between cows"""
    lst.sort()
    cows = cw
    pos = lst[0]
    start = lst[0]
    lst.pop(0)
    smallest = 0
    overflow = False
    for i in range(2,max(lst)):
        _temp = lst[:]
        pos = start
        for cownum in range(1,cows):
            if len(_temp) == 0:
                overflow = True
            for _idx2 in _temp:
                if _idx2 >= pos + i:
                    pos = _idx2
                    _temp = _temp[_temp.index(_idx2) + 1:]
                    break
                elif lst.index(_idx2) == len(lst) - 1:
                    overflow = True
            if overflow:
                break
        if overflow:
            smallest = i - 1
            break
    return smallest
print(find_min_spaces([2,6,8,10],4))