# Lec 3 Floating Point and Unicode
![[Pasted image 20250129104356.png]]
S: sign bit
Exponent is biased, theres a default value thats subtracted
	Single bias = 127
	Double bias = 1023
Fraction is like the scientific form
<mark style="background: #FF5582A6;">The significand is normalized, dont need to represent directly</mark>
SO the way that significand works is that its $1+2^{-n}$ wherever n is set to 1 so if the fraction is 
1010000 then its $1+2^{-1}+2^{-3}$ 

## Single precision 
Exponents 0000 0000 and 1111 1111 are reserved
Smallest value:
	Exponent = 0000 0001, fraction is all 0s so $\pm1.0 * 2^{-126}$ 
Largest value:
	Exponent = 1111 1110 = 254-127 = 127
	Fraction = all 1s so significand is pretty much 2
	$\pm 2 * 2^{127}$

Converting -.75:
	So first the sign bit is 1 because it is negative
	Then we know that .75 = .5 + .25 so the binary is .11
	We need to normalize it so it becomes $1.1 * 2^{-1}$ 
	So then the fraction is just 1000... and the exponent is needs to be -1 so then x - Bias = -1, x - 127 = -1, x = 126
	126 = 0111 1110
	So the final number is 1 0111 1110 1000...
