# Lec 2, 2s complement and overflow

Words in MIPS are 32 bits long
Right most bit is the LSB (because it only changes by 1)
Left most bit is the MSB (because it has a larger impact on the number)

You can represent $2^{32}-1$ as the max number (because of 0)


## Attempts to represent negatives 

**Let the first digit represent sign**
Let the left most bit determine the sign
Pros: Equal number of positive and negative
Cons: 2 0s, +0 and -0 (1000 and 0000), hard to do arithmitic 

**2s complement**: The MSB is just negative and the rest is positive so if the first bit is 1 then the number is negative, otherwise it is positive
Note that the amount of positive and negative numbers is uneven (-2^n-1 does not have a counterpart)
Range: \[$-2^{n-1}, 2^{n-1}-1$] 

When converting from 2s to decimal, the MSB is negative the rest is like normal

To negate a number, flip all bits then add 1 (or aniketh's trick, flip all bits until the last 1)
	4bit example:
		-1: 1111
		1: 0001
	Note this does not work for the lowest num ($-2^{n-1}$) 

Addition with 2s complement is normal, subtraction is addition with negation


## Overflow
WHen a number cant be represented by a fixed number of bits, overflow when result is wrong (not when losing the carryout bit)
	Occurs when result has the opposite sign of what you would expect 
	Occurances:
		+ **-** (-) = -
		- - + = +
		+ + + = -

For a 4bit register, it has the range \[-8, 7] so
	7 + 1 = 0111 + 0001 = 1000 = -8, overflow 
	![[Pasted image 20250129103512.png]]
	-7 - (2) = 1001 + 1110 = 0111 = 7 so overflow (+ve)

![[Pasted image 20250129103639.png]]
Overflow can be recognized pretty easily 


## Math
![[Pasted image 20250129103843.png]]
Half adder doesn't have a carry in to add the carry from the previous output


![[Pasted image 20250129103919.png]]
Full adder adds 3 bits: A, B, and the carry-in bit C
Formed by connecting 2 half adders 


Ripple carry adder is the cascading of multiple full adders to add an N-bit number
	There needs to be N consecutive full adders for N bits
	The carryout of one full adder is the carry in of the next
![[Pasted image 20250129104222.png]]
This is very slow which is why it is not used


