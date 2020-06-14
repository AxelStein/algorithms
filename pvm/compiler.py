from pvm.lexer import Lexer
from pvm.parser import *


class Compiler:
    def __init__(self, node_list):
        self.node_list = node_list
        self.vars = {}
        print(node_list)

    def get_var_value(self, node):
        if type(node) is Var:
            v = self.vars[node.name]
            s = -1 if node.negative else 1
            v *= s
            return v
        return node

    def calc(self, op, left, right):
        a = self.get_var_value(left)
        b = self.get_var_value(right)

        if op == const.ADD:
            return a + b
        elif op == const.SUB:
            return a - b
        elif op == const.MUL:
            return a * b
        elif op == const.DIV:
            return a / b
        elif op == const.DIV_INT:
            return a // b
        elif op == const.EXP:
            return a ** b
        elif op == const.MOD:
            return a % b

    def calc_expr(self, node):
        if type(node) is Num:
            return node.val
        if type(node) is Var:
            return node
        if type(node) is String:
            return node
        if type(node) is BinOp:
            left = self.calc_expr(node.left)
            right = self.calc_expr(node.right)
            if node.op == const.ASN:
                self.vars[left.name] = self.get_var_value(right)
            else:
                return self.calc(node.op, left, right)

    def compile(self):
        for node in self.node_list:
            self.calc_expr(node)


with open('program.txt', encoding="utf-8") as file:
    lexer = Lexer(file.read())
    parser = Parser(lexer)
    c = Compiler(parser.parse())
    c.compile()
    print(c.vars)
file.close()
