import numpy as np


def swap(arr, i, j):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]


def merge(arr, low, high):
    print(low, high, int(high / 2))
    if high - low == 0:
        return low
    mid = int(low + (high - low) / 2)
    r1 = merge(arr, low, mid)
    r2 = merge(arr, mid + 1, high)
    print("ret", r1, r2)
    return r1, r2


def sort():
    pass


arr = np.array([6, 5, 3, 1, 8, 7, 2, 4])
merge(arr, 0, len(arr)-1)
