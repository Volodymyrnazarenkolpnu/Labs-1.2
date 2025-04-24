"""lab6 task1 level3 variant3"""

class Graph():
    """graph def class"""
    def __init__(self):
        """init"""
        self.points = []
        self.edges = []

    def add_edge(self, a, b):
        """add edge from p.a to p.b"""
        if a in self.points:
            a = self.points[self.points.index(a)]
            a.connections.append(b)
            self.edges.append([a,b])

    def add_point(self, point):
        """add a point to graph"""
        self.points.append(point)

class Point():
    """point def class"""
    def __init__(self, value):
        self.value = value
        self.connections = []

def bfs(node, goal):
    """looking for gas"""
    queue = [node]
    met = [node]
    found = []
    while len(queue) > 0:
        for con in queue[0].connections:
            if not con in met:
                queue.append(con)
                met.append(con)
            if con.value in goal:
                found.append(goal.index(con.value))
    return found

def the_algorythm(towns, gas_storages, connections):
    """heart of the lab6"""
    #graph
    town_graph = Graph()
    len_list = [i for i in range(0, len(gas_storages))]
    len_set = set(len_list)
    for town in towns:
        t = Point(town)
        town_graph.add_point(t)
    for storage in gas_storages:
        g = Point(storage)
        town_graph.add_point(g)
    for connection in connections:
        pt, dest = connection
        town_graph.add_edge(pt, dest)
    not_found = []
    for storage in gas_storages:
        not_found.append([storage.value, []])
    for town in towns:
        found = bfs(town, gas_storages)
        not_found_idx = list(set(found) - len_set)
        for idx in not_found_idx:
            not_found[idx][1].append(town)
    print(not_found)
    return not_found
    
