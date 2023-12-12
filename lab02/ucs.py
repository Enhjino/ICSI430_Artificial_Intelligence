import heapq
from Undirected import UndirectedGraph


class MinHeap:

    def __init__(self):
        self.data = []

    def push(self, ver, prio):
        heapq.heappush(self.data, (prio, ver))

    def pop(self):
        return heapq.heappop(self.data)

    def size(self):
        return len(self.data)


def cost(graph, path):
    cost = 0
    for u, v in zip(path, path[1:]):
        cost += graph[u][v]
    return cost


def ucs(graph: UndirectedGraph, source, dest):
    parent = {}
    heap = MinHeap()
    heap.push(0, source)
    for ver in graph:
        parent[ver] = {"parent": None, "Cost": 9999999}
    parent[source] = {"parent": -1, "cost": 0}
    while heap.size():
        ver = heap.pop()[0]
        for u, cost in graph[ver].items():
            if parent[u]["parent"] is None or (
                    parent[u]["parent"] is not None and parent[ver]["cost"] + cost < parent[u]["cost"]):
                parent[u] = {"parent": ver, "cost": parent[ver]["cost"] + cost}
                heap.push(parent[u]["cost"], u)

    node = dest
    path = []
    while node != source:
        path.append(node)
        node = parent[node]["parent"]

    path.append(source)
    path.reverse()
    return path
