class Link:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, v):
        link = Link(v)
        link.next = self.first
        self.first = link

    def pop(self):
        if self.empty():
            return None
        tmp = self.first
        self.first = tmp.next
        return tmp

    def remove(self, v):
        if self.empty():
            return None
        prev = None
        current = self.first
        while current and current.val != v:
            prev = current
            current = current.next
        # there is no prev link, so this is the first one
        if not prev:
            self.first = current.next
        elif current:
            prev.next = current.next
        return current

    def empty(self):
        return self.first is None

    def find(self, v):
        link = self.first
        while link and link.val != v:
            link = link.next
        return link

    def __str__(self):
        if self.empty():
            return '[]'
        arr = []
        link = self.first
        while link:
            if link == self.first:
                arr.append('*')
            arr.append(str(link.val))
            link = link.next
            if link:
                arr.append('->')
        return ''.join(arr)


l = LinkedList()
l.add(5)
l.add(7)
l.add(3)
print(l)

print('find 10:', l.find(10))
print('find 5:', l.find(5))

print('remove 10:', l.remove(10))
print(l)
print('remove 7:', l.remove(7))
print(l)
print('remove 5:', l.remove(5))
print(l)
print('remove 3:', l.remove(3))
print(l)

l.add(4)
l.add(1)
l.add(6)
l.add(8)
print(l)

while not l.empty():
    print('pop:', l.pop())

print(l)