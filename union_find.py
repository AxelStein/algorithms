import numpy


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.group_count = size

        # array containing the size of each group
        self.sz = numpy.empty(size, dtype=int)

        # id[i] points to the parent of i,
        # if id[i] = i, the i is a root node
        self.id = numpy.empty(size, dtype=int)

        for i in range(size):
            self.id[i] = i  # link to itself (self root)
            self.sz[i] = 1

    # Returns root id of the given element
    # Takes amortised constant time
    def find(self, p):
        # find the root of the element
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # path compression
        while p != root:
            next_e = self.id[p]
            self.id[p] = root
            p = next_e

        return root

    # Returns whether or not elements 'p' and 'q'
    # are in the same group
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Returns the number of elements in the group
    # the element 'p' belongs to
    def get_group_size(self, p):
        return self.sz[self.find(p)]

    # Returns the number of groups in this set
    def get_group_count(self):
        return self.group_count

    # Returns the number of elements in this set
    def get_size(self):
        return self.size

    # Merges two groups containing elements 'p' and 'q'
    def union(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        # elements are already in the same group
        if root1 == root2:
            return

        # merge two groups
        if self.sz[root1] > self.sz[root2]:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        else:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2

        self.group_count -= 1


names = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}
names_r = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

u = UnionFind(5)
u.union(names_r["A"], names_r["B"])
u.union(names_r["C"], names_r["B"])
u.union(names_r["E"], names_r["D"])
u.union(names_r["E"], names_r["C"])
print(u.find(names_r["E"]))
print(u.id, u.sz)
