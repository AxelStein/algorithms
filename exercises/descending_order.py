def descending_order(num):
    s = []
    while num > 0:
        s.append(num % 10)
        num //= 10
    s.sort(reverse=True)
    return int(''.join(map(str, s)))


def descending_order_2(num):
    return int(''.join(sorted(str(num), reverse=True)))


v = descending_order(123456789)
print(v)
print(type(v))

print(descending_order(15))
