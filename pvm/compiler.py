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

    def d(self, node):
        if type(node) is Num:
            return node.val
        if type(node) is Var:
            return node
        if type(node) is BinOp:
            left = self.d(node.left)
            right = self.d(node.right)
            if node.op == const.ADD:
                return self.get_var_value(left) + self.get_var_value(right)
            elif node.op == const.SUB:
                return self.get_var_value(left) - self.get_var_value(right)
            elif node.op == const.MUL:
                return self.get_var_value(left) * self.get_var_value(right)
            elif node.op == const.DIV:
                return self.get_var_value(left) / self.get_var_value(right)
            elif node.op == const.EXP:
                return self.get_var_value(left) ** self.get_var_value(right)
            elif node.op == const.ASN:
                self.vars[left.name] = self.get_var_value(right)

    def compile(self):
        for node in self.node_list:
            self.d(node)


with open('program.txt', encoding="utf-8") as file:
    lexer = Lexer(file.read())
    parser = Parser(lexer)
    c = Compiler(parser.parse())
    c.compile()
    print(c.vars)
file.close()
