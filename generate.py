from token import *
from node import *

class Generate:

    def __init__(self, prog: Node_Prog, output_file: str):
        self.prog = prog
        self.output_file = output_file
        self.output = ".global _start\n\n_start:\n"

    def gen_expr(self, expr: Node_Expr):
        if isinstance(expr.node, Node_Expr_Int_Lit):
            self.output += f"    mov ${expr.node.int_lit.value}, %rax\n"
            self.output += "    push %rax\n"
        else:
            pass

    def gen_stmt(self, stmt: Node_Stmt):
        if isinstance(stmt.node, Node_Stmt_Exit):
            self.gen_expr(stmt.node.expr)

            self.output += "    mov $60, %rax\n"
            self.output += "    pop %rdi \n"
            self.output += "    syscall\n"
        else:
            pass

    def gen_prog(self): 
        for stmt in self.prog.stmts:
            self.gen_stmt(stmt)




        self.output += "    mov $60, %rax\n"
        self.output += "    mov $0, %rdi\n"
        self.output += "    syscall\n"



        try:            
            with open(self.output_file, 'w') as file:
                file.write(self.output)
        except FileNotFoundError:
            print("File '" + sys.argv[1] + "' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
