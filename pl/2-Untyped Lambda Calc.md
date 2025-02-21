Lambda calculus: everything is a name or a function 
	Logic of pure functions
	Opposite of turing machines 

Turing machine is pure state, no functions
Lambda calculus is pure functions, no state
	What does this mean? Functions are data and data transformations. There is nothing else

Concept of lambda comes from lambda calc

3 things in lambda calculus: 
	variable:                            *x* 
	abstraction (or lambda): $\lambda x, t$ 
	Application (app):            (t t)

so 
t ::= $\lambda x, t \space | \space (t,t) \space | \space x$  

Lambda is called an abstraction (since the variables are variable), param defined in scope

Application applies the abstraction <mark style="background: #FF5582A6;">(Also called instantiation??)</mark>

$\lambda x . t$ 
	x is the var, t is the term and the scope of x
	x may be in t
$\lambda x. x\space x$
	x is the var/param and it is applied to itself
$\lambda x . \lambda y . z$
	A function with 2 parameters (currying)
$\lambda x . \lambda y . z \space x$
	I forgot
$(\lambda x. x \space x)(\lambda x . x \space x)$
	Omega comb, doesnt terminate keeps generating the same thing 


1. Binding instance: where var declared
2. Bound instance: Where var used in scope
3. Free instance: Where var used out of scope

$\lambda x . \lambda y . x \space z$ x is bound and binding, z is free

A combinator is a lambda with no free vars
A redux is a combinator that can be reduced 


## Beta reduction
### Syntax
t ::= $\lambda x, t \space | \space (t,t) \space | \space x$  
v ::= $\lambda . t$ 


### Eval
$$\frac{}{((\lambda x, t_{12}) t_{2}) \rightarrow [x \rightarrow t_{2}]t_{12}}$$
Replace all x with $t_{2}$ in $t_{12}$ 
The lambda gets eliminated 


**Example:** $(\lambda w . w \space \lambda x . x)((\lambda y.y)(\lambda z.z))$  
	$\Rightarrow (\lambda x . x)((\lambda y.y)(\lambda z.z))$ 
	$\Rightarrow (\lambda x . x)(\lambda z.z)$ 
	$\Rightarrow \lambda z.z$ 


Note that this is nondeterministic because we don't really have parenthesis yet 

This is call called pure beta reduction when theres no values


$$\frac{t_{1} \rightarrow t_{1}'}{t_{1} \space t_{2} \rightarrow t_{1}' \space t_{2}} \frac{t_{2} \rightarrow t_{2}'}{v_{1} \space t_{2} \rightarrow v_{1} \space t_{2}'} \text{LambdaT1 and LambdaT2}$$
$$\frac{}{((\lambda x, t_{12}) v_{2}) \rightarrow [x \rightarrow v_{2}]t_{12}}$$ This is call by value because v2 is already a value ( it got evaluated by the rule before it)

For call by name, remove LambdaT2 and change v2 to t2

$((\lambda x, (\lambda y.x \space y))(\lambda z.z\space z))(\lambda w.w)$ 
$\Rightarrow (\lambda y .(\lambda z.z\space z) y)(\lambda w.w)$ 
$\Rightarrow (\lambda z.z\space z)(\lambda w.w)$ 
$\Rightarrow (\lambda w.w) (\lambda w.w)$ 
$\Rightarrow (\lambda w.w)$
This is currying woo!


The **o m e g a c o m b i n a t o r**
$(\lambda x.x \space x)(\lambda x.x \space x)$ 
$\Rightarrow [x \rightarrow (\lambda x.x \space x)](x \ x)$    

### Church Booleans
true = $\lambda x . \lambda y. x$ 
false = $\lambda x. \lambda y . y$ 
	
and = $\lambda x . \lambda y . x \ y \ x$ 
or $\lambda x . \lambda y . x \ x \ y$ 
not $\lambda x . x \ \text{false} \ \text{true}$ 


