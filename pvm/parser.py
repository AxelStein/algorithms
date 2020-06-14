from pvm import const


class BinOp:
    def __init__(self, op=None, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return '{} ->{} =>{} '.format(self.op, self.left, self.right)

    def __repr__(self):
        return str(self)


class Num:
    def __init__(self, val=None):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)


class String:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)


class Var:
    def __init__(self, name, negative=False):
        self.name = name
        self.negative = negative

    def __str__(self):
        s = '-' if self.negative else ''
        return s + self.name

    def __repr__(self):
        return str(self)


class If:
    def __init__(self):
        self.cond = None
        self.is_true = None
        self.is_false = None

    def __str__(self):
        return 'If cond:{} true:{} false:{} '.format(self.cond, self.is_true, self.is_false)

    def __repr__(self):
        return str(self)


class Parser:
    def __init__(self, lexer):
        self.bp_map = {
            const.EOF: 0,
            const.EOL: 0,
            const.ASN: 1,
            const.OR: 2,
            const.AND: 3,
            const.EQUALS: 4,
            const.NOT_EQUALS: 4,
            const.LESS: 5,
            const.LESS_OR_EQUALS: 5,
            const.GREATER: 5,
            const.GREATER_OR_EQUALS: 5,
            const.ADD: 6,
            const.SUB: 6,
            const.MUL: 7,
            const.DIV: 7,
            const.MOD: 7,
            const.EXP: 8,
        }
        self.lexer = lexer
        self.token = None

    # return next token from lexer
    def _next_token(self):
        self.token = self.lexer.next_token()
        return self.token

    def _peek_next_token(self):
        return self.lexer.peek_next_token()

    # return binding power of operator
    def _bp(self, token):
        if token.type in self.bp_map.keys():
            return self.bp_map[token.type]
        return 0

    # return null-denotation operator with no left context
    def _nud(self, token):
        negative = False
        if token.type == const.SUB:
            negative = True
            token = self._next_token()
        if token.type in (const.INT, const.FLOAT):
            sign = -1 if negative else 1
            return Num(token.val * sign)
        if token.type == const.STRING:
            return String(token.val)
        if token.type == const.NAME:
            return Var(token.val, negative)
        if token.type == const.L_PAREN:
            r = self._expr(0)
            self._next_token()
            return r
        if token.type == const.IF:
            return self._if()

    def check_token(self, t):
        return self.token.type == t

    def require_token(self, t):
        r = self.check_token(t)
        if not r:
            raise ValueError(t + ' is required')
        return r

    def _if(self):
        i = If()
        i.cond = self._expr(0)

        self._next_token()
        self.require_token(const.L_BRACE)

        i.is_true = self._expr_list()
        self.require_token(const.R_BRACE)
        self._next_token()

        if self.check_token(const.ELSE):
            self._next_token()
            self.require_token(const.L_BRACE)

            i.is_false = self._expr_list()
            self.require_token(const.R_BRACE)
            self._next_token()
        return i

    # return left-denotation operator with left context
    def _led(self, left, token):
        bp = self._bp(token)
        if token.type == const.EXP:
            bp -= 1
        return BinOp(token.type, left, self._expr(bp))

    # rbp is binding power of the right operator
    def _expr(self, rbp):
        left = self._nud(self._next_token())
        while self._bp(self._peek_next_token()) > rbp:
            left = self._led(left, self._next_token())
        return left

    def _expr_list(self):
        expr_list = []

        self.lexer.skip_new_lines()
        expr = self._expr(0)
        while expr:
            expr_list.append(expr)
            self._next_token()
            self.lexer.skip_new_lines()
            expr = self._expr(0)
        return expr_list

    def parse(self):
        return self._expr_list()
