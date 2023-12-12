from UndirectedGraph import UndirectedGraph
from gbfs import Queue


def astars(graph: UndirectedGraph, dist, source, dest):
    parent = {}
    path = []
    for ver in graph:
        parent[ver] = None
    parent[source] = -1
    q = Queue()
    q.enqueue(source)
    path_cost = 0
    while not q.isempty():
        v = q.dequeue()
        if v == dest:
            break
        min = {"ver": "", "dist": 999999}
        for u in graph[v]:
            if path_cost + dist[u] + graph[v][u] < min["dist"]:
                min["ver"] = u
                min["dist"] = path_cost + dist[u] + graph[v][u]
        path_cost += graph[v][min["ver"]]
        q.enqueue(min["ver"])
        parent[min["ver"]] = v

    node = dest
    while node != source:
        path.append(node)
        node = parent[node]

    path.append(source)
    path.reverse()
    return path
