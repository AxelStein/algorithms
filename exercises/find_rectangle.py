import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}:{}".format(self.x, self.y)

    def __repr__(self):
        return str(self)


def vector_length(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx ** 2 + dy ** 2)


points = [Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1),
          Point(2, 1), Point(2, 0), Point(0, 2), Point(1, 2)]
points.sort(key=lambda p: (p.x, p.y))


def has_rectangle(arr):
    print(arr)
    i = 0
    j = 1
    step = 1
    edge_count = 0
    marked = [False] * len(arr)

    while True:
        vl = vector_length(arr[i], arr[j])
        if vl % 1 == 0 and not marked[j]:
            print(arr[i], arr[j])
            marked[j] = True
            i = j
            edge_count += 1
        n = len(arr) - 1
        if i == n or j == n:  # end of arr
            step = -1
        if j == 0:  # end of cycle
            break
        j += step
    print("result", edge_count, len(arr))
    return edge_count == len(arr)


i = 0
rectangle_count = 0
while i + 3 < len(points):
    if has_rectangle(points[i:i + 4]):
        rectangle_count += 1
    i += 1

if has_rectangle(points):
    rectangle_count += 1

print(rectangle_count)
