class Stack:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def has_items(self):
        return len(self.items) > 0


ADD = 0
SUB = 1
MUL = 2
DIV = 3
DEC_VAR = 4
GET_VAR = 5

mem = {}
stack = Stack([5, 'a', DEC_VAR, 6, 'b', DEC_VAR])

while stack.has_items():
    c = stack.pop()
    if c == ADD:
        stack.push(stack.pop() + stack.pop())
    elif c == SUB:
        stack.push(stack.pop() - stack.pop())
    elif c == MUL:
        stack.push(stack.pop() * stack.pop())
    elif c == DIV:
        stack.push(stack.pop() // stack.pop())
    elif c == DEC_VAR:
        name = stack.pop()
        val = stack.pop()
        mem[name] = val
        print()

print(mem)
print(mem['a'])
