from UndirectedGraph import UndirectedGraph
from gbfs import gbfs
from Astars import astars


def cost(graph, path):
    cost = 0
    for u, v in zip(path, path[1:]):
        cost += graph[u][v]
    return cost


def main():
    romania_map = UndirectedGraph(dict(
        Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
        Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
        Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
        Drobeta=dict(Mehadia=75),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99),
        Hirsova=dict(Urziceni=98),
        Iasi=dict(Vaslui=92, Neamt=87),
        Lugoj=dict(Timisoara=111, Mehadia=70),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97),
        Rimnicu=dict(Sibiu=80),
        Urziceni=dict(Vaslui=142)))

    dist = {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Dobreta": 242,
        "Eforie": 161,
        "Fagaras": 176,
        "Giurgiu": 77,
        "Hirsowa": 151,
        "Lasi": 226,
        "Lugoj": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 100,
        "Rimnicu": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374
    }
    path = gbfs(romania_map, dist, "Arad", "Bucharest")
    print("gbfs: " + str(cost(romania_map, path)) + " => " + str(path))

    path = astars(romania_map, dist, "Arad", "Bucharest")
    print("Astars: " + str(cost(romania_map, path)) + " => " + str(path))


main()
