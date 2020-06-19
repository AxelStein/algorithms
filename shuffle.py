import random as r


# durstenfeld shuffle
# complexity O(n)
def shuffle(arr):
    i = len(arr) - 1
    while i > 0:
        j = r.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
        i -= 1
    return arr


print(shuffle([1, 2, 3, 4, 5]))
