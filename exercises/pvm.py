INTEGER, FLOAT, ADD, SUB, MUL, \
POW, DIV, NAME, EOF = 'INTEGER', 'FLOAT', 'ADD', 'SUB', 'MUL', 'POW', 'DIV', 'NAME', 'EOF'


class Token:
    def __init__(self, t, v=None):
        self.type = t
        self.val = v

    def __str__(self):
        s = 'Token type={}'.format(self.type)
        if self.val:
            s += ', val={}'.format(self.val)
        return s


class Lexer:
    def __init__(self, txt):
        self.txt = txt.strip().replace(' ', '')
        self.pos = 0

    def pop_next_char(self):
        self.pos += 1
        if self.pos < len(self.txt):
            return self.txt[self.pos]

    def peek_next_char(self):
        if self.pos < len(self.txt):
            return self.txt[self.pos]

    def peek_char(self):
        if self.pos < len(self.txt):
            return self.txt[self.pos]

    def get_digit(self, ch):
        is_float = False
        buf = []
        while ch.isdigit():
            buf.append(ch)
            ch = self.pop_next_char()
            if not ch:
                break
            if ch == '.':
                is_float = True
                buf.append('.')
                ch = self.pop_next_char()
        s = ''.join(buf)
        if is_float:
            return Token(FLOAT, float(s))
        return Token(INTEGER, int(s))

    def next_token(self):
        if self.pos >= len(self.txt):
            return Token(EOF)

        ch = self.peek_char()
        if ch.isdigit():
            return self.get_digit(ch)
        if ch.isalpha():
            return self.get_name(ch)

        self.pos += 1
        if ch == '+':
            return Token(ADD)
        elif ch == '-':
            return Token(SUB)
        elif ch == '*':
            if self.peek_next_char() == '*':
                self.pos += 1
                return Token(POW)
            return Token(MUL)
        elif ch == '/':
            return Token(DIV)


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

    def mon_op(self, com, param):
        self.push(param)
        self.push(com)

    def __str__(self):
        return str(self.items)


lex = Lexer('-123 + -47.5 - 13 * -3 / 2 ** 13.0')
token = lex.next_token()
while token.type != EOF:
    print(token)
    token = lex.next_token()


"""
ADD = 0
SUB = 1
MUL = 2
DIV = 3
DEC_VAR = 4
GET_VAR = 5

mem = {}
stack = Stack()
stack.mon_op(DEC_VAR, 'c')
stack.push(ADD)
stack.mon_op(GET_VAR, 'b')
stack.mon_op(GET_VAR, 'a')
stack.push(25)
stack.mon_op(DEC_VAR, 'b')
stack.push(21)
stack.mon_op(DEC_VAR, 'a')

while stack.has_items():
    print(mem)
    print(stack)
    print('----')
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
    elif c == GET_VAR:
        name = stack.pop()
        stack.push(mem[name])
"""
