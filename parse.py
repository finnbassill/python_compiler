from node import *
from token import *
import sys

class Parse:
    
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.i = 0

    def parse_expr(self) -> Node_Expr:
        if self.__peek() != None and self.__peek().token_type == TokenType.int_lit:
            return Node_Expr(self.__consume())
        else:
            return None

    def parse(self) -> Node_Exit:
        exit_node = Node_Exit(Node_Expr(0))

        while self.__peek() != None:
            if self.__peek() != None and self.__peek().token_type == TokenType._exit and self.__peek(1) != None and self.__peek(1).token_type == TokenType.open_paren:
                self.__consume()
                self.__consume()
                expr_node = self.parse_expr()
                if expr_node != None:
                    exit_node.set_data(expr_node)
                else:
                    print("Invalid Expression")
                    sys.exit(1)
                if self.__peek() == None or self.__peek().token_type != TokenType.closed_paren and self.__peek(1) == None or self.__peek(1).token_type != TokenType.semi:
                    print("Invalid Expression")
                    sys.exit(1)
                self.__consume()
                self.__consume()
        
        self.i = 0
        return exit_node

                

            
    def __peek(self, offset = 0) -> Token:
        if (self.i + offset >= len(self.tokens)):
            return None
        
        return self.tokens[self.i + offset]

    def __consume(self) -> Token:
        temp = self.tokens[self.i]
        self.i += 1
        return temp
