Progress and preservation
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



