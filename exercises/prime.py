import random
import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_2(num):
    print('is_prime', num)

    # There's only one even prime: 2
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    """
    Property:
        Every number n that is not prime has at least one prime divisor p
        such 1 < p < square_root(n)
    """
    root = int(math.sqrt(num))
    print('root', root)

    # We know there's only one even prime, so with that in mind
    # we're going to iterate only over the odd numbers plus using the above property
    # the performance will be improved
    for i in range(3, root + 1, 2):
        print('i', i, num)
        if num % i == 0:
            print('-')
            return False
    return True


# This is the Miller-Rabin test for primes, which works for super large n
def even_odd(n):
    s, d = 0, n
    while d % 2 == 0:
        s += 1
        d >>= 1
    return s, d


def Miller_Rabin(a, p):
    s, d = even_odd(p - 1)
    a = pow(a, d, p)
    if a == 1:
        return True
    for i in range(s):
        if a == p - 1:
            return True
        a = pow(a, 2, p)
    return False


def is_prime_3(p):
    if p == 2:
        return True
    if p <= 1 or p % 2 == 0:
        return False
    return all(Miller_Rabin(random.randint(2, p - 1), p) for _ in range(40))


# print(is_prime(2147483647))
print(is_prime_2(2147483647))
print(is_prime_3(2147483647))

"""
for i in range(1, 1000001):
    if is_prime_2(i):
        print(i)
"""
