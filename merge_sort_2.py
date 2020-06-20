"""
Worst-case performance	O(n log n)
Best-case performance	O(n log n) typical, O(n) natural variant
Average performance	O(n log n)
Worst-case space complexity	О(n) total with O(n) auxiliary, O(1) auxiliary with linked lists[1]
"""
import time
import random


def _merge(arr, buf, li, ri, end):
    start = li
    left_end = ri
    n = end - start

    for k in range(n):
        if li >= left_end or ri < end and arr[li] >= arr[ri]:
            buf[k] = arr[ri]
            ri += 1
        else:
            buf[k] = arr[li]
            li += 1

    for i in range(n):
        arr[start + i] = buf[i]


def _merge_sort_impl(arr, buf, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    # sort left half
    _merge_sort_impl(arr, buf, low, mid)
    # sort right half
    _merge_sort_impl(arr, buf, mid + 1, high)
    # merge two half's
    _merge(arr, buf, low, mid + 1, high + 1)


def merge_sort(arr):
    buf = [0] * len(arr)
    _merge_sort_impl(arr, buf, 0, len(arr) - 1)


def gen_nums(n):
    nums = []
    for i in range(n):
        nums.append(i)
    random.shuffle(nums)
    return nums


arr = gen_nums(10 ** 6)

start_time = time.time()
merge_sort(arr)
print("--- %s seconds ---" % (time.time() - start_time))
