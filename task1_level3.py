"""lab6 task1 level3 variant3"""
import json
import random
import math
import copy
import pygame_features
#region LAB
file = open("config.txt", "r", encoding="utf8")
names = json.loads(file.readline())

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
#endregion LAB
#region Generation
def generate_towns(town_num, town_con_max, storage_num, seed_str):
    """generate towns"""
    names_copy = names[:]
    town_list = []
    storage_list = []
    connection_list = []
    game_graph = Graph()
    for t in range(town_num):
        if range(town_num).index(t) % 10 <= 7:
            _town_rng = int(seed_str[t % 10:(t % 10 + 3)])
        else:
            _town_rng = int(seed_str[t % 10:10] + seed_str[0:(t + 3) % 10])
        _town_rng = math.floor(int(_town_rng) * (len(names_copy)/1000))
        town_name = names_copy[int(_town_rng)]
        names_copy.remove(town_name)
        town = game_graph.add_point(town_name)
        town_list.append(town.value)
    for s in range(storage_num):
        storage_name = "Сховище_" + str(s + 1)
        storage = game_graph.add_point(storage_name)
        storage_list.append(storage.value)
    for s in storage_list:
        _idx = math.floor(int(seed_str[storage_list.index(s) % 10] + seed_str[storage_list.index(s) // 10]) * len(town_list) / 100)
        town = town_list[_idx]
        game_graph.add_edge(s, town)
        connection_list.append([s, town])
    for t in town_list:
        _i1 = (town_list.index(t) + int(seed_str[1])) % 10
        _i2 = ((town_list.index(t) // 10) + int(seed_str[2])) % 10
        _i3 = (town_list.index(t) // 100 + int(seed_str[3])) % 10
        _town_rng = seed_str[_i1] + seed_str[_i2] + seed_str[_i3]
        _town_rng = math.floor(int(_town_rng) * (town_con_max / 1000)) + 1
        town_list_copy = town_list[:]
        town_list_copy.remove(t)
        for town in range(_town_rng):
            _i4 = (town_list.index(t) + int(seed_str[4])) % 10
            _i5 = ((town_list.index(t) // 10) + int(seed_str[5])) % 10
            _i6 = (town_list.index(t) // 100 + int(seed_str[6])) % 10
            _idx = seed_str[_i4] + seed_str[_i5] + seed_str[_i6]
            _idx = math.floor(int(_idx) * (len(town_list_copy) / 1000))
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
                        _idx = 0
                    town = town_list_copy[_idx]
                    con_list = game_graph.points[town].connections[:]
                    t_con_list= []
                else:
                    satisfied = True
            town_list_copy.remove(town)
            game_graph.add_edge(t, town)
            connection_list.append([t, town])
    return (town_list, storage_list, connection_list, game_graph)

def check_max_points(t_list, stor_list, con_list, graph, not_found_list):
    """chech hom many points seed can score at max"""
    con_list_copy = con_list[:]
    points = []
    for town in t_list:
        del_list = []
        test_graph = copy.deepcopy(graph)
        point = test_graph.points[town]
        for con in point.connections:
            for con_in in test_graph.points[con[0]].connections:
                if con_in[0] == point:
                    del_list.append([con[0], con_in])
        point.connections = []
        for el in del_list:
            el[0].connections.remove(el[1])
        for el in con_list_copy:
            if el[0] == point or el[1] == point:
                con_list_copy.remove(el)
        not_found_list_2 = the_algorythm(t_list, stor_list, con_list_copy, test_graph)
        comparison_list = []
        summ = 0
        for el in not_found_list:
            comparison_list.append(el[1])
        for el in not_found_list_2:
            idx = not_found_list_2.index(el)
            if town not in not_found_list[idx][1] and town in not_found_list_2[idx][1]:
                summ -= 1
            comparison_list[idx] = len(el[1]) - len(comparison_list[idx])
        for el in comparison_list:
            summ += el
        points.append(summ)
    return max(points)
#endregion Generation
def game():
    """func for game"""
    pygame_features.pygame_window_shenedigans()
    lost = False
    level = 1
    game_points = 0
    max_town_cons = 2
    print("Select game mode (any string for custom mode)")
    mode = input()
    while not lost:
        if mode != "rogue":
            lost = True
        if lost:
            print("Please enter Seed (ENTER for random):")
            seed = input()
            if seed == "":
                seed = random.randint(0, 9999999999)
        else:
            seed = random.randint(0, 9999999999)
        seed_txt = str(seed)
        if len(seed_txt) < 10:
            for i in range(10 - len(seed_txt)):
                seed_txt = "0" + seed_txt
        print("Seed:" + seed_txt)
        #randomisation
        towns = math.floor(0.24 * level + 8)
        views = math.floor(0.2 * level + 6)
        storages = math.floor(0.15 * level + 4)
        min_percent = math.floor(0.3 * level) * 10
        if min_percent > 50:
            min_percent = 50
        town_list, storage_list, connection_list, game_graph = generate_towns(towns, max_town_cons, storages, seed_txt)
        #initialization
        print("Towns: ")
        line = ""
        for el in town_list:
            line += el + ", "
        print(line)
        not_found = the_algorythm(town_list, storage_list, connection_list, game_graph)
        maxx = check_max_points(town_list, storage_list, connection_list, game_graph, not_found)
        if not lost:
            print("Level:" + str(level))
            print("Current threshold:" + str(min_percent) + "%")
        print("Maximum amount of points:" + str(maxx))
        for el in not_found:
            print("There is no access from " + el[0] + " to:")
            line = ""
            for town in el[1]:
                line += town + ", "
            print(line)
        _count = 0

        print(f"Choose {views} towns to view")
        while _count < views:
            inp = input()
            if inp == "skip" or inp == "скіп":
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
        summ = 0
        for el in not_found:
            comparison_list.append(el[1])
        for el in not_found_2:
            idx = not_found_2.index(el)
            if inp not in not_found[idx][1] and inp in not_found_2[idx][1]:
                summ -= 1
            comparison_list[idx] = len(el[1]) - len(comparison_list[idx])
        for el in comparison_list:
            summ += el
        print(str(summ) + " points out of " + str(maxx) + f"({round((summ / maxx) * 100, 3)}%)")
        if not lost:
            print("Current threshold:" + str(min_percent) + "%")
            if (summ / maxx) * 100 >= min_percent:
                print("You passed!")
                print(f"Gained {summ} points. Current points:{game_points + summ}")
                level += 1
            else:
                print("Not enough!")
                lost = True
        game_points += summ
        _wait = input()
    if mode == "rogue":
        print("Run lost! Score:" + str(game_points))

#graph
file = open("info.txt", "r", encoding="utf8")
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
