.global _start

_start:
    mov $69, %rax
    push %rax
    mov $60, %rax
    pop %rdi 
    syscall
    mov $60, %rax
    mov $0, %rdi
    syscall
