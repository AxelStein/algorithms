def persistence(n):
    if n < 10:
        return 0
    m = 1
    while n != 0:
        m *= n % 10
        n //= 10
    return 1 + persistence(m)


print(persistence(39))
print(persistence(999))
print(persistence(4))
