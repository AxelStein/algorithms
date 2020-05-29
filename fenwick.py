class FenwickTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = self._prefix_tree(arr)

    def get_sum_range(self, start, end):
        sum_end = self._get_sum(end)
        return sum_end - self._get_sum(start - 1)

    def update(self, i, val):
        dif = val - self.arr[i]
        self.arr[i] += dif
        while i < len(self.tree):
            self.tree[i] += dif
            i += pow(2, self._lsb(i))

    def check_sum(self):
        s = 0
        n = len(self.arr)
        for i in range(n):
            s += self.arr[i]
        return s == self.get_sum_range(1, n-1)

    def _get_sum(self, i):
        s = 0
        while i != 0:
            s += self.tree[i]
            i -= pow(2, self._lsb(i))
        return s

    def _prefix_tree(self, arr):
        tree = [0] * len(arr)
        i = len(arr) - 1
        while i >= 0:
            j = i - pow(2, self._lsb(i)) + 1
            while j <= i:
                tree[i] += arr[j]
                j += 1
            i -= 1
        return tree

    # least significant bit position
    @staticmethod
    def _lsb(num):
        if num == 0:
            return 0
        i = 0
        while not num & 1 << i:
            i += 1
        return i


a = [0, 3, 7, 1, 9, 8, 6, 4, 2, 1, 5]
f = FenwickTree(a)
print(f.get_sum_range(2, 5))
print(f.check_sum())

f.update(2, 3)
print(f.check_sum())

f.update(4, 10)
print(f.check_sum())
