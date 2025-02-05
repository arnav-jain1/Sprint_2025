# Multiplication
Multiplication is like normal 
![[Pasted image 20250203115128.png]]
Another way to do it, would be this:
	![[Pasted image 20250203115230.png]]
	Go through each multiplier if it is 0, shift the multiplicand left 1 bit (so that it becomes larger) and the multiplier right 1 bit (so that we go to the next bit). If it is 1, then add the multiplicand to the produce (in the product register) and then do the same thing 32 times


The thing is this is NOT effecient 
	We can do the left and right shift in parallel to make it faster


Amdahl's law:
	Performance increase is limited by the fraction of time that it is actually used
	Exec time = $\frac{\text{exec time affected by improvement}}{\text{Amount of improvement}} + \text{Exec time unaffected}$ 
		If we have a program that runs in 100 seconds on a computer, and 80 seconds  are related to multiplication, how much do we need to improve multiplication  instructions to run the program 5 times faster?
			100/5 = 80/n + 20
			20=80/n + 20
			0 = 80/n therefore not possible
	Make the slowest case faster

Space effecient mult
![[Pasted image 20250205101710.png]]
	What we can do is combine the partial product with the multiplier (32 bits each) so this will make it only 2 registers and shifts are easier

To go even faster, we can do multiple multiplications in parallel 
