what does `int x` tell us
	It tells us where x can be used
`f: nat -> nat`:
	It tells us f is a function that maps a natural to a natural which helps us w the 
`A: Type`
	A is a variable that stores a type

Syntax are the stuff in the language
types are a subset that are terms

$T ::= \ Bool \ | \ Nat$ 

Making typing relations:

$\frac{}{0 : Nat}$ 
$\frac{}{true \ : Bool}$ 
$\frac{}{false \ : Bool}$ 

ALL VALS HAVE 1 TYPE

for succ 
$\frac{t \ : \ Nat}{\text{succ } t \ : Nat}$ 

The issue is we don't know the type of if