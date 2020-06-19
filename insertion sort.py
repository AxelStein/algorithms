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
