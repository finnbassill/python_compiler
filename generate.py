from token import *

class Generate():

    def __init__(self, tokens: list, output_file: str):
        self.tokens = tokens
        self.output_file = output_file
        self.i = 0

    def tokens_to_s(self):

        asm_str = ".global _start\n\n_start:\n"

        while self.__peek() != None:
            if self.__peek() != None and self.__peek().token_type == TokenType._exit:
                if self.__peek(1) != None and self.__peek(1).token_type == TokenType.int_lit:
                    if self.__peek(2) != None and self.__peek(2).token_type == TokenType.semi:
                        self.__consume()
                        asm_str += "    mov $60, %rax\n"
                        asm_str += f"    mov ${self.__consume().value}, %rdi\n"
                        asm_str += "    syscall\n"
                        self.__consume()
        try:
            with open(self.output_file, 'w') as file:
                file.write(asm_str)
        except FileNotFoundError:
            print("File '" + sys.argv[1] + "' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def __peek(self, offset = 0) -> str:
        if (self.i + offset >= len(self.tokens)):
            return None
        
        return self.tokens[self.i + offset]

    def __consume(self) -> str:
        temp_char = self.tokens[self.i]
        self.i += 1
        return temp_char