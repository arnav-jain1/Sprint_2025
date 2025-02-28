1.  
	or $\lambda x . \lambda y . x \ x \ y$ 
	not $\lambda x . \lambda y . \lambda z . x \ z \ y$ 
2. 
	$\lambda m . \lambda n . \lambda s . \lambda z . m ( n \ s) z$ 
3. 
	$\lambda b . \lambda e . \lambda S . \lambda Z . (e \ b) \ S \ Z$  
4. 
	$\lambda x . \lambda y . \text{and} (\le x \ y) \ (\le y \ x)$ 
5. 
	NIL: $\lambda x . x$
	List with 1 elem: $\lambda c . \lambda x \ c \ a \ x$ 
	List with 2 elem: $\lambda c . c \ a_{1} \lambda c . \lambda x \ c \ a_{0} \ x$  
	Cons (prepend):	$\lambda a . \lambda l . \lambda c \ c \ a \ l$ 
		Takes a value, *a* and a list then returns c a list
	Head: $\lambda l . l \ \text{true}$ 
	isnil: $\lambda l.l \ \text{true false}$ 
		So what this does is take in a list first and applies true to it, this return true if the first element is just nil. If it is not, then it will substitute false into whatever the first element is and return false
	
	
	
	