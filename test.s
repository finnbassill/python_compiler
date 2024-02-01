.section .data
.section .text
.global _start

_start:
    mov $60, %rax   # syscall number for exit
    mov $10, %rdi    # exit status
    syscall
