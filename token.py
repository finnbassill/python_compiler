from enum import Enum
import sys

class TokenType(Enum):
    _exit = "EXIT"
    int_lit = "INTEGER_LITERAL"
    open_paren = "OPEN_PAREN"
    closed_paren = "CLOSED_PAREN"
    semi = "SEMI_COLON"

class Token:
    def __init__(self, token_type: TokenType, value: any):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token({self.token_type}, {self.value})"

class Tokenize:
    def __init__(self, file_str: str):
        self.i = 0
        self.file_str = file_str

    def tokenize(self) -> list[Token]:
        tokens = []
        buf = ''

        while self.__peek() != None:

            if self.__peek() != None and self.__peek().isalpha():
                buf += self.__consume()
                while self.__peek() != None and self.__peek().isalnum():
                    buf += self.__consume()
                if buf == 'exit':
                    tokens.append(Token(TokenType._exit, None))
                    buf = ''
                else:
                    print("Unrecognized token")
                    sys.exit(1)

            elif self.__peek() != None and self.__peek().isdigit():
                buf += self.__consume()
                while self.__peek() != None and self.__peek().isdigit():
                    buf += self.__consume()
                tokens.append(Token(TokenType.int_lit, buf))
                buf = ''
            elif self.__peek() != None and self.__peek() == '(':
                tokens.append(Token(TokenType.open_paren, None))
                self.__consume()
            elif self.__peek() != None and self.__peek() == ')':
                tokens.append(Token(TokenType.closed_paren, None))
                self.__consume()
            elif self.__peek() != None and self.__peek() == ';':
                tokens.append(Token(TokenType.semi, None))
                self.__consume()
            elif self.__peek() != None and self.__peek() == ' ':
                self.__consume()
            else:
                print("Unrecognized token")
                sys.exit(1)
        return tokens

    
    def __peek(self, offset = 0) -> str:
        if (self.i + offset >= len(self.file_str)):
            return None
        
        return self.file_str[self.i + offset]

    def __consume(self) -> str:
        temp_char = self.file_str[self.i]
        self.i += 1
        return temp_char
        