INTEGER, FLOAT, NAME, TRUE, FALSE, NIL, NOT = 'INTEGER', 'FLOAT', 'NAME', 'TRUE', 'FALSE', 'NIL', 'NOT'
ADD, ADD_ASN, SUB, SUB_ASN, MUL, MUL_ASN, EXP, DIV, DIV_ASN, MOD, MOD_ASN = 'ADD', 'ADD_ASN', 'SUB', 'SUB_ASN', 'MUL', \
                                                                            'MUL_ASN', 'EXP', 'DIV', 'DIV_ASN', 'MOD', 'MOD_ASN'
ASSIGNMENT, EQUALS, NOT_EQUALS, LESS, GREATER, LESS_OR_EQUALS, GREATER_OR_EQUALS, COLON, LEFT_PARENTHESIS, RIGHT_PARENTHESIS, \
LEFT_BRACKET, RIGHT_BRACKET, LEFT_BRACE, RIGHT_BRACE, COMA, DOT, QUOTE,  = 'ASSIGNMENT', 'EQUALS', 'NOT_EQUALS', 'LESS', 'GREATER', 'LESS_OR_EQUALS', \
                                                'GREATER_OR_EQUALS', 'COLON', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', \
                                                'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_BRACE', 'RIGHT_BRACE', 'COMA', 'DOT', 'QUOTE'
IF, ELSE, ELIF, FOR, WHILE, RETURN, AND, OR, IS, IN, FUNC, BREAK, CONTINUE, RANGE = 'IF', 'ELSE', 'ELIF', 'FOR', 'WHILE', 'RETURN', 'AND', 'OR', 'IS', 'IN', 'FUNC', 'BREAK', 'CONTINUE', 'RANGE'
EOL, EOF = 'EOL', 'EOF'


class AST(object):
    pass


class BinOp(AST):
    def __init__(self, op, left, right):
        self.token = self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return '[BinOp token={}, left={}, right={}]'.format(self.token, self.left, self.right)

    def __repr__(self):
        return str(self)


class Num(AST):
    def __init__(self, t, val):
        self.type = t
        self.val = val

    def __str__(self):
        return '[Num type={}, val={}]'.format(self.type, self.val)

    def __repr__(self):
        return str(self)


class String(AST):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return '[String val={}]'.format(self.val)

    def __repr__(self):
        return str(self)


class IfBranch(AST):
    def __init__(self, condition=None):
        self.condition = condition
        self.is_true = []
        self.is_false = []

    def __str__(self):
        return '[IfBranch cond={}, is_true={}, is_false={}]'.format(self.condition, self.is_true, self.is_false)


class Var(AST):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '[Var name={}]'.format(self.name)

    def __repr__(self):
        return str(self)


class Call(AST):
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __str__(self):
        return '[Call name={}, params={}]'.format(self.name, self.params)

    def __repr__(self):
        return str(self)


class Return(AST):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return '[Return expr={}]'.format(self.expr)

    def __repr__(self):
        return str(self)


class WhileLoop(AST):
    def __init__(self, condition=None):
        self.condition = condition
        self.body = []

    def __str__(self):
        return '[WhileLoop condition={}, body={}]'.format(self.condition, self.body)

    def __repr__(self):
        return str(self)


