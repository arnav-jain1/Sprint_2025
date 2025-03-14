1. $$\lambda f. (\lambda x. f \ (x \ x)) (\lambda x. f \ (x \ x)) \ (\lambda f. \lambda x. \text{if (isnil x) then 0 else (head x) + (f tail x)}  )$$
2. Prove |FV(t)| $\le$ size(t)
	Note: all of the proofs will assume $\forall t, \ size(t) \ge 1$ which is obvious
	Case 1: t = value ie $t \in \{true, false, 0\}$  
		$|FV(t)| = 1$ and $size(t) = 1$ therefore holds
	Case 2: isZero(t), succ(t), pred(t)
		$\frac{t \in Nat}{\text{isZero : Nat ; succ(t) : Nat ; pred(t) : Nat}}$ so then $|FV(isZero(t))|\ =\ |FV(Nat)| = 1$, same proof applies to succ and pred so we statement holds
	Case 3: $\text{if} \ t_{1}\ t_{2}\ t_{3}$  
		Let $t_{1} \rightarrow^{*} t_{1}'$  and $t_{2} \rightarrow^{*} t_{2}'$, by definition of if, the if statement must evaluate to one of those 2. By the induction hypothesis $|FV(t_{1}')| = 1$ and $|FV(t_{2}')| = 1$  so $|FV(\text{if} \ t_{1}\ t_{2}\ t_{3})| = 1 \le size(\text{if} \ t_{1}\ t_{2}\ t_{3})$ 
	Thus the statement holds	
	Another proof would be all terms evaluate to 1 value therefore $\forall t, |FV(t)|=1$  so the statement must be true (proof by logic)

I just found out that this should be for lambda calc so finish this later
Prove |FV(t)| $\le$ size(t)
	Case 1: t = x. This case is obvious, the |FV(t)| = 1 = size(t)
	Case 2: $t=\lambda x. t_{1}$. |FV(t)| = 1 = size(t) since functions are values
	Case 3: $t = (t_{1} \ t_{2})$  $|FV(t)| = |FV(t_{1}) \cup FV(t_{2})| \le |FV(t_{1})| + |FV(t_{2})|$  which by induction hypothesis $\le size(t_{1}) + size(t_{2}) = size(t)$ 
	So for all cases, the statement holds
3. 
	Lazy eval: Delete the first/second and replace the 3rd with the following: $(\lambda x. t_{1}) t_{2} \rightarrow [x \rightarrow t_{2}]t_{1}$ 
	Beta reduction: replace the first two terms with: $\frac{t_{1} \rightarrow v_{1} \quad t_{2} \rightarrow v_{2}}{\lambda t_{1} t_{2} \rightarrow v_{1} v_{2}}$   
4. 
	$$\frac{t_{1} \rightarrow wrong}{t_{1} \ t_{2} \rightarrow wrong} \quad \frac{t_{2} \rightarrow wrong}{ t_{1} \ t_{2} \quad \rightarrow wrong} (\lambda. t_{12})wrong \rightarrow wrong$$ 
	