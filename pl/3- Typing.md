Type safety = Progress and preservation
	Progress means we can continue to eval or its a value 
		Aka can always go forward
	Preservation means the type itself won't change
		When you go forward the type doesn't change

Canonical forms: If you are given a type, all the values in the type are known

Well typed term: Value or can be evaluated aka it isn't stuck
	Also means that a term *t* has a type
	*t* is either a value or $t \ \rightarrow t'$

We are doing a kind of induction but it is over the inference rules


### Proof of progress
For all the terms, need to prove this holds
	$t:T \Rightarrow t \in v \text{ OR } t \rightarrow t'$ 

So for:
	0: Nat
	true: Bool
	false: Bool
These are base cases and they are all values so they follow the rule

Now for 
$$\frac{t:Nat}{\text{succ } t: Nat}$$
	In this case, we need to use induction. 
	t:Nat is the inductive hypothesis, we assume this to be true
	so we have that t is a value so $t \in nv$
	Since $t \in nv$ then $\text{succ(nv)} \in nv$   by definition of nv
	Now if t is not a value, then $t \rightarrow t'$, then succ t -> succ t'
This also applies for pred, and isZero

WTS: `if (t1 t2 t3)` is a value or evaluates 
	If t1 is a value, then t1 is either true or false (by canonical form)
		If true then it evaluates to t2
		If false then it evaluates to t3
	If t1 is not a value, then we have a rule saying that t1->t1' ???


Reduxes are terms that can be reduced, needs to have a value (think of it like a function)
Values need to have a type as well

We can create a type $\rightarrow$  for functions
	$\lambda x. t : \rightarrow$ 

Example: $(\lambda x. x : \rightarrow) (\lambda x.x : \rightarrow)$ 
This is cool and all but doesn't really give us anything (right now)

Example: int x = x + 1
Inc :: Nat -> Nat
	The first one is the domain and the second is the range
	The full thing is a function
Note that this is right assoc so 
	Nat -> Nat -> Nat
		The domain is Nat the range is T->T

New rule time!
$$\frac{}{\lambda x.\ x\ :\ T \rightarrow T}$$


## Base types
 new type with the only Type def:
 $T ::= T \rightarrow T$ 
 This takes an argument thats a type so it becomes
 Bool -> Bool

So now $\lambda x : Bool$ will become $x : Bool \rightarrow Bool$ 
	We can then record the type itself

Function application will remove information because the var (abstraction) is now gone

Examples
	$\lambda x:Bool. \lambda y:Nat. x$: $T_{1} \rightarrow T_{2} \rightarrow T_{1}$  so Bool -> Nat -> Bool
	$(\lambda x . x \ x)(\lambda y. y \ y)$  
	$\lambda x. x$
