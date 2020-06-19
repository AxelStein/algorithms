# Worst-case performance	О(n2) comparisons and swaps
# Best-case performance	O(n) comparisons, O(1) swaps
# Average performance	О(n2) comparisons and swaps
# Worst-case space complexity	О(n) total, O(1) auxiliary


def sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1
    return arr


print(sort([8, 2, 1, 6, 5, 7, 3, 4]))
