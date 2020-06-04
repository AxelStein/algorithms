"""
Worst-case performance	O(n log n)
Best-case performance	O(n log n) typical, O(n) natural variant
Average performance	O(n log n)
Worst-case space complexity	О(n) total with O(n) auxiliary, O(1) auxiliary with linked lists[1]
"""


def sort(left, right):
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


def merge(arr, start, end):
    if end - start == 0:
        return [arr[start]]
    mid = (start + end) // 2
    left = merge(arr, start, mid)
    right = merge(arr, mid + 1, end)
    return sort(left, right)


def merge_sort(arr):
    return merge(arr, 0, len(arr) - 1)


a = [6, 5, 3, 1, 8, 7, 2, 4]
print(a)
print(merge_sort(a))
