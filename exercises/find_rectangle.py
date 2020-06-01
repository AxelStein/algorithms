import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}:{}".format(self.x, self.y)

    def __repr__(self):
        return str(self)


class Rectangle:
    def __init__(self, tl, br):
        self.tl = tl
        self.br = br

    def __str__(self):
        return "{}:{}".format(self.tl, self.br)

    def __repr__(self):
        return str(self)


DIR_NONE = -1
DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3
dir_map = {DIR_UP: "up", DIR_RIGHT: "right", DIR_DOWN: "down", DIR_LEFT: "left"}


def get_vector(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y

    direction = -1
    if dx > 0:
        direction = DIR_RIGHT
    elif dx < 0:
        direction = DIR_LEFT
    if dy > 0:
        direction = DIR_UP
    elif dy < 0:
        direction = DIR_DOWN
    return math.sqrt(dx ** 2 + dy ** 2), direction


points = [Point(0, 0), Point(0, 1), Point(1, 1),
          Point(2, 1), Point(2, 0), Point(0, 2), Point(1, 2)]
points.sort(key=lambda p: (p.x, p.y))


def get_rectangle(arr):
    i = 0
    j = 1
    step = 1
    dir_stack = [DIR_LEFT, DIR_DOWN, DIR_RIGHT, DIR_UP]
    rect = []

    while True:
        vl, dr = get_vector(arr[i], arr[j])
        # if vector is straight
        if vl % 1 == 0:
            # if direction is the same as we need
            # append point to rectangle
            if len(dir_stack) > 0 and dr == dir_stack[-1]:
                rect.append(arr[i])
                dir_stack.pop()
                i = j
        n = len(arr) - 1
        if i == n or j == n:  # end of arr
            step = -1
        if j == 0:  # end of cycle
            break
        j += step
    # we have found the rectangle
    if len(dir_stack) == 0:
        return rect
    return None


i = 0
res = []
rectangle_count = 0
while i + 3 < len(points):
    r = get_rectangle(points[i:])
    if r:
        res.append(r)
        rectangle_count += 1
    i += 1

print(res)
print(rectangle_count)