class ForLoop(AST):
    def __init__(self, var=None):
        self.var = var
        self.start = 0
        self.stop = None
        self.step = 1
        self.body = None

    def __str__(self):
        return '[ForLoop var={}, start={}, stop={}, step={}, body={}]'.format(self.var, self.start, self.stop, self.step, self.body)

    def __repr__(self):
        return str(self)


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = lexer.next_token()
        self.bin_op_pr = {
            ASSIGNMENT: 1,
            ADD_ASN: 1,
            SUB_ASN: 1,
            DIV_ASN: 1,
            MOD_ASN: 1,
            OR: 2,
            AND: 3,
            EQUALS: 4,
            NOT_EQUALS: 4,
            LESS: 5,
            LESS_OR_EQUALS: 5,
            GREATER: 5,
            GREATER_OR_EQUALS: 5,
            ADD: 6,
            SUB: 6,
            MUL: 7,
            DIV: 7,
            MOD: 7,
            EXP: 8,
            LEFT_PARENTHESIS: 9,
            RIGHT_PARENTHESIS: 9,
            LEFT_BRACKET: 9,
            RIGHT_BRACKET: 9,
            DOT: 9,
        }

    def get_precedence(self):
        t = self.token
        if t.type in self.bin_op_pr.keys():
            return self.bin_op_pr[t.type]
        return 0

    def next_token(self):
        self.token = self.lexer.next_token()
        return self.token

    def parse_num(self):
        t = self.token
        self.next_token()
        return Num(t.type, t.val)

    def parse_name(self):
        t = self.token
        n = self.next_token()
        if n.type == LEFT_PARENTHESIS:
            self.next_token()
            params = []
            self.parse_arg_expr(params)
            if self.token.type == RIGHT_PARENTHESIS:
                self.next_token()
                return Call(t.val, params)
        return Var(t.val)

    def parse_paren(self):
        self.next_token()
        r = self.parse_expr()
        self.next_token()
        return r

    def parse_string(self):
        self.next_token()
        r = self.parse_expr()
        self.next_token()
        return String(r)

    def parse_primary(self):
        t = self.token
        if t.type == INTEGER or t.type == FLOAT:
            return self.parse_num()
        elif t.type == QUOTE:
            return self.parse_string()
        elif t.type == NAME:
            return self.parse_name()
        elif t.type == LEFT_PARENTHESIS:
            return self.parse_paren()
        elif t.type == IF:
            return self.parse_if()
        elif t.type == RETURN:
            return self.parse_return()
        elif t.type == WHILE:
            return self.parse_while()
        elif t.type == FOR:
            return self.parse_for()

    def parse_bin_op(self, left):
        t = self.token
        c_pr = self.get_precedence()  # current precedence
        if t.type in (ADD, ADD_ASN, SUB, SUB_ASN, MUL, MUL_ASN, DIV, DIV_ASN, EXP, EQUALS, NOT_EQUALS, LESS, LESS_OR_EQUALS, GREATER, GREATER_OR_EQUALS, AND, OR, ASSIGNMENT, MOD, MOD_ASN):
            self.next_token()
            right = self.parse_expr()
            if type(right) is BinOp:
                r_pr = self.bin_op_pr[right.token.type]
                if c_pr > r_pr:
                    # if current token precedence is greater then
                    # precedence of the right one
                    # then swap BinOps
                    right.left = BinOp(t, left, right.left)
                    return right
            return BinOp(t, left, right)

    def parse_expr(self):
        left = self.parse_primary()
        n = self.parse_bin_op(left)
        if n:
            return n
        return left

    def parse_arg_expr(self, params):
        n = self.parse_expr()
        if n:
            params.append(n)

        t = self.token
        if t.type == COMA:
            self.next_token()
            self.parse_arg_expr(params)

    def check_token(self, t):
        return self.token.type == t

    def require_token(self, t):
        r = self.check_token(t)
        if not r:
            raise ValueError(t + ' is required')
        return r

    def parse_expr_list(self):
        expr_list = []
        expr = self.parse_expr()
        while expr:
            expr_list.append(expr)
            expr = self.parse_expr()
        return expr_list

    def parse_return(self):
        self.next_token()
        return Return(self.parse_expr())

    def parse_for(self):
        self.next_token()

        var = self.parse_primary()
        if not var:
            raise ValueError('For loop requires var')

        for_loop = ForLoop(var)

        self.require_token(IN)
        self.next_token()

        self.require_token(RANGE)
        self.next_token()

        self.require_token(LEFT_PARENTHESIS)
        self.next_token()

        args = []
        self.parse_arg_expr(args)

        arg_count = len(args)
        if arg_count == 1:
            for_loop.stop = args[0]
        elif arg_count > 1:
            for_loop.start = args[0]
            for_loop.stop = args[1]
            if arg_count == 3:
                for_loop.step = args[2]
        else:
            raise ValueError('Range requires at least 1 argument')

        self.require_token(RIGHT_PARENTHESIS)
        self.next_token()

        self.require_token(LEFT_BRACE)
        self.next_token()

        for_loop.body = self.parse_expr_list()

        self.require_token(RIGHT_BRACE)
        self.next_token()

        return for_loop

    def parse_while(self):
        self.next_token()

        while_loop = WhileLoop(self.parse_expr())
        if self.require_token(LEFT_BRACE):
            self.next_token()
            while_loop.body = self.parse_expr_list()
            self.require_token(RIGHT_BRACE)
        self.next_token()
        return while_loop

    def parse_if(self):
        self.next_token()

        if_branch = IfBranch()
        if_branch.condition = self.parse_expr()

        if self.require_token(LEFT_BRACE):
            self.next_token()
            if_branch.is_true = self.parse_expr_list()
        if self.require_token(RIGHT_BRACE):
            self.next_token()
            if self.check_token(ELSE):
                self.next_token()
                if self.require_token(LEFT_BRACE):
                    self.next_token()
                    if_branch.is_false = self.parse_expr_list()
                    self.require_token(RIGHT_BRACE)
        self.next_token()
        return if_branch

    def parse(self):
        return self.parse_expr_list()


