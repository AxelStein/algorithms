class PriorityQueue:
    def __init__(self):
        self.key = [0]
        self.val = [0]
        self.size = 0

    def get(self):
        if self.size > 0:
            return self.key[1], self.val[1]
        return 0

    def pop(self):
        res = self.get()
        self._swap(1, self.size)
        self.key.pop()
        self.val.pop()
        self.size -= 1
        self._heapify_down(1)
        return res

    def insert(self, key, val):
        if key < 0:
            raise ValueError()
        self.key.append(key)
        self.val.append(val)
        self.size += 1
        self._heapify_up(self.size)

    def update_key(self, old, new):
        i = self._find_key_index(1, old)
        if i is None:
            raise ValueError("value not found")
        self.key[i] = new
        self._heapify_down(1)

    def update_value(self, key, val):
        i = self._find_key_index(1, key)
        if i is None:
            raise ValueError("value not found")
        self.val[i] = val

    def not_empty(self):
        return self.size > 0

    def empty(self):
        return self.size == 0

    def has_key(self, key):
        return self._find_key_index(1, key) is not None

    def _find_key_index(self, i, val):
        if self.key[i] == val:
            return i
        if self._has_left_child(i):
            return self._find_key_index(i * 2, val)
        elif self._has_right_child(i):
            return self._find_key_index(i * 2 + 1, val)
        return None

    def _heapify_down(self, i):
        while self._has_left_child(i):
            min_index = self._min_child_index(i)
            if self.key[i] > self.key[min_index]:
                self._swap(i, min_index)
            i += 1

    def _heapify_up(self, i):
        while self._has_parent(i):
            p = self._get_parent(i)
            if p > self.key[i]:
                self._swap(int(i / 2), i)
            i -= 1

    def _min_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.key[i * 2] < self.key[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def _has_parent(self, i):
        return i < len(self.key) and i / 2 > 0

    def _get_parent(self, i):
        if self._has_parent(i):
            return self.key[int(i / 2)]
        return None

    def _has_left_child(self, i):
        return i * 2 < len(self.key)

    def _get_left_child(self, i):
        if self._has_left_child(i):
            return self.key[i * 2]
        return None

    def _has_right_child(self, i):
        return i * 2 + 1 < len(self.key)

    def _get_right_child(self, i):
        if self._has_right_child(i):
            return self.key[i * 2 + 1]
        return None

    def _swap(self, i, j):
        self.key[i], self.key[j] = self.key[j], self.key[i]
        self.val[i], self.val[j] = self.val[j], self.val[i]

    def __str__(self):
        for i in range(1, len(self.key)):
            print("{} - {}".format(self.key[i], self.val[i]))
        return ""


q = PriorityQueue()
q.insert(2.7, "a")
q.insert(1.3, "b")
q.insert(0.5, "c")

print(q)

q.update_key(2.7, 0.1)
q.update_value(0.1, "_a")

print(q)

while q.not_empty():
    key, val = q.pop()
    print(key, val)
