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
	
	