And true true = 
	$(((\lambda x . \lambda y . x \ y \ x) \lambda x . \lambda y. x) \lambda x . \lambda y. x)$  
	$\Rightarrow ( \lambda y . (\lambda x . \lambda y. x) \ y \ (\lambda x . \lambda y. x)) \lambda x . \lambda y. x$  
	$\Rightarrow (\lambda x . \lambda y. x) \ \lambda x . \lambda y. x \ (\lambda x . \lambda y. x)$     
	$\Rightarrow (\lambda y. \lambda x . \lambda y. x) (\lambda x . \lambda y. x)$     
	$\Rightarrow (\lambda x . \lambda y. x) (\lambda x . \lambda y. x)$     Because no y
	$\Rightarrow  \lambda y. \lambda x . \lambda y. x$     
	$\Rightarrow \lambda x . \lambda y. x$     Because no y
	$\Rightarrow true$ 


And true false = 
	$(((\lambda x . \lambda y . x \ y \ x) \lambda x . \lambda y. x) \lambda x . \lambda y. y)$  
	$\Rightarrow ( \lambda y . (\lambda x . \lambda y. x) \ y \ (\lambda x . \lambda y. x)) \lambda x . \lambda y. y$  
	$\Rightarrow (\lambda x . \lambda y. x) \ \lambda x . \lambda y. x \ (\lambda x . \lambda y. y)$     
	$\Rightarrow (\lambda y. \lambda x . \lambda y. x) (\lambda x . \lambda y. y)$     
	$\Rightarrow (\lambda x . \lambda y. x) (\lambda x . \lambda y. y)$     Because no y
	$\Rightarrow  \lambda y. \lambda x . \lambda y. y$     
	$\Rightarrow \lambda x . \lambda y. y$     Because no y
	$\Rightarrow false$ 

Not false =
	$\lambda x . x \ \text{false } \text{true }  \text{false}$   
	$(\lambda x . x \ \text{false true }) \ (\lambda x. \lambda y . y)$      
	$(\lambda x. \lambda y . y) \ (\text{false true})$ 
	$(\lambda y . y \ \text{true})$ 
	true

not (and a b) = or (not a) (not b)
	Since we are doing this over arbitrary values (vars), put lambdas in front
	$\lambda x . \lambda b . \text{not (and a b)} = \lambda a. \lambda b . \text{or (not a) (not b)}$
	Simplifying the left side
		$\lambda x.x \ \text{false true } ((\lambda x . \lambda y . x \ y \ x) \ a \ b)$    
		$\lambda x.x \ \text{false true } (a \ b \ a)$     
		$\text{a b a false true}$ 
	Right side
		$(\lambda x . \lambda y . x \ x \ y) \text{(not a) (not b)}$ 
		$\text{(not a) (not a) (not b)}$ 
		

cons: $\lambda l . \lambda r . \lambda c. c \ l \ r$ 
	l and r is a pair and c is a boolean that gives you one of them

((cons v1) v2) =
	$(((\lambda l . \lambda r . \lambda c. c \ l \ r) v_{1}) v_{2})$ 
	$\lambda c. c \ v_{1} \ v_{2}$ 
To get the left we put true there
To get right we put false


## Church numbers
Canonical encoding of natural numbers in lambda calculus 
Definition of *nv* from previous language is actually close
	0, S(0), S(S(0)), ... S() = succ
But note THESE ARE VALUES, you DONT EVAL FURTHER
	Its because of numbers vs numerals
	Numbers are the actual numbers
	numerals are ways of representing numbers (ie roman numerals) 
	Numerals represent numbers so S(S(0)) is a numeral representing 2

In Rocq
```
Inductive nat :=
	| 0 : nat
	| S : nat -> nat
```

In lambda calc
$0 = \lambda f . \lambda x . x$
$1 = \lambda f . \lambda x . f \ x$
$2 = \lambda f . \lambda x . f \ (f \ x)$ 
And this thing is a value!!!!!!!!

Adding 3 + 2:
	$2 = \lambda f . \lambda x . f \ (f \ x)$ = S(S(0)) 
	$3 = \lambda f . \lambda x . f (f \ (f \ x))$  = S(S(S(0)))
	2+3 would be S(S(S(2)))

Plus: $\lambda m . \lambda n . \lambda F . \lambda Z . (m \ F (n \ F) \ Z)$  
	$(\lambda f . \lambda x . f (f \ (f \ x)))(\lambda f . \lambda x . f \ (f \ x))$ 


