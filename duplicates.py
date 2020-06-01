arr = [3, 1, 6, 9, 4, 3, 1, 6, 2, 3]
arr.sort()

out = [0] * len(arr)

i = 0
while i != len(arr):
    out[i] = arr[i]
    p = i - 1
    if p >= 0:
        if arr[p] == arr[i]:
            out[i] = 0
    i += 1
    """
    if arr[i] == arr[i+1]:
        arr.pop(i+1)
    else:
        i += 1
    """
print(arr)
print(out)
