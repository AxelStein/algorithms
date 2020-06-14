def helper(arr, k, mem):
    if k == 0:
        return 1
    s = len(arr) - k
    if arr[s] == 0:
        return 0
    if mem[k] is not None:
        return mem[k]
    result = helper(arr, k - 1, mem)
    if k >= 2 and int(arr[s:s+2]) <= 26:
        result += helper(arr, k - 2, mem)
    mem[k] = result
    return result


def decode(arr):
    mem = [None] * (len(arr) + 1)
    return helper(arr, len(arr), mem)


print(decode('123'))
