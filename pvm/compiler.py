from pvm import const
from pvm.lexer import Lexer
from pvm.parser import Parser, Num, BinOp


class Compiler:
    def __init__(self, ast):
        self.ast = ast
        print(ast)

    def d(self, node):
        if type(node) is Num:
            return node.val
        if type(node) is BinOp:
            left = self.d(node.left)
            right = self.d(node.right)
            if node.op == const.ADD:
                return left + right
            elif node.op == const.SUB:
                return left - right
            elif node.op == const.MUL:
                return left * right
            elif node.op == const.DIV:
                return left / right

    def compile(self):
        return self.d(self.ast)


p = Parser(Lexer('-2 - 4 * -2 + 3 - 2'))
c = Compiler(p.parse())
print(c.compile())
