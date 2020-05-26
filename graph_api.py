from collections import deque


class Graph:
    def __init__(self):
        self.vertex_count = 0
        self.edge_count = 0
        self.adj = {}

    def add_vertex(self, v):
        self.adj[v] = []
        self.vertex_count += 1

    def add_edge(self, v, w):
        if v not in self.adj:
            self.add_vertex(v)
        if w not in self.adj:
            self.add_vertex(w)

        self.adj[v].append(w)
        # self.children[w].append(v)
        self.edge_count += 1

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        max_d = 0
        for v in self.adj.keys():
            d = self.degree(v)
            if d > max_d:
                max_d = d
        return max_d

    def avg_degree(self):
        return 2 * self.edge_count / self.vertex_count

    def count_loops(self):
        count = 0
        for v in self.adj.keys():
            for w in self.adj[v]:
                if v == w:
                    count += 1
        return count / 2

    def __str__(self):
        return "vertex_count = {}\nedge_count = {}\nadj = {}".format(self.vertex_count, self.edge_count, self.adj)


class DepthFirstSearch:
    def __init__(self, graph, start):
        self.marked = {}
        self.parent = {}
        self.start = start
        self.has_cycle = False
        self.call_stack = []
        self.direct_order = deque()
        self.reverse_order = deque()
        self.search(graph, start)

    def search(self, graph, v):
        print("search {}".format(v))
        self.call_stack.append(v)
        self.direct_order.append(v)
        self.marked[v] = True
        for w in graph.adj[v]:
            if w not in self.marked:
                self.marked[w] = False
            if not self.marked[w]:
                # print("{} - {}".format(v, w))
                self.parent[w] = v
                self.search(graph, w)
            elif w in self.call_stack:
                self.has_cycle = True
        self.reverse_order.appendleft(v)
        self.call_stack.remove(v)
        print("exit {}".format(v))

    def path_to(self, end):
        path = deque()

        x = end
        while x != self.start and x in self.parent:
            x = self.parent[x]
            path.appendleft(x)
        if len(path) > 0:
            path.append(end)
        return path


class BreadthFirstSearch:
    def __init__(self, graph, start):
        self.marked = {}
        self.parent = {}
        self.start = start
        self.search(graph)

    def search(self, graph):
        self.marked[self.start] = True

        queue = deque()
        queue.append(self.start)

        while queue:
            v = queue.popleft()
            for w in graph.adj[v]:
                if w not in self.marked:
                    self.marked[w] = False
                if not self.marked[w]:
                    # print("{} - {}".format(v, w))
                    self.parent[w] = v
                    self.marked[w] = True
                    queue.append(w)

    def path_to(self, end):
        path = deque()

        x = end
        while x != self.start and x in self.parent:
            x = self.parent[x]
            path.appendleft(x)
        if len(path) > 0:
            path.append(end)
        return path


g = Graph()

"""
random.seed()
for i in range(100):
    g.add_edge(random.randint(1, 100), random.randint(1, 100))

g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(7, 3)
g.add_edge(1, 8)
g.add_edge(8, 6)
g.add_edge(9, 6)
g.add_edge(9, 8)
"""

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 8)
g.add_edge(8, 2)

print(g)
print("----")

dfs = DepthFirstSearch(g, 0)
print(dfs.has_cycle)
print(dfs.reverse_order)

"""
for i in range(g.vertex_count):
    dfs = DepthFirstSearch(g, i)
    # print("direct order = {}".format(dfs.direct_order))
    print("reverse order = {}".format(dfs.reverse_order))
    print("----")


for i in range(2, 10):
    dfs = DepthFirstSearch(g, 1)
    print(dfs.direct_order)
    p = dfs.path_to(i)
    if len(p) == 0:
        print("garbage: {}".format(i))
    else:
        print(dfs.path_to(i))
"""
# bfs = BreadthFirstSearch(g, 1)
# print(bfs.path_to(7))