class Token:
    def __init__(self, t, v=None):
        self.type = t
        self.val = v

    def __str__(self):
        s = '[Token type={}'.format(self.type)
        if self.val:
            s += ', val={}'.format(self.val)
        s += ']'
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
        elif s == 'in':
            return Token(IN)
        elif s == 'func':
            return Token(FUNC)
        elif s == 'break':
            return Token(BREAK)
        elif s == 'continue':
            return Token(CONTINUE)
        elif s == 'range':
            return Token(RANGE)
        return Token(NAME, ''.join(buf))

    def next_token(self):
        if self.pos >= len(self.txt):
            return Token(EOF)

        ch = self.peek_char()
        while ch == ' ' or ch == '\t' or ch == '\n':
            ch = self.pop_next_char()

        if ch.isdigit():
            return self.get_digit(ch)
        elif ch.isalpha():
            return self.get_name(ch)

        self.pos += 1
        if ch == '+':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(ADD_ASN)
            return Token(ADD)
        elif ch == '-':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(SUB_ASN)
            return Token(SUB)
        elif ch == '*':
            c = self.peek_char()
            if c == '*':
                self.pos += 1
                return Token(EXP)
            elif c == '=':
                self.pos += 1
                return Token(MUL_ASN)
            return Token(MUL)
        elif ch == '/':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(DIV_ASN)
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
        elif ch == '{':
            return Token(LEFT_BRACE)
        elif ch == '}':
            return Token(RIGHT_BRACE)
        elif ch == ',':
            return Token(COMA)
        elif ch == '.':
            return Token(DOT)
        elif ch == '"':
            return Token(QUOTE)
        elif ch == '\'':
            return Token(QUOTE)
        elif ch == '<':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(LESS_OR_EQUALS)
            return Token(LESS)
        elif ch == '>':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(GREATER_OR_EQUALS)
            return Token(GREATER)
        elif ch == '=':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(EQUALS)
            return Token(ASSIGNMENT)
        elif ch == '!':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(NOT_EQUALS)
        elif ch == '%':
            if self.peek_char() == '=':
                self.pos += 1
                return Token(MOD_ASN)
            return Token(MOD)
        """
        elif ch == '\n':
            return Token(EOL)
        """


with open('pvm.txt', encoding="utf-8") as file:
    lexer = Lexer(file.read())
    parser = Parser(lexer)
    res = parser.parse()
    for e in res:
        print(e)
file.close()

"""
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
        
lex = Lexer(input())
token = lex.next_token()
while token.type != EOF:
    print(token)
    token = lex.next_token()


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
