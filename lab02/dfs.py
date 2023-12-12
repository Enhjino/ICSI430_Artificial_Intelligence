from Undirected import UndirectedGraph


class Stack:

    def __init__(self, stuff=None):
        if stuff is None:
            stuff = []
        self.items = stuff[:]
        self.size = len(stuff)

    def __repr__(self):
        return "stack({})".format(list(self.items))

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def peek(self):
        if self.isempty():
            return "Error: stack is empty"
        else:
            return self.items[-1]

    def pop(self):
        if self.isempty():
            return "Error: stack is empty"
        else:
            self.size -= 1
            return self.items.pop()

    # swap the top two items in the stack
    def rotate(self):
        if self.size < 2:
            return "Error: stack has fewer than 2 elements"
        else:
            self.items[-1], self.items[-2] = self.items[-2], self.items[-1]

    # define the iterator for stack.  Used in for or list comprehension
    def __iter__(self):
        """Return iterator for the stack."""
        if self.isempty():
            return None
        else:
            index = self.size - 1
            while index >= 0:
                yield self.items[index]
                index -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.items == other.items:
            return True
        else:
            return False

    # copy constructor - clone the current instance
    def copy(self):
        s = Stack(self.items)
        return s


def dfs(graph: UndirectedGraph, source, dest):
    parent = {}
    path = []
    for ver in graph:
        parent[ver] = None
    parent[source] = -1
    s = Stack()
    s.push(source)
    while not s.isempty():
        ver = s.pop()
        if ver == dest:
            break
        for u in graph[ver]:
            if parent[u] is None:
                parent[u] = ver
                s.push(u)
    node = dest
    while node != source:
        path.append(node)
        node = parent[node]

    path.append(source)
    path.reverse()
    return path
