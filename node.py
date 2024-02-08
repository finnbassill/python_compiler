from typing import Union
from token import *

class Node:
    def __init__(self, data):
        self.data = data

class Node_Expr_Int_Lit(Node):
    def __init__(self, int_lit: Token):
        self.int_lit = int_lit

class Node_Expr_Ident(Node):
    def __init__(self, ident: Token):
        self.ident = ident

class Node_Expr(Node):
    def __init__(self, node: Union[Node_Expr_Ident, Node_Expr_Int_Lit]):
        self.node = node

class Node_Stmt_Exit(Node):
    def __init__(self, expr: Node_Expr):
        self.expr = expr

class Node_Stmt_Let(Node):
    def __init__(self, expr: Node_Expr, ident: Token):
        self.expr = expr
        self.ident = ident

class Node_Stmt(Node):
    def __init__(self, node: Union[Node_Stmt_Exit, Node_Stmt_Let]):
        self.node = node

class Node_Prog(Node):
    def __init__(self):
        self.stmts = []
    def add_stmt(self, stmt: Node_Stmt):
        self.stmts.append(stmt)
