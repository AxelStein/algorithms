import math as m


def find_next_square(num):
    s = m.sqrt(num)
    return int(m.pow(s + 1, 2)) if s % 1 == 0 else -1


def find_next_square_2(sq):
    x = sq ** 0.5
    return -1 if x % 1 else (x + 1) ** 2


def find_next_square_3(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1


print(find_next_square(625))
