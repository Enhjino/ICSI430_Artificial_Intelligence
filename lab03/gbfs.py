from UndirectedGraph import UndirectedGraph


class Queue:

    def __init__(self, stuff=[]):
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

    # define the iterator for queue.  Used in for or list comprehension
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


def gbfs(graph: UndirectedGraph, dist, source, dest):
    parent = {}
    for i in graph:
        parent[i] = {"parent": None}
    parent[source] = {"parent": -1}
    q = Queue()
    q.enqueue(source)
    while not q.isempty():
        ver = q.dequeue()
        if ver == dest:
            break
        min = {"ver": "", "dist": 999999}
        for u, cost in graph[ver].items():
            if dist[u] < min["dist"]:
                min["ver"] = u
                min["dist"] = dist[u]
        parent[min["ver"]]["parent"] = ver
        q.enqueue(min["ver"])
    node = dest
    path = []
    while node != source:
        path.append(node)
        node = parent[node]["parent"]

    path.append(source)
    path.reverse()
    return path
