"""lab2, task1, level3, variant3"""
import random
N = random.randint(2,100000)
free_spaces = []
for sec in range(N):
    xN = random.randint(0, 1000000000)
    if not xN in free_spaces:
        free_spaces.append(xN)
c = random.randint(0, N)
# print(N)
# print(free_spaces)
# print(c)
def quicksort(lst2):
    less = []
    eq = []
    more = []

    if len(lst2) > 1:
        p = lst2[0]
        for x in lst2:
            if x < p:
                less.append(x)
            elif x == p:
                eq.append(x)
            elif x > p:
                more.append(x)
        return quicksort(less) + eq + quicksort(more)
    else:
        return lst2
def find_min_spaces(lst: list, cw):
    """finds a smallest amount of spaces between cows"""
    lst = quicksort(lst)
    cows = cw
    pos = lst[0]
    start = lst[0]
    lst.pop(0)
    smallest = 0
    overflow = False
    iters = 0
    left = 2
    right = max(lst)
    found = False
    while not found:
        overflow = False
        curr = (left + right)//2
        if abs(curr - left) <= 1:
            smallest = curr
            found = True
        _temp = lst[:]
        pos = start
        cow = 1
        for i in range(1,len(lst)):
            if _temp[i] - pos >= curr:
                pos = _temp[i]
                if cow == cows:
                    break
            elif i == len(lst) - 1:
                overflow = True
            if overflow:
                break
            cow += 1
        iters += 1
        print(iters)
        if overflow:
            right = curr
        else:
            left = curr
    return smallest
print(find_min_spaces(free_spaces, c))