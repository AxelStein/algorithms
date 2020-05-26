import heapq


class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        raise AttributeError

    def __str__(self):
        return "{} {} {}".format(self.v, self.w, self.weight)

    def __repr__(self):
        return str(self)


class Graph:
    def __init__(self):
        self.vertex_count = 0
        self.edge_count = 0
        self.adj = {}

    def add_vertex(self, v):
        self.adj[v] = []
        self.vertex_count += 1

    def add_edge(self, v, w, weight):
        if v not in self.adj:
            self.add_vertex(v)
        if w not in self.adj:
            self.add_vertex(w)

        e = Edge(v, w, weight)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.edge_count += 1

    def __str__(self):
        return "vertex_count = {}\nedge_count = {}\nadj = {}".format(self.vertex_count, self.edge_count, self.adj)


g = Graph()
g.add_edge(0, 1, 0.04)
g.add_edge(0, 2, 0.03)
g.add_edge(0, 3, 2.67)
g.add_edge(0, 4, 0.15)

g.add_edge(1, 0, 26.76)
g.add_edge(1, 2, 0.92)
g.add_edge(1, 3, 71.48)
g.add_edge(1, 4, 4.15)

g.add_edge(2, 0, 29.17)
g.add_edge(2, 1, 1.09)
g.add_edge(2, 3, 77.93)
g.add_edge(2, 4, 4.52)

g.add_edge(3, 0, 0.37)
g.add_edge(3, 1, 0.01)
g.add_edge(3, 2, 0.01)
g.add_edge(3, 4, 0.06)

g.add_edge(4, 0, 6.45)
g.add_edge(4, 1, 0.24)
g.add_edge(4, 2, 0.22)
g.add_edge(4, 3, 17.24)

currency = {
    0: "UAH",
    1: "USD",
    2: "EUR",
    3: "RUB",
    4: "PLN",
}
"""
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 3)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 4)
g.add_edge(1, 4, 3)
g.add_edge(2, 3, 5)
g.add_edge(2, 4, 1)
g.add_edge(2, 5, 6)
g.add_edge(3, 5, 7)
g.add_edge(4, 5, 8)
g.add_edge(5, 6, 9)
"""

marked = [False] * g.vertex_count
queue = []
mst = []


def visit(v):
    marked[v] = True
    for e in g.adj[v]:
        other = e.other(v)
        if not marked[other]:
            heapq.heappush(queue, (e.weight, e))


visit(0)
while queue:
    min_edge = heapq.heappop(queue)[1]

    v = min_edge.v
    w = min_edge.w
    if marked[v] and marked[w]:
        continue
    mst.append(min_edge)
    if not marked[v]:
        visit(v)
    if not marked[w]:
        visit(w)


sum = 0
for e in mst:
    sum += e.weight
    print("{} - {} = {}".format(currency[e.v], currency[e.w], e.weight))
print("sum = {}".format(sum))
