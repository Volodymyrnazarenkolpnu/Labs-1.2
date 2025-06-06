"""lab1, task1, level3, variant3"""
import random

lst1 = []
for i in range(random.randint(12,18)):
    lst1.append(random.randint(0,100))
##lst1= [-1,-10,-5,7,3,5,8,9,10,0,0,1,2,3,0]
##uncomment for test
print(lst1)
def find_longest_peak(lst):
    """checks for longest peak"""
    found = {}
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
                    _len = end - start + 1
                    found[start] = _len
                    decreasing = False
                    start = idx - 1
                    peak = 0
                else:
                    _len = end - start + 1
                    found[start] = _len
                    decreasing = False
                    start = idx - 1
                    peak = 0
        else:
            if decreasing and increasing:
                end = idx - 1
                if peak - start >= end - peak:
                    _len = end - start + 1
                    found[start] = _len
                    decreasing = False
                    start = idx - 1
                    peak = 0
                else:
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
    peak_sequences = []
    for idx in range(0, len(_mxl)):
        peak_sequences.append(lst[_ell[idx]:_ell[idx] + _mxl[idx]])
    _idx = 0
    max_length_start = _ell[_mxl.index(max(_mxl))]
    print("Peaks of the sequence:")
    for seq in peak_sequences:
        print(seq)
        print("Length = " + str(_mxl[_idx]))
        if _mxl[_idx] == max_length:
            print("Longest!")
        _idx += 1
    return lst[max_length_start:max_length_start + max_length]

def find_longest_pit(lst):
    """checks for longest peak"""
    found = {}
    end = 1
    increasing = False
    decreasing = False
    start = 0
    peak = 0
    for idx in range(end, len(lst)):
        if lst[idx] > lst[idx - 1]:
            if decreasing and not increasing:
                peak = idx - 1
                increasing = True
            if idx == len(lst) - 1 and increasing:
                end = idx
                if peak - start >= end - peak:
                    _len = end - start + 1
                    found[start] = _len
                    increasing = False
                    start = idx - 1
                    peak = 0
                else:
                    _len = end - start + 1
                    found[start] = _len
                    increasing = False
                    start = idx - 1
                    peak = 0
        else:
            if decreasing and increasing:
                end = idx - 1
                if peak - start >= end - peak:
                    _len = end - start + 1
                    found[start] = _len
                    increasing = False
                    start = idx - 1
                    peak = 0
                else:
                    _len = end - start + 1
                    found[start] = _len
                    increasing = False
                    start = idx - 1
                    peak = 0
            elif not increasing and not decreasing and lst[idx] < lst[idx - 1]:
                decreasing = True
                start = idx - 1
            elif lst[idx] == lst[idx - 1]:
                decreasing = False
    _mxl = []
    _ell = []
    for st in found.items():
        _mx = st[1]
        _el = st[0]
        _ell.append(_el)
        _mxl.append(_mx)
    max_length = max(_mxl)
    peak_sequences = []
    for idx in range(0, len(_mxl)):
        peak_sequences.append(lst[_ell[idx]:_ell[idx] + _mxl[idx]])
    _idx = 0
    max_length_start = _ell[_mxl.index(max(_mxl))]
    print("Pits of the sequence:")
    for seq in peak_sequences:
        print(seq)
        print("Length = " + str(_mxl[_idx]))
        if _mxl[_idx] == max_length:
            print("Longest!")
        _idx += 1
    return lst[max_length_start:max_length_start + max_length]
find_longest_peak(lst1)
find_longest_pit(lst1)
##todo:графік
