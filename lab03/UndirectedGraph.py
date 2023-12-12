class UndirectedGraph(dict):
    def __init__(self, graph):
        super().__init__()
        for vertex, edges in (graph.items()):
            if vertex not in self:
                self[vertex] = {}
            for neighbour, weight in edges.items():
                if neighbour not in self:
                    self[neighbour] = {}
                self[vertex][neighbour] = weight
                self[neighbour][vertex] = weight
