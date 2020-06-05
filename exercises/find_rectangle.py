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
          Point(2, 1), Point(2, 0), Point(0, 2), Point(1, 2), Point(2, 2)]
points.sort(key=lambda p: (p.x, p.y))

X_MAX = 3
Y_MAX = 3

matrix = np.zeros(shape=(X_MAX, Y_MAX), dtype=bool)
for p in points:
    matrix[p.x][p.y] = True
print(matrix)

res = []


def check(m, dx, dy):
    for x1 in range(X_MAX - 1):
        for y1 in range(Y_MAX - 1):
            x2 = x1 + dx
            y2 = y1 + dy

            if x2 < X_MAX and y2 < Y_MAX:
                if m[x1][y1] and m[x1][y2] and m[x2][y2] and m[x2][y1]:
                    res.append("{},{} - {},{}".format(x1, y1, x2, y2))


for i in range(1, max(X_MAX, Y_MAX)):
    check(matrix, i, i)
    check(matrix, i + 1, i)
    check(matrix, i, i + 1)

print(res, len(res))
