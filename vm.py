
MEMORY_MAX = 1 << 16   # 65536 locations

# Condition Flags

FL_POS = 1 << 0   # Positive Flag (binary 0001)
FL_ZRO = 1 << 1   # Zero flag (binary 0010)
FL_NEG = 1 << 2   # Negative flag (binary 0100)

# Registers

R_R0    =  0
R_R1    =  1
R_R2    =  2
R_R3    =  3
R_R4    =  4
R_R5    =  5
R_R6    =  6
R_R7    =  7
R_PC    =  8   # Program counter
R_COND  =  9
R_COUNT = 10   # Total number of registers

reg = [0] * R_COUNT

# Opcodes

OP_BR   =  0   # branch
OP_ADD  =  1   # add
OP_LD   =  2   # load
OP_ST   =  3   # store
OP_JSR  =  4   # jump register
OP_AND  =  5   # bitwise and
OP_LDR  =  6   # load register
OP_STR  =  7   # store register
OP_RTI  =  8   # unused
OP_NOT  =  9   # bitwise not
OP_LDI  = 10   # load indirect
OP_STI  = 11   # store indirect
OP_JMP  = 12   # jump
OP_RES  = 13   # reserved (unused)
OP_LEA  = 14   # load effective address
OP_TRAP = 15   # execute trap


