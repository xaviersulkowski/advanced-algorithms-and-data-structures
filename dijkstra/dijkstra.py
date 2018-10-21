import networkx as nx
import numpy as np


def read_graph_structure_scheme(graph_structure_scheme_file):
    with open(graph_structure_scheme_file, 'r') as f:
        tmp_structure = f.read().splitlines()
    f.close()

    structure = []
    for line in tmp_structure:
        structure.append(line.split(';'))

    return structure


def dijkstra(graph, start):
    S = set()
    #set infinity
    delta = dict.fromkeys(list(graph.adj), np.inf)
    #set zero
    previous = dict.fromkeys(list(graph.adj), None)

    delta[start] = 0

    #create set of neighbours
    neighbors = {key: list(graph.neighbors(key)) for key in list(graph.node)}


    while S != set(graph.node):
        #choose smallest from neighbours
        v = min((set(delta.keys())-S), key=delta.get)
        for neighbor in set(neighbors[v]) - S:
            new_path =delta[v] + graph[v][neighbor]['weight']
            if new_path < delta[neighbor]:
                delta[neighbor] = new_path
                previous[neighbor] = v

        S.add(v)

    return (delta, previous)


def shortest_path(graph, start, end):
    delta, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]


    path.reverse()


    for key in path:
        print("node: " + str(key), "  cost after step: " + str(delta[key]))


    return path



graph_structure_file = './graf.txt'
structure_scheme = read_graph_structure_scheme(graph_structure_file)
structure_scheme = np.asarray(structure_scheme, dtype=int)

graph = nx.DiGraph()
graph.add_weighted_edges_from(structure_scheme)

print(shortest_path(graph, 1, 20))


