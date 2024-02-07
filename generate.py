from token import *
from node import *

class Generate:

    def __init__(self, root: Node, output_file: str):
        self.root = root
        self.output_file = output_file

    def tokens_to_s(self):
        asm_str = ".global _start\n\n_start:\n"

        asm_str += "    mov $60, %rax\n"
        asm_str += f"    mov ${self.root.get_data().get_data().value}, %rdi\n"
        asm_str += "    syscall\n"



        try:            
            with open(self.output_file, 'w') as file:
                file.write(asm_str)
        except FileNotFoundError:
            print("File '" + sys.argv[1] + "' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
