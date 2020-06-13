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

    def next_token(self, forward=True):
        if self.pos >= len(self.txt):
            return Token(const.EOF)

        ch = self._peek_char()
        while ch == ' ' or ch == '\t' or ch == '\n':
            ch = self._pop_next_char()

        if ch.isdigit():
            return self._get_digit(ch)

        if forward:
            self._forward()
        if ch == '+':
            return Token(const.ADD)
        elif ch == '-':
            return Token(const.SUB)
        elif ch == '*':
            return Token(const.MUL)
        elif ch == '/':
            return Token(const.DIV)

    def peek_next_token(self):
        return self.next_token(False)
