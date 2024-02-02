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

def tokenize(file_str: str) -> list:
    tokens = []
    buf = ''

    i = 0
    while i < len(file_str):
        if file_str[i].isalpha():
            buf += file_str[i]
            i += 1
            while file_str[i].isalnum():
                buf += file_str[i]
                i += 1  
            if buf == 'exit':
                tokens.append(Token(TokenType._exit, None))
                buf = ''
            else:
                print("Unrecognized token")
                sys.exit(1)
        elif file_str[i].isdigit():
            buf += file_str[i]
            i += 1
            while file_str[i].isdigit():
                buf += file_str[i]
                i += 1
            tokens.append(Token(TokenType.int_lit, buf))
            buf = ''
        elif file_str[i] == ';':
            tokens.append(Token(TokenType.semi, None))
            i += 1
        elif file_str[i] == ' ':
            i += 1
        else:
            print("Unrecognized token")
            sys.exit(1)
    return tokens