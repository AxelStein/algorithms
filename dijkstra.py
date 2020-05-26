class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.marked = False
        self.children = []
        self.weights = []

    def add_child(self, node, weight):
        self.children.append(node)
        self.weights.append(weight)

    def __str__(self):
        return self.name


start = Node("start")
end = Node("end")

a = Node("a")
b = Node("b")

start.add_child(a, 6)
start.add_child(b, 2)

a.add_child(end, 1)

b.add_child(a, 3)
b.add_child(end, 5)

costs = {a.name: 6, b.name: 2, end.name: float("inf")}


def find_lowest(nodes):
    lowest_weight = float("inf")
    lowest_node = None
    for n in nodes:
        cost = costs[n.name]
        if not n.marked and cost < lowest_weight:
            lowest_weight = cost
            lowest_node = n
    return lowest_node


node = find_lowest(start.children)
while node is not None:
    children = node.children
    for i, c in enumerate(children):
        new_weight = node.weights[i] + c.weights[i]
        if new_weight < node.weights[i]:
            costs[node.end.name] = new_weight
            c.parent = node
    node.marked = True
    node = find_lowest(node.children)

print(costs)
