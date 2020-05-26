class MaxHeap:
    def __init__(self):
        self.arr = []

    def insert(self, v):
        self.arr.append(v)
        self.heapify_up()

    def heapify_up(self):
        pass
