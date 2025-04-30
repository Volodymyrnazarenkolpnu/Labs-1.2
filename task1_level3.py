"""lab6 task1 level3 variant3"""
import json
import random
import math
from tkinter import *
class Graph():
    """graph def class"""
    def __init__(self):
        """init"""
        self.points = {}
        self.edges = []

    def add_edge(self, a, b):
        """add edge from p.a to p.b"""
        if a in self.points:
            ap = self.points[a]
            ap.connections.append([b, "f"])
            bp = self.points[b]
            bp.connections.append([a, "b"])
            self.edges.append([a,b])

    def add_point(self, point):
        """add a point to graph"""
        p = Point(point)
        self.points[point] = p
        return p

class Point():
    """point def class"""
    def __init__(self, value):
        self.value = value
        self.connections = []

def bfs(node, goal, graph):
    """looking for gas"""
    queue = [graph.points[node]]
    met = [graph.points[node]]
    found = []
    while len(queue) > 0:
        for con in graph.points[queue[0].value].connections:
            if con[1] == "b":
                if not graph.points[con[0]] in met:
                    queue.append(graph.points[con[0]])
                    met.append(graph.points[con[0]])
                if con[0] in goal and not goal.index(con[0]) in found:
                    found.append(goal.index(con[0]))
        queue.pop(0)
    return found

def the_algorythm(towns, gas_storages, connections, graph):
    """heart of the lab6"""
    len_list = [i for i in range(0, len(gas_storages))]
    len_set = set(len_list)
    not_found = []
    for storage in gas_storages:
        not_found.append([storage, []])
    for town in graph.points:
        if not town in gas_storages:
            found = bfs(town, gas_storages, graph)
            not_found_idx = list(len_set - set(found))
            for idx in not_found_idx:
                not_found[idx][1].append(town)
    return not_found

def game():
    """func for game"""
    print("Please enter Seed (ENTER for random):")
    seed = input()
    if seed == "":
        seed = random.randint(0, 9999999999)
    seed_txt = str(seed)
    print("Seed:" + seed_txt)
    file = open("config.txt", "r")
    names = json.loads(file.readline())
    town_list = []
    storage_list = []
    connection_list = []
    game_graph = Graph()
    #randomisation
    for t in range(8):
        _town_rng = seed_txt[(0 + t if 0 + t < 10 else 0 + t - 10):(3 + t) - 10 * int(str(1000 + t)[2]) if 3 + t < 10 or t % 10 < 8 else 10] + (seed_txt[0:3 + t - 10] if 3 + t > 10 and t < 10 else "")
        _town_rng = math.floor(int(_town_rng) * (len(names)/1000))
        town_name = names[int(_town_rng)]
        names.remove(town_name)
        town = game_graph.add_point(town_name)
        town_list.append(town.value)
    for s in range(4):
        storage_name = "Сховище_" + str(s + 1)
        storage = game_graph.add_point(storage_name)
        storage_list.append(storage.value)
    for s in storage_list:
        n = 1
        town_list_copy = town_list[:]
        for town in range(n):
            _idx = math.floor(int(seed_txt[range(n).index(n - 1) + storage_list.index(s):range(n).index(n - 1) + 2 + storage_list.index(s)]) * (len(town_list_copy) / 100))
            town = town_list_copy[_idx]
            town_list_copy.remove(town)
            game_graph.add_edge(s, town)
            connection_list.append([s, town])
    for t in town_list:
        n = math.floor(int(seed_txt[town_list.index(t) % 10]) / 5) + 1
        town_list_copy = town_list[:]
        town_list_copy.remove(t)
        for town in range(n):
            _idx = math.floor(int(seed_txt[(int(seed_txt[8]) * range(n).index(n - 1)) // 10]) * (len(town_list_copy) / 100))
            town = town_list_copy[_idx]
            con_list = game_graph.points[town].connections[:]
            t_con_list= []
            satisfied = False
            while not satisfied:
                for el in con_list:
                    t_con_list.append(el[0])
                if t in t_con_list:
                    _idx+=1
                    if _idx >= len(town_list_copy):
                        _idx -= 8
                        town = town_list_copy[_idx]
                        con_list = game_graph.points[town].connections[:]
                        t_con_list= []
                else:
                    satisfied = True
            town_list_copy.remove(town)
            game_graph.add_edge(t, town)
            connection_list.append([t, town])
    #initialization
    print("Towns: ")
    line = ""
    for el in town_list:
        line += el + ", "
    print(line)
    not_found = the_algorythm(town_list, storage_list, connection_list, game_graph)

    for el in not_found:
        print("There is no access from " + el[0] + " to:")
        line = ""
        for town in el[1]:
            line += town + ", "
        print(line)
    _count = 0

    print("Choose 5 towns to view")
    while _count < 5:
        inp = input()
        if inp == "skip":
            break
        if inp in game_graph.points:
            point = game_graph.points[inp]
            for con in point.connections:
                if con[1] == "f":
                    print("-" + con[0])
            _count += 1
        else:
            print("try again")
    print("choose 1 town to sabotage")
    del_list = []
    while True:
        inp = input()
        if inp in game_graph.points:
            point = game_graph.points[inp]
            for con in point.connections:
                for con_in in game_graph.points[con[0]].connections:
                    if con_in[0] == point:
                        del_list.append([con[0], con_in])
            point.connections = []
            break
        else:
            print("try again")
    for el in del_list:
        el[0].connections.remove(el[1])
    for el in connections:
        if el[0] == point or el[1] == point:
            connections.remove(el)
    not_found_2 = the_algorythm(town_list, storage_list, connection_list, game_graph)
    for el in not_found_2:
        print("There is no access from " + el[0] + " to:")
        line = ""
        for town in el[1]:
            line += town + ", "
        print(line)
    comparison_list = []
    for el in not_found:
        comparison_list.append(el[1])
    for el in not_found_2:
        idx = not_found_2.index(el)
        comparison_list[idx] = len(el[1]) - len(comparison_list[idx])
    summ = 0
    for el in comparison_list:
        summ += el
    summ -= 4
    if summ < 0:
        summ = 0
    print(str(summ) + " points")


#graph
file = open("info.txt", "r")
towns = json.loads(file.readline().split("\n")[0])
gas_storages = json.loads(file.readline().split("\n")[0])
connections = json.loads(file.readline().split("\n")[0])
town_graph = Graph()
len_list = [i for i in range(0, len(gas_storages))]
len_set = set(len_list)
for town in towns:
    town_graph.add_point(town)
for storage in gas_storages:
    town_graph.add_point(storage)
for connection in connections:
    pt, dest = connection
    town_graph.add_edge(pt, dest)
print(the_algorythm(towns, gas_storages, connections, town_graph))
inp  = input()
if inp == "game":
    while True:
        game()
        inp = input()
        if inp == "exit":
            break
