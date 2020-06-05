import numpy as np


def m(arr, buf, li, ri, end):
    print('m', li, ri, end)
    start = li
    n = end - start + 1
    for k in range(n):
        if li >= ri or ri < end and arr[li] >= arr[ri]:
            buf[k] = arr[ri]
            ri += 1
        else:
            buf[k] = arr[li]
            li += 1
    for i in range(n):
        arr[start + i] = buf[i]
    print(arr, buf)

    """
    i = j = 0
    length = len(left) + len(right)
    out = []
    for _ in range(length):
        if i >= len(left) or j < len(right) and left[i] >= right[j]:
            out.append(right[j])
            j += 1
        else:
            out.append(left[i])
            i += 1
    return out
    """


def merge(arr, buf, low, high, end):
    j = 0
    start = low
    mid = high - 1
    n = end - start + 1  # element count
    while start <= mid and high <= end:
        if arr[low] < arr[high]:
            buf[j] = arr[low]
            low += 1
        else:
            buf[j] = arr[high]
            high += 1
        j += 1

    while low <= mid:
        buf[j] = arr[low]
        j += 1
        low += 1

    while high <= end:
        buf[j] = arr[high]
        j += 1
        high += 1

    for j in range(n):
        arr[start + j] = buf[j]


def _merge_sort_impl(arr, buf, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    # sort left half
    _merge_sort_impl(arr, buf, low, mid)
    # sort right half
    _merge_sort_impl(arr, buf, mid + 1, high)
    # merge two half's
    m(arr, buf, low, mid + 1, high)


def merge_sort(arr):
    buf = np.zeros(len(arr), dtype=int)
    _merge_sort_impl(arr, buf, 0, len(arr) - 1)


a = np.array([6, 5, 3, 1, 8, 7, 2, 4], dtype=int)
print(a)

merge_sort(a)
print(a)
