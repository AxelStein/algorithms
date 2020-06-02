import random

arr = []
for i in range(1, 10):
    arr.append(i)

arr.remove(random.randint(0, len(arr)))
print(arr)


def search(arr, low, high):
    if high - low == 1:
        d = arr[high] - arr[low]
        if d > 1:
            return arr[high]-1
        else:
            if arr[high] == len(arr):
                return len(arr) + 1
            elif arr[low] == 2:
                return 1
        return -1

    mid = low + int((high-low) / 2)
    if arr[mid] - mid == 1:
        return search(arr, mid, high)
    else:
        return search(arr, low, mid)


low = 0
high = len(arr)-1

print('result:', search(arr, low, high))
