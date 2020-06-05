from collections import defaultdict

import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}:{}".format(self.x, self.y)

    def __repr__(self):
        return str(self)


points = [Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0),
          Point(2, 1), Point(2, 0), Point(0, 2), Point(1, 2), Point(2, 2),
          Point(0, 3), Point(1, 3), Point(2, 3)]

X_MAX = 5
Y_MAX = 5

matrix = np.zeros(shape=(X_MAX, Y_MAX), dtype=bool)
for p in points:
    matrix[p.x][p.y] = True
print(matrix)

edges = defaultdict(int)
answer = 0


def add_edge(e):
    print(e)
    global answer
    if e in edges.keys():
        edges[e] += 1
    else:
        edges[e] = 0
    answer += edges[e]


for x in range(X_MAX):
    y1 = 0
    for y2 in range(Y_MAX):
        if not matrix[x][y2]:
            continue
        if y1 != y2:
            add_edge((y1, y2))
            if y2 >= 2:
                add_edge((0, y2))
            y1 = y2

print(edges)
print(answer)
