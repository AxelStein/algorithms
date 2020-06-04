import numpy as np


def swap(arr, i, j):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]


def sort(arr, i, j):
    print('sort', i, j, arr)
    start = j
    end = (j - i) + j
    n = i
    v = arr[i]
    while n < end:
        if v < arr[j]:
            arr[n] = v
            i += 1
            v = arr[i]
        else:
            arr[n] = arr[j]
            j += 1
        n += 1


def merge(arr, start, end):
    if end - start == 0:
        return start
    mid = int(start + (end - start) / 2)
    l = merge(arr, start, mid)
    h = merge(arr, mid + 1, end)
    sort(arr, l, h)
    return start


# 5613 2478
a = np.array([6, 5, 3, 1, 8, 7, 2, 4])
# s = np.zeros(len(a), dtype=int)
# print(s)

merge(a, 0, len(a) - 1)
print(a)

# print(s)
