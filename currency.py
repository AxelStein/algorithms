import math


class Edge:
    def __init__(self, from_, to_, weight):
        self.from_ = from_
        self.to_ = to_
        self.weight = weight

    def other(self, vertex):
        if vertex == self.from_:
            return self.to_
        elif vertex == self.to_:
            return self.from_
        raise AttributeError

    def __str__(self):
        return "{} - {} = {}".format(self.from_, self.to_, self.weight)

    def __repr__(self):
        return str(self)


class Graph:
    def __init__(self):
        self.vertex_count = 0
        self.edge_count = 0
        self.adj = {}
        self.edgeTo = {}
        self.distTo = {}

    def add_vertex(self, v):
        self.adj[v] = []
        self.vertex_count += 1

        self.edgeTo[v] = None
        self.distTo[v] = float("inf")

    def add_edge(self, from_, to_, weight):
        if from_ not in self.adj:
            self.add_vertex(from_)
        if to_ not in self.adj:
            self.add_vertex(to_)

        edge = Edge(from_, to_, weight)
        self.adj[from_].append(edge)
        self.edge_count += 1

    def __str__(self):
        return "vertex_count = {}\nedge_count = {}\nadj = {}".format(self.vertex_count, self.edge_count, self.adj)


g = Graph()

with open('currency.txt', encoding="utf-8") as file:
    for l in file.readlines():
        arr = l.split(' ')
        g.add_edge(int(arr[0]), int(arr[1]), float(arr[2]))
file.close()

print(g)

currency = {
    0: "UAH",
    1: "USD",
    2: "EUR",
    3: "RUB",
    4: "PLN",
}

on_queue = [False] * g.vertex_count  # vertices on queue
queue = [5]
cost = 0  # relax() count
cycle = []
g.distTo[5] = 0


def find_negative_cycle(graph):
    pass


def relax_vertex(graph, vertex):
    global cost
    for edge in graph.adj[vertex]:
        print(edge)
        v = edge.from_
        w = edge.to_
        distance = graph.distTo[v] + edge.weight
        if graph.distTo[w] > distance:
            graph.distTo[w] = distance
            graph.edgeTo[w] = edge

            if not on_queue[w]:
                queue.append(w)
                on_queue[w] = True

        cost += 1
        if cost % graph.vertex_count == 0:
            find_negative_cycle(graph)


while queue:
    v = queue.pop(0)
    relax_vertex(g, v)

print("edgeTo = {}".format(g.edgeTo))
print("distTo = {}".format(g.distTo))
