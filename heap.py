class MinHeap:
    def __init__(self):
        self.arr = [0]
        self.size = 0

    def get(self):
        if self.size > 0:
            return self.arr[1]
        return 0

    def pop(self):
        val = self.get()
        self._swap(1, self.size)
        self.arr.pop()
        self.size -= 1
        self._heapify_down(1)
        return val

    def insert(self, v):
        if v < 0:
            raise ValueError()
        self.arr.append(v)
        self.size += 1
        self._heapify_up(self.size)

    def update(self, old, new):
        i = self._find_value_index(1, old)
        if i is None:
            raise ValueError("value not found")
        self.arr[i] = new
        self._heapify_down(1)

    def merge(self, items):
        for i in items:
            if i < 0:
                raise ValueError()
            self.arr.append(i)
        self.size += len(items)
        self._heapify_up(self.size)

    def empty(self):
        return self.size == 0

    def not_empty(self):
        return self.size > 0

    def _find_value_index(self, i, val):
        if self.arr[i] == val:
            return i
        if self._has_left_child(i):
            return self._find_value_index(i * 2, val)
        elif self._has_right_child(i):
            return self._find_value_index(i * 2 + 1, val)
        return None

    def _heapify_down(self, i):
        while self._has_left_child(i):
            min_index = self._min_child_index(i)
            if self.arr[i] > self.arr[min_index]:
                self._swap(i, min_index)
            i += 1

    def _heapify_up(self, i):
        while self._has_parent(i):
            p = self._get_parent(i)
            if p > self.arr[i]:
                self._swap(int(i / 2), i)
            i -= 1

    def _min_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.arr[i * 2] < self.arr[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def _has_parent(self, i):
        return i < len(self.arr) and i / 2 > 0

    def _get_parent(self, i):
        if self._has_parent(i):
            return self.arr[int(i / 2)]
        return None

    def _has_left_child(self, i):
        return i * 2 < len(self.arr)

    def _get_left_child(self, i):
        if self._has_left_child(i):
            return self.arr[i * 2]
        return None

    def _has_right_child(self, i):
        return i * 2 + 1 < len(self.arr)

    def _get_right_child(self, i):
        if self._has_right_child(i):
            return self.arr[i * 2 + 1]
        return None

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def __str__(self):
        return str(self.arr[1:])


h = MinHeap()
h.insert(2.7)
h.insert(1.3)
h.insert(0.5)

while h.not_empty():
    print(h.pop())
print(h)
