.global _start

_start:
    mov $60, %rax
    mov $69, %rdi
    syscall
