Instructions are words used to tell the computer what to do
The collection of words is called the "instruction set"

Classes of instructions:
	R-instruction: Registers only, no addresses
		op $reg $reg $reg
	I-instruction (immediate): Uses immediate value
		op $reg $reg val
	I-instruction (branch): Uses a label
		op $reg $reg label
	I-instruction (memory): uses memory
		op $reg value(\$reg)
	J-instruction: uses operator and label only
		op label
opcode: operation
operand: data or memory location to execute that operation
	Order is fixed (non commutative), first one is where its stored

All instructions use registers

Registers:
	Very limited, 32 in MIPS32 (64 in MIPS64)
	![[Pasted image 20250210102016.png]]


Memory:
	Used to store more information than just the registers
	Cannot perform arithmitic in memory (need to use load to get it into registers)
	Large one dim array each with address. Each location stores 1 byte

Most data items used "words" which in MIPS is 4 bytes long 
	All words have to start at a multiple of 4 for alignment

Example `lw $t0, 4($s0)`
	This adds 4 to s0 and then moves 4 bytes to register t0
	So if s0=4000, then the numbers at addresses 4000, 4001, 4002, 4003 are moved.

Big endian: MSB at lowest memory address
Small endian: MSB at highest memory address
Doesn't matter as long as you know what it is 
![[Pasted image 20250210102850.png]]


Example: g = h + A\[8]
	`lw $t0 32($s1)$` add 32 (because 8th index * 4 bytes) to where our array is located. Store that in t0
	`add $t0, $s2, $t0` add t0 to t1 and store at t0
	To store in A\[12]: `sw $t0, 48($s1)` store t0 into 48+base

Depending on the instruction class it is converted to binary differently
![[Pasted image 20250210103813.png]]
	Opcode is part of the instruction (0 for all R type)
	Rs, Rt, and Rd are all registers 
		Rs = first operand
		Rt = second operand
		Rd = destination register
	shamt is shift
	Funct helps specify the instruction

`add $t0 $s1 $s2`
	opcode 000000
	rs 10001
	rt 10010
	rd 01000
	shamt 00000
	funct 100000
	all 0000 0010 0011 0010 0100 0000 0010 0000
	![[Pasted image 20250210104248.png]]
Steps for R-format: **EXAM**
	Set opcode to 0
	Find register number for rs, rt, rd
	Compute shamt (0 for non shift)
	find value of funct
	Convert to binary
	Combine fields

R type doesn't work well for load and store so I type used (2 registers)
`lw $t0 32($s2)`
	opcode = 0d32
	rs = 18
	rt = 8
	offset = 32

# Lec 7

### Signed loads
Some instructions like lbu and lh load one byte or half the reg respectively. THey fill the rest with 0s. The issue is that this does not keep the sign the same.
	Signed versions and unsigned versions (lb and lbu) exist to fix this issue

Small constants are used a lot 
	i = i + 5
Instead of loading the val to a register and then adding the two registers, we can just add immediate  which is faster

Make the common case fast

Logical operations are also very important and exist in mips
![[Pasted image 20250214101351.png]]
	Note that shift left and right are r-type but with one src operand (use the shamt)

Shift left is the same as multiplying by 2 so shift left n = $* 2^{n}$ (unless MSB is lost)
Shift right is the same but div


### Branching
MIPS also has branching such as beq (branch if equal) or bne (branch if not equal)
Example:
	`if (i==j) h = i+j`
	`bne $s0 $s1 LABEL` This will jump to LABEL if they are not equal
	`add $s3 $0 $s1`
	`j EXIT` This is for the else part
	`LABEL: ...`
	`...`
	`EXIT: ...`
	
### Loops

![[Pasted image 20250214102546.png]]
	The first line shifts the i left twice (so mult by 4) and stores in t1. This is for getting how much we will have to jump from base
	Line 2 gets the address of save\[i] 
	Line 3 loads the value at the address
	Line 4 checks to see if they are not equal. If they aren't equal then jump to exit otherwise continue
	Line 5 adds 1 to our i value and then we repeat