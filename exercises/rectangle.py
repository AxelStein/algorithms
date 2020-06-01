# How do you check if two rectangles overlap with each other?
import math


class Rect:
    def __init__(self, v, s):
        self.vertex = v
        self.size = s


r1 = Rect([(0, 0), (3, 0), (0, 3), (3, 3)], 3)
r2 = Rect([(2, 0), (4, 0), (2, 2), (4, 2)], 2)
r3 = Rect([(4, 0), (4, 2), (6, 0), (6, 2)], 2)


def vector_length(v1, v2):
    # print(v1, v2)
    dx = (v1[0] - v2[0]) ** 2
    dy = (v1[1] - v2[1]) ** 2
    return math.sqrt(dx + dy)


def belongs(r1, r2):
    r1.vertex.sort()
    r2.vertex.sort()

    for i in range(4):
        l = vector_length(r1.vertex[i], r2.vertex[i])
        # print(l)
        if l < r1.size:
            # r2 belongs to r1
            return True
    return False


print(belongs(r1, r2))
print(belongs(r1, r3))
print(belongs(r2, r3))
