from Undirected import UndirectedGraph
from bfs import bfs
from dfs import dfs
from ucs import ucs, cost


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

    path = bfs(romania_map, "Arad", "Bucharest")
    print("bfs : " + str(cost(romania_map, path)) + " => " + str(path))

    path = dfs(romania_map, "Arad", "Bucharest")
    print("dfs : " + str(cost(romania_map, path)) + " => " + str(path))

    path = ucs(romania_map, "Arad", "Bucharest")
    print("ucs : " + str(cost(romania_map, path)) + " => " + str(path))


main()
