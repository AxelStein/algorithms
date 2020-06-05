# How do you check if two rectangles overlap with each other?
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect:
    def __init__(self, tl, br):
        self.tl = tl
        self.br = br

    def overlaps(self, r):
        if self.tl.y < r.br.y or self.br.y > r.tl.y or self.br.x < r.tl.x or self.tl.x > r.br.x:
            return False
        return True


r1 = Rect(Point(0, 3), Point(3, 0))
r2 = Rect(Point(2, 2), Point(4, 0))
r3 = Rect(Point(5, 2), Point(7, 0))

print(r1.overlaps(r2))
print(r1.overlaps(r3))
print(r2.overlaps(r3))
