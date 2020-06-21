import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def gen_nums(n):
    nums = []
    for i in range(n):
        nums.append(i)
    random.shuffle(nums)
    return nums


a = gen_nums(100)
print(a)

a = quick_sort(a)
print(a)
