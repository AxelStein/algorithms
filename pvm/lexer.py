from pvm import const


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

    def _forward(self):
        self.pos += 1

    def _pop_next_char(self):
        self._forward()
        if self.pos < len(self.txt):
            return self.txt[self.pos]

    def _peek_char(self):
        if self.pos < len(self.txt):
            return self.txt[self.pos]

    def _peek_next_char(self):
        p = self.pos + 1
        if p < len(self.txt):
            return self.txt[p]

    def _get_digit(self, ch):
        is_float = False
        buf = []
        while ch.isdigit():
            buf.append(ch)
            ch = self._pop_next_char()
            if not ch:
                break
            if ch == '.':
                is_float = True
                buf.append('.')
                ch = self._pop_next_char()
        s = ''.join(buf)
        if is_float:
            return Token(const.FLOAT, float(s))
        return Token(const.INT, int(s))

    def _get_name(self, ch):
        buf = []
        while ch.isalpha() or ch.isdigit():
            buf.append(ch)
            ch = self._pop_next_char()
            if not ch:
                break
        s = ''.join(buf)
        if s == 'for':
            return Token(const.FOR)
        elif s == 'while':
            return Token(const.WHILE)
        elif s == 'if':
            return Token(const.IF)
        elif s == 'else':
            return Token(const.ELSE)
        elif s == 'elif':
            return Token(const.ELIF)
        elif s == 'return':
            return Token(const.RETURN)
        elif s == 'true':
            return Token(const.TRUE)
        elif s == 'false':
            return Token(const.FALSE)
        elif s == 'null':
            return Token(const.NULL)
        elif s == 'and':
            return Token(const.AND)
        elif s == 'or':
            return Token(const.OR)
        elif s == 'in':
            return Token(const.IN)
        elif s == 'func':
            return Token(const.FUNC)
        elif s == 'break':
            return Token(const.BREAK)
        elif s == 'continue':
            return Token(const.CONTINUE)
        elif s == 'range':
            return Token(const.RANGE)
        return Token(const.NAME, ''.join(buf))

    def _get_op(self, ch):
        self._forward()
        if ch == '+':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.ADD_ASN)
            return Token(const.ADD)
        elif ch == '-':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.SUB_ASN)
            return Token(const.SUB)
        elif ch == '*':
            c = self._peek_char()
            if c == '*':
                self._forward()
                return Token(const.EXP)
            if c == '=':
                self._forward()
                return Token(const.MUL_ASN)
            return Token(const.MUL)
        elif ch == '/':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.DIV_ASN)
            return Token(const.DIV)
        elif ch == '(':
            return Token(const.L_PAREN)
        elif ch == ')':
            return Token(const.R_PAREN)
        elif ch == '[':
            return Token(const.L_BRACKET)
        elif ch == ']':
            return Token(const.R_BRACKET)
        elif ch == '{':
            return Token(const.L_BRACE)
        elif ch == '}':
            return Token(const.R_BRACE)
        elif ch == ',':
            return Token(const.COMA)
        elif ch == '.':
            return Token(const.DOT)
        elif ch == '"':
            return Token(const.QUOTE)
        elif ch == '\'':
            return Token(const.QUOTE)
        elif ch == '<':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.LESS_OR_EQUALS)
            return Token(const.LESS)
        elif ch == '>':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.GREATER_OR_EQUALS)
            return Token(const.GREATER)
        elif ch == '=':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.EQUALS)
            return Token(const.ASN)
        elif ch == '!':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.NOT_EQUALS)
        elif ch == '%':
            if self._peek_char() == '=':
                self._forward()
                return Token(const.MOD_ASN)
            return Token(const.MOD)

    def next_token(self):
        if self.pos >= len(self.txt):
            return Token(const.EOF)

        ch = self._peek_char()
        while ch == ' ' or ch == '\t':
            ch = self._pop_next_char()
        if ch == '\n':
            self._forward()
            return Token(const.EOL)

        if ch.isdigit():
            return self._get_digit(ch)
        elif ch.isalpha():
            return self._get_name(ch)
        else:
            return self._get_op(ch)

    def peek_next_token(self):
        p = self.pos
        nt = self.next_token()
        self.pos = p
        return nt


'''
with open('program.txt', encoding="utf-8") as file:
    s = file.read()
    print(s)

    l = Lexer(s)
    t = l.next_token()
    while t.type != const.EOF:
        print(t)
        t = l.next_token()
file.close()

l = Lexer('-2 - 4 * -2 + 3 - 2**2')
t = l.next_token()
while t.type != const.EOF:
    print(t)
    t = l.next_token()
'''
