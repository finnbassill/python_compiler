from token import *

def tokens_to_s(tokens: list, output_file: str):

    asm_str = ".global _start\n\n_start:\n"

    i = 0
    while i < len(tokens):
        if tokens[i].token_type == TokenType._exit:
            if tokens[i + 1].token_type == TokenType.int_lit:
                if tokens[i + 2].token_type == TokenType.semi:
                    asm_str += "    mov $60, %rax\n"
                    asm_str += f"    mov ${tokens[i+1].value}, %rdi\n"
                    asm_str += "    syscall\n"
                    i += 1
                i += 1
            i += 1
        i += 1

    try:
        with open(output_file, 'w') as file:
            file.write(asm_str)
    except FileNotFoundError:
        print("File '" + sys.argv[1] + "' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
