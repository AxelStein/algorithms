INTEGER, FLOAT, NAME, TRUE, FALSE, NIL, NOT = 'INTEGER', 'FLOAT', 'NAME', 'TRUE', 'FALSE', 'NIL', 'NOT'
ADD, SUB, MUL, POW, DIV = 'ADD', 'SUB', 'MUL', 'POW', 'DIV'
ASSIGNMENT, EQUALS, COLON, LEFT_PARENTHESIS, RIGHT_PARENTHESIS, LEFT_BRACKET, RIGHT_BRACKET, COMA, DOT, QUOTE = 'ASSIGNMENT', 'EQUALS', 'COLON', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'COMA', 'DOT', 'QUOTE'
IF, ELSE, ELIF, FOR, WHILE, RETURN, AND, OR, IS = 'IF', 'ELSE', 'ELIF', 'FOR', 'WHILE', 'RETURN', 'AND', 'OR', 'IS'
EOF = 'EOF'


class Node:
    def __init__(self, t, v=None):
        self.type = t
        self.val = v
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node type={}, value={}, left={}, right={}'.format(self.type, self.val, self.left, self.right)


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.root = None

    def next_token(self):
        return self.lexer.next_token()

    def parse(self):
        token = self.next_token()
        if token.type == NAME:
            nt = self.next_token()
            if nt.type == ASSIGNMENT:
                node = Node(ASSIGNMENT)
                node.left = token
                node.right = self.next_token()
                return node


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
        self.txt = txt.strip()
        self.pos = 0

    def pop_next_char(self):
        self.pos += 1
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

    def get_name(self, ch):
        buf = []
        while ch.isalpha() or ch.isdigit():
            buf.append(ch)
            ch = self.pop_next_char()
            if not ch:
                break
        s = ''.join(buf)
        if s == 'for':
            return Token(FOR)
        elif s == 'while':
            return Token(WHILE)
        elif s == 'if':
            return Token(IF)
        elif s == 'else':
            return Token(ELSE)
        elif s == 'elif':
            return Token(ELIF)
        elif s == 'return':
            return Token(RETURN)
        elif s == 'true':
            return Token(TRUE)
        elif s == 'false':
            return Token(FALSE)
        elif s == 'nil':
            return Token(NIL)
        elif s == 'and':
            return Token(AND)
        elif s == 'or':
            return Token(OR)
        elif s == 'is':
            return Token(IS)
        return Token(NAME, ''.join(buf))

    def next_token(self):
        if self.pos >= len(self.txt):
            return Token(EOF)

        ch = self.peek_char()
        while ch == ' ':
            ch = self.pop_next_char()

        if ch.isdigit():
            return self.get_digit(ch)
        elif ch.isalpha():
            return self.get_name(ch)

        self.pos += 1
        if ch == '+':
            return Token(ADD)
        elif ch == '-':
            return Token(SUB)
        elif ch == '*':
            if self.peek_char() == '*':
                self.pos += 1
                return Token(POW)
            return Token(MUL)
        elif ch == '/':
            return Token(DIV)
        elif ch == ':':
            return Token(COLON)
        elif ch == '(':
            return Token(LEFT_PARENTHESIS)
        elif ch == ')':
            return Token(RIGHT_PARENTHESIS)
        elif ch == '[':
            return Token(LEFT_BRACKET)
        elif ch == ']':
            return Token(RIGHT_BRACKET)
        elif ch == ',':
            return Token(COMA)
        elif ch == '.':
            return Token(DOT)
        elif ch == '"':
            return Token(QUOTE)
        elif ch == '\'':
            return Token(QUOTE)
        elif ch == '=':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(EQUALS)
            return Token(ASSIGNMENT)


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


parser = Parser(Lexer(input()))
print(parser.parse())
"""
lex = Lexer(input())
token = lex.next_token()
while token.type != EOF:
    print(token)
    token = lex.next_token()
"""

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
