"""lab1, task1, level3, variant3"""
import random
import math

lst1 = []
for i in range(random.randint(12,18)):
    lst1.append(random.randint(-13,15))
print(lst1)
def find_longest_peak(lst):
    """checks for longest peak"""
    found = {0:0,}
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
    max_length_start = _ell[_mxl.index(max(_mxl))]
    print(lst[max_length_start:max_length_start + max_length])
    return (lst, found)

def graph_sequence(lst, found):
    """Makes a graphical representation of given sequence with its peaks"""
    height = 30
    width = 30
    graph = []
    center = math.floor((max(lst) + min(lst))/2)
    for line_num in range(center + (height // 2), center - (height // 2), -1):
        if not line_num == 0:
            _line = f"{line_num}"
            if abs(line_num) < 10:
                _line += "  "
            for _i in range(width):
                _line += "    "
        else:
            _line = "0  "
            for _i in range(width):
                _line += "---"
        graph.append(_line)
    #drawing points
    _idx = 3
    for point in lst:
        if point < center + height // 2 and point > center - height // 2:
            _line = graph[(height // 2 - point + center)]
            _new_line = _line[:_idx * 4] + "O" + _line[_idx * 4 + 1:]
            graph[(height // 2 - point + center)] = _new_line
        _idx += 1
    #drawing lines
    _idx = 3
    for i in enumerate(lst):
        i = i[0]
        if not i + 1 >= len(lst):
            if lst[i] > lst[i+1]:
                try:
                    if not (height // 2 - lst[i]) + center < 0:
                        if lst[i] - lst[i + 1] < 2:
                            _line = graph[(height // 2 - lst[i]) + center]
                            _new_line = _line[:_idx * 4 + 1] + "___" + _line[_idx * 4 + 4:]
                            graph[(height // 2 - lst[i] + center)] = _new_line
                        elif lst[i] - lst[i + 1] < 3:
                            _line = graph[(height // 2 - lst[i]) + center + 1]
                            _new_line = _line[:_idx * 4 + 1] + "\\__" + _line[_idx * 4 + 4:]
                            graph[(height // 2 - lst[i] + center) + 1] = _new_line
                        elif lst[i] - lst[i + 1] < 4:
                            _line = graph[(height // 2 - lst[i]) + center + 1]
                            _new_line = _line[:_idx * 4 + 1] + "\\_" + _line[_idx * 4 + 3:]
                            graph[(height // 2 - lst[i] + center) + 1] = _new_line
                            _line = graph[(height // 2 - lst[i]) + center + 2]
                            _new_line = _line[:_idx * 4 + 3] + "\\" + _line[_idx * 4 + 4:]
                            graph[(height // 2 - lst[i] + center) + 2] = _new_line
                        elif lst[i] - lst[i + 1] < 5:
                            _line = graph[(height // 2 - lst[i]) + center + 1]
                            _new_line = _line[:_idx * 4 + 1] + "\\" + _line[_idx * 4 + 2:]
                            graph[(height // 2 - lst[i] + center) + 1] = _new_line
                            _line = graph[(height // 2 - lst[i]) + center + 2]
                            _new_line = _line[:_idx * 4 + 2] + "\\" + _line[_idx * 4 + 3:]
                            graph[(height // 2 - lst[i] + center) + 2] = _new_line
                            _line = graph[(height // 2 - lst[i]) + center + 3]
                            _new_line = _line[:_idx * 4 + 3] + "\\" + _line[_idx * 4 + 4:]
                            graph[(height // 2 - lst[i] + center) + 3] = _new_line
                        else:
                            _line = graph[(height // 2 - lst[i]) + center + 1]
                            _new_line = _line[:_idx * 4 + 1] + "\\" + _line[_idx * 4 + 2:]
                            graph[(height // 2 - lst[i] + center) + 1] = _new_line
                            dist = lst[i] - lst[i + 1] - 3
                            for stick in range(dist):
                                _line = graph[(height // 2 - lst[i]) + center + 2 + stick]
                                _new_line = _line[:_idx * 4 + 2] + "|" + _line[_idx * 4 + 3:]
                                graph[(height // 2 - lst[i] + center) + 2 +  stick] = _new_line
                            _line = graph[(height // 2 - lst[i]) + center + 1 + dist]
                            _new_line = _line[:_idx * 4 + 2] + "\\" + _line[_idx * 4 + 3:]
                            graph[(height // 2 - lst[i] + center) + 1 + dist] = _new_line
                            _line = graph[(height // 2 - lst[i]) + center + 2 + dist]
                            _new_line = _line[:_idx * 4 + 3] + "\\" + _line[_idx * 4 + 4:]
                            graph[(height // 2 - lst[i] + center) + 2 + dist] = _new_line
                except:
                    _idx += 1
                    continue
            elif lst[i] < lst[i+1]:
                try:
                    if not (height // 2 - lst[i + 1]) + center < 0:
                        if lst[i+1] - lst[i] < 2:
                            _line = graph[(height // 2 - lst[i + 1]) + center]
                            _new_line = _line[:(_idx + 1) * 4 - 3] + "___" + _line[(_idx + 1) * 4 - 0:]
                            graph[(height // 2 - lst[i + 1] + center)] = _new_line
                        elif lst[i+1] - lst[i] < 3:
                            _line = graph[(height // 2 - lst[i + 1]) + center + 1]
                            _new_line = _line[:(_idx + 1) * 4 - 3] + "__/" + _line[(_idx + 1) * 4 - 0:]
                            graph[(height // 2 - lst[i + 1] + center) + 1] = _new_line
                        elif lst[i+1] - lst[i] < 4:
                            _line = graph[(height // 2 - lst[i + 1]) + center + 1]
                            _new_line = _line[:(_idx + 1) * 4 - 2] + "_/" + _line[(_idx + 1) * 4 - 0:]
                            graph[(height // 2 - lst[i + 1] + center) + 1] = _new_line
                            _line = graph[(height // 2 - lst[i + 1]) + center + 2]
                            _new_line = _line[:(_idx + 1) * 4 - 3] + "/" + _line[(_idx + 1) * 4 - 2:]
                            graph[(height // 2 - lst[i + 1] + center) + 2] = _new_line
                        elif lst[i+1] - lst[i] < 5:
                            _line = graph[(height // 2 - lst[i + 1]) + center + 1]
                            _new_line = _line[:(_idx + 1) * 4 - 1] + "/" + _line[(_idx + 1) * 4 - 0:]
                            graph[(height // 2 - lst[i + 1] + center) + 1] = _new_line
                            _line = graph[(height // 2 - lst[i + 1]) + center + 2]
                            _new_line = _line[:(_idx + 1) * 4 - 2] + "/" + _line[(_idx + 1) * 4 - 1:]
                            graph[(height // 2 - lst[i + 1] + center) + 2] = _new_line
                            _line = graph[(height // 2 - lst[i + 1]) + center + 3]
                            _new_line = _line[:(_idx + 1) * 4 - 3] + "/" + _line[(_idx + 1) * 4 - 2:]
                            graph[(height // 2 - lst[i + 1] + center) + 3] = _new_line
                        else:
                            _line = graph[(height // 2 - lst[i + 1]) + center + 1]
                            _new_line = _line[:(_idx + 1) * 4 - 1] + "/" + _line[(_idx + 1) * 4 - 0:]
                            graph[(height // 2 - lst[i + 1] + center) + 1] = _new_line
                            dist = lst[i+1] - lst[i] - 4
                            for stick in range(dist):
                                _line = graph[(height // 2 - lst[i + 1]) + center + 2 + stick]
                                _new_line = _line[:(_idx + 1) * 4 - 1] + "|" + _line[(_idx + 1) * 4 - 0:]
                                graph[(height // 2 - lst[i + 1] + center) + 2 + stick] = _new_line
                            _line = graph[(height // 2 - lst[i + 1]) + center + 2 + dist]
                            _new_line = _line[:(_idx + 1) * 4 - 2] + "/" + _line[(_idx + 1) * 4 - 1:]
                            graph[(height // 2 - lst[i + 1] + center) + 2 + dist] = _new_line
                            _line = graph[(height // 2 - lst[i + 1]) + center + 3 + dist]
                            _new_line = _line[:(_idx + 1) * 4 - 3] + "/" + _line[(_idx + 1) * 4 - 2:]
                            graph[(height // 2 - lst[i + 1] + center) + 3 + dist] = _new_line
                            
                except:
                    _idx +=1
                    continue
            else:
                try:
                    if not (height // 2 - lst[i + 1]) + center < 0:
                        _line = graph[(height // 2 - lst[i]) + center]
                        _new_line = _line[:_idx * 4 + 1] + "---" + _line[_idx * 4 + 4:]
                        graph[(height // 2 - lst[i] + center)] = _new_line
                except:
                    _idx += 1
                    continue
            _idx += 1
    infoline1 = ""
    infoline2 = ""
    line_num = 1
    _mxl = []
    _ell = []
    for st in found.items():
        _mx = st[1]
        _el = st[0]
        _ell.append(_el)
        _mxl.append(_mx)
    peak_sequences = []
    for idx in range(0, len(_mxl)):
        if not _ell[idx] == _mxl[idx] == 0:
            peak_sequences.append(lst[_ell[idx]:_ell[idx] + _mxl[idx]])
    infoline1 += " " * (lst.index(peak_sequences[0][0]) * 4 + 10)
    infoline2 += " " * (lst.index(peak_sequences[0][0]) * 4 + 10)
    lines = [0, infoline1, infoline2]
    for seq in peak_sequences:
        new_line = ""
        new_line += "["
        for num in seq:
            new_line += f"{num}"
            if len(f"{num}") < 2:
                new_line += "  "
            elif len(f"{num}") < 3:
                new_line += " "
            new_line += ","
        new_line = new_line[:-1]
        new_line += "]"
        lines[line_num] += new_line
        line_num *= -1
        if lines[0] < 1:
            for _i in range(len(new_line) - 5):
                lines[line_num] += " "
        else:
            for _i in range(len(new_line) - 10):
                lines[line_num] += " "
        lines[0] += 1
    graph.append(lines[1])
    graph.append(lines[2])
    for line in graph:
        print(line)
graph_sequence(lst1, find_longest_peak(lst1)[1])
