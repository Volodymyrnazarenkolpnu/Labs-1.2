"""lab5 task1 level3 variant1"""
from tkinter import *
from functools import partial
import random
t_matr = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
for el in t_matr:
    for num in range(10):
        _r = random.randint(0,2)
        if _r == 0:
            _r = "R"
        elif _r == 1:
            _r = "G"
        elif _r == 2:
            _r = 'B'
        el.append(_r)

def writefile(matrix):
    """writes to file"""
    file = open("modified.txt", "w")
    for el in matrix:
        line = str(el) + "\n"
        file.write(line)

def readfile():
    """reads matrix from file"""
    file = open("matrix.txt", "r")
    line1 = file.readline()
    line1 = line1.split(",")
    point = (int(line1[0]), int(line1[1]))
    line1 = file.readline()
    color = line1.split("\n")[0]
    matrix = []
    line = " "
    while line != "":
        line = file.readline()
        line = line.split(",")
        if len(line) > 1:
            line[0] = line[0].split("[")[1]
            line[-1] = line[-1].split("]")[0]
            matrix.append(line)
        else:
            line = ""
    return (point, color, matrix)
COLOR_G = "green"
def bfs(point, matrix):
    """bfs"""
    global COLOR_G
    color = COLOR_G
    buffer = []
    queue = [point]
    afterqueue = []
    orig_color = matrix[point[1]][point[0]]
    while len(queue) >= 1:
        for el in queue:
            work_points = []
            if el[0] + 1 < len(matrix[0]):
                work_points.append((el[0] + 1, el[1]))
            if el[0] - 1 >= 0:
                work_points.append((el[0] - 1, el[1]))
            if el[1] + 1 < len(matrix):
                work_points.append((el[0], el[1] + 1))
            if el[1] - 1 >= 0:
                work_points.append((el[0], el[1] - 1))
            for pt in work_points:
                if matrix[pt[1]][pt[0]] == orig_color and pt not in afterqueue:
                    buffer.append(pt)
        for el in queue:
            afterqueue.append(el)
        queue = buffer[:]
        buffer = []
    for pt in afterqueue:
        box_list[pt[1]][pt[0]].configure(bg=color)
        if color == "red":
            col = "R"
        elif color == "blue":
            col = "B"
        elif color == "green":
            col = "G"
        matrix[pt[1]][pt[0]] = col
        
    print(matrix)
    return matrix
def color_red():
    global COLOR_G
    COLOR_G = "red" 

def color_green():
    global COLOR_G
    COLOR_G = "green"

def color_blue():
    global COLOR_G
    COLOR_G = "blue"
def window_init(matrix):
    """init for main window"""
    global COLOR_G
    global box_list
    arr = readfile()
    main_window = Tk()
    main_window.title("Canvas")
    main_window.geometry("700x520")
    main_frame = Frame(main_window)
    main_frame.grid(row=0, column=0)
    box_list = []
    _idx = 0
    _idx2 = 0
    for el in matrix:
        cur_list = []
        for el2 in el:
            col = matrix[_idx2][_idx]
            if col == "R":
                col = "red"
            elif col == "B":
                col = "blue"
            elif col == "G":
                col = "green"
            but1 = Button(main_frame, bg=col, fg=col, width=2, height=2, command=partial(bfs, (_idx,_idx2), matrix))
            cur_list.append(but1)
            but1.grid(row=_idx2, column=_idx)
            _idx += 1
        box_list.append(cur_list)
        _idx = 0
        _idx2 += 1
    green_button = Button(main_frame, bg="green", width=2, height=2, command=color_green)
    blue_button = Button(main_frame, bg="blue", width=2, height=2, command=color_blue)
    red_button = Button(main_frame, bg="red", width=2, height=2, command=color_red)
    green_button.grid(row=0, column=10)
    blue_button.grid(row=1, column=10)
    red_button.grid(row=2, column=10)
    main_window.mainloop()
    return box_list
arr = readfile()
box_list = window_init(arr[2])
matr = bfs(arr[0], arr[2])
writefile(matr)
