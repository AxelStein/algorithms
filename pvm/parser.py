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


class Parser:
    def __init__(self, lexer):
        self.bp_map = {
            const.EOF: 0,
            const.ADD: 1,
            const.SUB: 1,
            const.MUL: 2,
            const.DIV: 2,
            const.EXP: 3,
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
        if token.type == const.QUOTE:
            self._next_token()
            s = String(self._expr(0))
            self._next_token()
            return s

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

    def parse(self):
        return self._expr(0)
