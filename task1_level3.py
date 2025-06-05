"""Lab8, Task1, Variant3, Level2"""
import math
import sys
class Node():
    """nodes of the graph"""
    def __init__(self, name, status):
        self.name = name
        self.connections = []
        self.back_connections = []
        self.status = status
        self.dist = sys.maxsize

class Graph():
    """graph itself"""
    def __init__(self):
        self.nodes = {}
        self.connections = []
        self.back_connections = []
        self.factories = []
        self.shops = []

    def add_node(self, node, status):
        """add node to graph"""
        try:
            _a = self.nodes[node]
        except KeyError:
            self.nodes[node] = Node(node, status)
            if status == "shop":
                self.shops.append(node)
            elif status == "factory":
                self.factories.append(node)

    def add_connection(self, con):
        """add connection to graph"""
        self.connections.append(con)
        self.nodes[con[0]].connections.append([con[1], con[2]])
        self.nodes[con[1]].back_connections.append([con[0], con[2]])

def enumerate(graph : Graph, shop):
    graph.nodes[shop].dist = 0
    dist = 0
    queue = [shop]
    met = [shop]
    while queue:
        working = graph.nodes[queue.pop(0)]
        dist = working.dist
        for con in working.back_connections:
            if not con[0] in met:
                graph.nodes[con[0]].dist = dist + 1
                queue.append(con[0])
                met.append(con[0])


def dijkstra(graph : Graph, source : str, shop_max_flows : list):
    """algo for finding max flow to each shop"""
    queue = [source]
    met = {source:source}
    node_list = list(graph.nodes.values())
    source_idx = node_list.index(graph.nodes[source])
    flow_matrix = [sys.maxsize] * len(node_list)
    flow_matrix[source_idx] = sys.maxsize
    while queue:
        working_name = queue.pop(0)
        working_obj = graph.nodes[working_name]
        working_idx = node_list.index(working_obj)
        potential = flow_matrix[working_idx]
        cons = []
        for con in working_obj.connections:
            if cons:
                for con1 in cons:
                    if graph.nodes[con[0]].dist > graph.nodes[con1[0]].dist:
                        continue
                    else:
                        cons.insert(cons.index(con1), con)
                        break
            else:
                cons.append(con)
        for con in cons:
            next_node_idx = node_list.index(graph.nodes[con[0]])
            if con[0] not in met:
                met[con[0]] = working_name
                if met[con[0]] != con[0] and con[1] != 0:
                    min_temp = min(flow_matrix[working_idx], con[1], potential)
                    flow_matrix[next_node_idx] = min_temp
                    potential -= min_temp
                    con[1] -= min_temp
                    if con[0] not in queue:
                        queue.append(con[0])
            else :
                if met[con[0]] != con[0] and con[1] != 0:
                    min_temp = min(flow_matrix[working_idx], con[1], potential)
                    flow_matrix[next_node_idx] += min_temp
                    potential -= min_temp
                    con[1] -= min_temp

    _idx = 0
    for shop in graph.shops:
        shop_list_idx = node_list.index(graph.nodes[shop])
        curr_max_value = flow_matrix[shop_list_idx]
        if shop_max_flows[_idx] < curr_max_value and curr_max_value != sys.maxsize:
            shop_max_flows[_idx] = curr_max_value
        _idx += 1
    return shop_max_flows

def find_max_flow(graph: Graph):
    """finding max amount for each shop"""
    shop_max = [0] * len(graph.shops)
    for factory in graph.factories:
        shop_max = dijkstra(graph, factory, shop_max)
    return shop_max

def main():
    """the algo"""
    graph1 = Graph()
    file = open("roads.csv", "r")
    factories = file.readline()
    factories = factories.split(", ")
    factories[-1] = factories[-1].split("\n")[0]
    shops = file.readline()
    shops = shops.split(", ")
    shops[-1] = shops[-1].split("\n")[0]
    connections = file.readline()
    connections = connections.split(", ")
    connections[-1] = connections[-1].split("\n")[0]
    for factory in factories:
        graph1.add_node(factory, "factory")
    for shop in shops:
        graph1.add_node(shop, "shop")
    _idx = 0
    _t_con_1 = ""
    _t_con_2 = ""
    for el in connections:
        if _idx % 3 == 0:
            graph1.add_node(el, "")
            _t_con_1 = el
        if _idx % 3 == 1:
            graph1.add_node(el, "")
            _t_con_2 = el
        if _idx % 3 == 2:
            graph1.add_connection([_t_con_1, _t_con_2, int(el)])
        _idx += 1
    summ = 0
    for shop in graph1.shops:
        enumerate(graph1, shop)
        summ += sum(find_max_flow(graph1))
    return summ

a = main()
print(a)
