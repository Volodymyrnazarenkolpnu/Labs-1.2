"""lab1, task1, level3, variant3"""
import unittest
import random

lst = []
for i in range(random.randint(12,18)):
    lst.append(random.randint(0,100))
print(lst)
def find_longest_peak(lst):
    """checks for longest peak"""
    found = {0:0,}
    working = True
    end = 1
    increasing = False
    decreasing = False
    start = 0
    peak = 0
    for idx in range(end, len(lst)):
        if lst[idx] < lst[idx - 1]:
            if increasing and not decreasing:
                peak = idx - 1
                decreasing = True
            if idx == len(lst) - 1 and decreasing:
                end = idx
                if peak - start >= end - peak:
                    start = peak - (end - peak)
                    _len = end - start + 1
                    found[start] = _len
                    decreasing = False
                    start = idx - 1
                    peak = 0
                else:
                    end = peak + (peak - start)
                    _len = end - start + 1
                    found[start] = _len
                    decreasing = False
                    start = idx - 1
                    peak = 0
        else:
            if decreasing and increasing:
                end = idx - 1
                if peak - start >= end - peak:
                    start = peak - (end - peak)
                    _len = end - start + 1
                    found[start] = _len
                    decreasing = False
                    start = idx - 1
                    peak = 0
                else:
                    end = peak + (peak - start)
                    _len = end - start + 1
                    found[start] = _len
                    decreasing = False
                    start = idx - 1
                    peak = 0
            elif not increasing and not decreasing and lst[idx] > lst[idx - 1]:
                increasing = True
                start = idx - 1
            elif lst[idx] == lst[idx - 1]:
                increasing = False
    _mxl = []
    _ell = []
    for st in found.items():
        _mx = st[1]
        _el = st[0]
        _ell.append(_el)
        _mxl.append(_mx)
    max_length = max(_mxl)
    max_length_start = _ell[_mxl.index(max(_mxl))]
    print(lst[max_length_start:max_length_start + max_length])
find_longest_peak(lst)

