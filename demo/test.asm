.data
str_nl: .asciz "\n"
.text
j Lmain
L0:
sw ra, (sp)
L1:
li a7, 5
ecall
mv t1, a0
sw t1, -12(sp)
L2:
lw t1, -12(sp)
li t2, 5
bgt t1, t2, L4
L3:
j L11
L4:
lw t1, -12(sp)
li t2, 0
bgt t1, t2, L6
L5:
j L10
L6:
lw t1, -12(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L7:
lw t1, -12(sp)
li t2, 1
sub t1, t1, t2
sw t1, -20(sp)
L8:
lw t1, -20(sp)
sw t1, -12(sp)
L9:
j L4
L10:
j L18
L11:
li t1, 10
sw t1, -16(sp)
L12:
lw t1, -12(sp)
lw t2, -16(sp)
blt t1, t2, L14
L13:
j L18
L14:
lw t1, -12(sp)
mv a0, t1
li a7, 1
ecall
la a0, str_nl
li a7, 4
ecall
L15:
lw t1, -12(sp)
li t2, 1
add t1, t1, t2
sw t1, -24(sp)
L16:
lw t1, -24(sp)
sw t1, -12(sp)
L17:
j L12
L18:
lw ra, (sp)
jr ra
L19:
Lmain:
L20:
sw sp, -4(fp)
addi sp, sp, 28
jal L0
addi sp, sp, -28
L21:
L22:
li a0, 0
li a7, 93
ecall
