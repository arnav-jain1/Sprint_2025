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

Convert 11000000101000...00 (SPF)
	So sign bit is 1 so this is negative
	Then 10000001 is the exponent component which is 129 
	01000...00 is the fraction which is .25
	$-1 *  (1+.25) * 10^{129-127} = -1 * 1.25 * 10^{2}= -5.0$ 


ASCII is the standard for info interchange where each char is 1 byte
	Strings are sequences of ascii with the end being a null

Unicode uses code points (same thing pretty much)
	Each letter maps to a number but that depends on the encoding
	Need to know the encoding to decode the message
	UTF8 uses 1-4 bytes per code point
	UTF16 uses 1-2 16bit codes per code point
	UTF 32 uses exactly 4 bytes 


Decoding 0xC3A9
	This is 2 bytes so we use 2 bytes
	Convert it to binary: 11000011 10101001
	Then 2 byte uses the pattern 110xxxxx 10xxxxxx
	So then it bcomes 00011 101001 = 00011101001= 223 = E9
		E9 is **é** so that is the char



Convert 85.125 to FP single precision 4 byte
	85.125 = 1010101.001 then we shift this so it becomes 1.010101001 * 2^6
	When we put it in the fraction component we will omit the leading 1
	So we want the exponent to be 6 so x-127=6, x=133=10000101
	So the full is 0 10000101 0101010010...0
	= 0x42A90000

