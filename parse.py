from node import *
from token import *
import sys

class Parse:
    
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.i = 0

    def parse_expr(self) -> Node_Expr:
        if self.__peek() != None and self.__peek().token_type == TokenType.int_lit:
            return Node_Expr(Node_Expr_Int_Lit(self.__consume()))
        elif self.__peek() != None and self.__peek().token_type == TokenType.ident:
            return Node_Expr(Node_Expr_Ident(self.__consume()))
        else:
            return None
    
    def parse_stmt(self) -> Node_Stmt:
        
        if self.__peek() != None and self.__peek().token_type == TokenType._exit and self.__peek(1) != None and self.__peek(1).token_type == TokenType.open_paren:
                
            exit_stmt = None
            self.__consume()
            self.__consume()
            expr_node = self.parse_expr()
            if expr_node != None:
                exit_stmt = Node_Stmt_Exit(expr_node)
            else:
                print("Invalid Expression")
                sys.exit(1)
            if self.__peek() == None or self.__peek().token_type != TokenType.closed_paren and self.__peek(1) == None or self.__peek(1).token_type != TokenType.semi:
                print("Invalid Expression")
                sys.exit(1)
            self.__consume()
            self.__consume()
            return Node_Stmt(exit_stmt)

        elif self.__peek() != None and self.__peek().token_type == TokenType.let and self.__peek(1) != None and self.__peek(1).token_type == TokenType.ident and self.__peek(2) != None and self.__peek(2).token_type == TokenType.eq:
            self.__consume()
            let_stmt = Node_Stmt_Let(None, self.__consume())
            self.__consume()
            expr_node = self.parse_expr()
            if expr_node != None:
                let_stmt.expr = expr_node
            else:
                print("Invalid Expression")
                sys.exit(1)
            if self.__peek() == None or self.__peek().token_type != TokenType.semi:
                print("Invalid Expression")
                sys.exit(1)
            self.__consume()
            return Node_Stmt(let_stmt)
        else:
            return None
         
    def parse_prog(self) -> Node_Prog:
        prog_node = Node_Prog()
        while self.__peek() != None:
            stmt_node = self.parse_stmt()
            if stmt_node != None:
                prog_node.add_stmt(stmt_node)
            else:
                print("Invalid Expression")
                sys.exit(1)
        return prog_node



            
    def __peek(self, offset = 0) -> Token:
        if (self.i + offset >= len(self.tokens)):
            return None
        
        return self.tokens[self.i + offset]

    def __consume(self) -> Token:
        temp = self.tokens[self.i]
        self.i += 1
        return temp
            
