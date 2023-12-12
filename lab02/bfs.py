from Undirected import UndirectedGraph


class Queue:

    def __init__(self, stuff=None):
        if stuff is None:
            stuff = []
        self.data = list(stuff)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def isempty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if not self.isempty():
            return self.data.pop(0)
        else:
            return 'queue is empty'

    # return error message if queue is empty
    def peek(self):
        if not self.isempty():
            return self.data[0]
        else:
            return 'queue is empty'

    def __iter__(self):
        """Return iterator for the queue."""
        if self.isempty():
            return None
        else:
            index = 0
            while index < len(self.data):
                yield self.data[index]
                index += 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.data == other.data:
            return True
        else:
            return False

    # copy constructor - clone the current instance
    def copy(self):
        q = Queue(self.data)
        return q


def bfs(graph: UndirectedGraph, source, dest):
    parent = {}
    path = []
    for ver in graph:
        parent[ver] = None
    parent[source] = -1
    q = Queue()
    q.enqueue(source)
    while not q.isempty():
        v = q.dequeue()
        if v == dest:
            break
        for u in graph[v]:
            if parent[u] is None:
                parent[u] = v
                q.enqueue(u)

    node = dest
    while node != source:
        path.append(node)
        node = parent[node]

    path.append(source)
    path.reverse()
    return path
