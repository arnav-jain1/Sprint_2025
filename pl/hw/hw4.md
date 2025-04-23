Original language:
$$
\begin{align*}
t &::= \lambda x : T . t \mid (t\ t) \mid x \\
v &::= \lambda x : T . t  \\
T &::= T \rightarrow T
\end{align*}

$$

1. New language:

$$
\begin{align*}
t &::= \lambda x : T . t \mid (t\ t) \mid x \ | \text{ True | False | if } t_{1} \ t_{2} \ t_{3} \ | \text { AND } t_{1} \ t_{2}\\
v &::= \lambda x : T . t \ | \text{ True | False}\\
T &::= T \rightarrow T \ | \text{ Bool}
\end{align*}
$$
New rules:
This one just says True and False are of type Bools
$$
\frac{}{\Gamma \vdash \text{True : Bool}} \frac{}{\Gamma \vdash \text{False : Bool}}  \\\\
$$

This is basic typing
$$ \frac{(x \mapsto Bool) \in \Gamma}{\Gamma \vdash x : T}TBool $$


These are for evaluating (IFApp 1, 2, 3)
$$
\frac{t_{1}\rightarrow t_{1}'}{\text{if } t_{1} \text{ then } t_{2} \text{ else } t_{3} \rightarrow \text{if } t_{1}' \ t_{2} \ t_{3}}
\frac{t_{2}\rightarrow t_{2}'}{\text{if } v_{1} \text{ then } t_{2} \text{ else } t_{3} \rightarrow \text{if } v_{1} \ t_{2}' \ t_{3}}
$$

$$
\frac{t_{3}\rightarrow t_{3}'}{\text{if } v_{1} \ v_{2} \ t_{3} \rightarrow \text{if } v_{1} \ v_{2} \ t_{3}'}
$$
The IFtrue and IFfalse are trivial, not going to list them


This one is for actually type checking
$$
\frac{\Gamma \vdash v_{1} : \text{Bool} \quad \Gamma \vdash v_{2} : T \quad \Gamma \vdash v_{3} : T}{ \Gamma \vdash \text{if } v_{1} \ v_{2} \ v_{3} : T} TIf
$$

Not going to write down the eval rules for AND, pretend they exist (very similar) with the name ANDApp 1, 2
Type checking:
$$\frac{\Gamma \vdash v_{1} : Bool \quad \Gamma \vdash v_{2} : Bool}{\Gamma \vdash AND \ v_{1} \ v_{2} : Bool}TBool$$

2. Progress
Case 1:
	if $\Gamma \vdash t : Bool$ then t is a value ELSE IF $\Gamma \vdash t : T$ then t is a value ELSE $t \rightarrow t'$ for some $t'$ 


Case 2:
$$\Gamma \vdash \text{if } t_{1} \ t_{2} \ t_{3} : T$$
	Assume progress for $t_{1}$ and $t_{2}$ and $t_{3}$
	If $t_{1}$ or $t_{2}$ or $t_{3}$ are not values then IFApp 1 2 and 3 will apply (respectively)
	If they are all values  and t1 is a bool and t2 == t3 then TIf applies, otherwise we are in a broken state


Case 3:
$$\Gamma \vdash AND \ t_{1} \ t_{2} : Bool$$
	Assume progress for $t_{1}$ and $t_{2}$
	If $t_{1}$ or $t_{2}$are not values then ANDApp 1 and 2will apply (respectively)
	If they are all values then TBool applies

Preservation 

Permutation
	Case 1: x
		$\Gamma \vdash x : Bool \Rightarrow (x \mapsto Bool) \in \Gamma$ by type inversion. By def permutation, $(x \mapsto Bool) \in \Delta. \Delta \vdash x : Bool$  by TBool 
	Case 2: $\Gamma \vdash \text{if } t_{1} \ t_{2} \ t_{3} : T$
		$\Gamma \vdash \text{if } t_{1} \ t_{2} \ t_{3} : T \Rightarrow (t_{1} \mapsto Bool) \in \Gamma, (t_{2} \mapsto T) \in \Gamma, (t_{3} \mapsto T) \in \Gamma$ by type inversion. Induction hyp says permutation holds and $\Delta \vdash t_{1} : Bool$ and $\Delta \vdash t_{2} : T$ and $\Delta \vdash t_{3} : T$ Thus $\Delta \vdash (\text{if } t_{1} \ t_{2} \ t_{3}) : T$ holds by TIf
	Case 3: $\Gamma \vdash AND \ t_{1} \ t_{2}$	 
		$\Gamma \vdash AND \ t_{1} \ t_{2} : Bool \Rightarrow (t_{1} \mapsto Bool) \in \Gamma, (t_{2} \mapsto Bool) \in \Gamma$ by type inversion. Induc hyp says permutation holds and $\Delta \vdash t_{1} : Bool$ and $\Delta \vdash t_{2} : Bool$  Thus $\Delta \vdash (AND \ t_{1} \ t_{2}) : Bool$  Holds by TAnd

Weakening
	Case 1: x
		$\Gamma \vdash x : Bool \Rightarrow (x \mapsto Bool) \in \Gamma$ by type inversion. With the assumption $x \ne y, (x \mapsto Bool) \in (y \mapsto T), \Gamma$  by def lookup. Thus $(y \mapsto T), \Gamma \vdash x : Bool$ by applying TBool
	Case 2: $\Gamma \vdash \text{if } t_{1} \ t_{2} \ t_{3} : T$
		$\Gamma \vdash \text{if } t_{1} \ t_{2} \ t_{3} : T \Rightarrow (t_{1} \mapsto Bool) \in \Gamma, (t_{2} \mapsto T) \in \Gamma, (t_{3} \mapsto T) \in \Gamma$ by type inversion. Induction hyp says $(y \mapsto S), \Gamma \vdash t_{1} : Bool$, $(y \mapsto S), \Gamma \vdash t_{2} : T$, and $(y \mapsto S), \Gamma \vdash t_{3} : T$ hold thus $(y \mapsto S), \Gamma \vdash (if \ t_{1} \ t_{2} \ t_{3}) : T$ holds by TIf
	Case 3: $\Gamma \vdash AND \ t_{1} \ t_{2}$	 
		$\Gamma \vdash AND \ t_{1} \ t_{2} : Bool \Rightarrow (t_{1} \mapsto Bool) \in \Gamma, (t_{2} \mapsto Bool) \in \Gamma$ by type inversion. Induc hyp says $(y \mapsto S), \Gamma \vdash t_{1} : Bool$ and $(y \mapsto S), \Gamma \vdash t_{2} : Bool$ hold Thus $(y \mapsto S), \Gamma \vdash (AND \ t_{1} \ t_{2}) : Bool$  Holds by TAnd 

Subst
	Case 1: TBool
		$t = z \Rightarrow z : Bool$ 
		$(z \mapsto Bool) \in (x \mapsto S), \Gamma$: Type inverting t: Bool and replacing t with z
		z = x: $[x \mapsto s]x = s$ Vars are unique. Know Bool = S : s : Bool. If you sub s in for x, you get s. s : Bool so preservation holds
		$z \ne x$  $[x \mapsto s]z = z$ 
	Case 2: Tif
		$t = (if \ t_{1} \ t_{2} \ t_{3})$ 
		$(x \mapsto X), \Gamma \vdash t : T$ 
		Type inversion
			$(x \mapsto S), \Gamma \vdash t_{1} : Bool$ 
			$(x \mapsto S), \Gamma \vdash t_{2} : T$ 
			$(x \mapsto S), \Gamma \vdash t_{3} : T$ 
		Induction hyp
			$\Gamma \vdash [x \mapsto s]t_{1} : Bool$ 
			$\Gamma \vdash [x \mapsto s]t_{2} : T$ 
			$\Gamma \vdash [x \mapsto s]t_{3} : T$ 
		By Tif: $\Gamma \vdash [x \mapsto s](if \ t_{1} \ t_{2} \ t_{3}) : T$ so type pres over subst
	Case 3: TBool
		$t = (AND \ t_{1} \ t_{2})$ 
		$(x \mapsto X), \Gamma \vdash t : Bool$ 
		Type inversion
			$(x \mapsto S), \Gamma \vdash t_{1} : Bool$ 
			$(x \mapsto S), \Gamma \vdash t_{2} : Bool$ 
		Induction hyp
			$\Gamma \vdash [x \mapsto s]t_{1} : Bool$ 
			$\Gamma \vdash [x \mapsto s]t_{2} : Bool$ 
		By TBool: $\Gamma \vdash [x \mapsto s](AND \ t_{1} \ t_{2}) : Bool$ so type pres over subst

Proof: 
	Case 1: x
		true and false are vals no t' st t -> t'
	Case 2: $\Gamma \vdash \text{if } t_{1} \ t_{2} \ t_{3} : T$
		Type inversion
			$t_{1} : Bool$ 
			$t_{2} : T$ 
			$t_{3} : T$ 
		5 eval ruls: IFApp 1, 2, 3, and IfTrue/IfFalse
		TypeInf cases:
			$t_{1} : Bool$ (type inv), $t_{1} : T_{1} \rightarrow t_{1}' : Bool$ (ind hyp), $t_{2} : T$, $t_{3} : T (both type inv)$ $\vdash (if \ t_{1}' \ t_{2} \ t_{3}) : T$ 
				Essentially either t1 is bool or it evals to bool in either case if will eval to T
			$v_{1} : Bool$ (type inv), $t_{2} : T \rightarrow t_{2}' : T$ (ind hyp), $t_{2} : T$, $t_{3} : T (both type inv)$ $\vdash (if \ v_{1} \ t_{2}' \ t_{3}) : T$ 
				So in this case t1 is now a value v1 and t2 is either T or it evals to T in either case if will eval to T
			$v_{1} : Bool$ (type inv), $t_{3} : T \rightarrow t_{3}' : T$ (ind hyp), $v_{2} : T$, $t_{3} : T (both type inv)$ $\vdash (if \ v_{1} \ v_{2} \ t_{3}') : T$ 
				Same thing but with t3 instead
			Since we proved subst, subst will hold as well
		Preservation holds
	Case 3: $\Gamma \vdash AND \ t_{1} \ t_{2}$	 
		Type inversion
			$t_{1} : Bool$ 
			$t_{2} : Bool$ 
		4 eval rules (F/F, T/F, T/T, F/T) and 2 to eval both sides
		Type inf cases:
			$t_{1} : Bool$ (type inv), $t_{1} : T_{1} \rightarrow t_{1}' : Bool$ (ind hyp), $t_{2} : Bool$ (type inv) $\vdash (AND \ t_{1}' \ t_{2}) : Bool$
				Essentially either t1 is bool or it evals to bool in either case AND will eval to Bool
			$v_{1} : Bool$ (type inv), $t_{2} : T_{1} \rightarrow t_{2}' : Bool$ (ind hyp), $t_{2} : Bool$ (type inv) $\vdash (AND \ v_{1} \ t_{2}') : Bool$
				Essentially either t2 is bool or it evals to bool in either case AND will eval to Bool
			Since we proved subst, subst will hold as well
		Preservation holds

Done yippee


3. Let
$$
\frac{}{\text{Let } x = v_1 \text{ in } t_2 \rightarrow [x \mapsto v_1] t_2} \; \text{ELetV} \quad \frac{t_1 \rightarrow t_1'}{\text{Let } x = t_1 \text{ in } t_2 \rightarrow \text{Let } x = t_1' \text{ in } t_2} \; \text{ELet}$$
Type rule
$$
\frac{\Gamma \vdash t_1 : T_1 \quad (x \mapsto T_1), \Gamma \vdash t_2 : T_2}{\Gamma \vdash \text{Let } x = t_1 \text{ in } t_2 : T_2} \; \text{TLet}$$
4. Proof
Progress: $\Gamma \vdash \text{Let } x = t_1 \text{ in } t_2 : T_2$
	Assume progress for t1 and t2
	t1 not a val then ELet applies
	t1 a val then ELetV applies


Preservation

Permutation
	$\Gamma \vdash \text{Let } x = t_1 \text{ in } t_2 : T_2$
		$\Gamma \vdash \text{Let } x = t_1 \text{ in } t_2 : T_{2} \Rightarrow (t_{1} \mapsto T_{1}) \in \Gamma, (t_{2} \mapsto T_{2}) \in \Gamma$  by type inv and. Induc hyp says permutation holds and $\Delta \vdash t_{1} : T_{1}$  and $\Delta \vdash t_{2} : T_{2}$ Thus $\Delta \vdash (Let \ x \ t_{1} \ in \ t_{2}) : T_{2}$  Holds by TLet	

Weakening
	$\Gamma \vdash \text{Let } x = t_1 \text{ in } t_2 : T_2$
		$\Gamma \vdash \text{Let } x = t_1 \text{ in } t_2 : T_{2} \Rightarrow (t_{1} \mapsto T_{1}) \in \Gamma, (t_{2} \mapsto T_{2}) \in \Gamma$  by type inv and. Induc hyp says $(y \mapsto S), \Gamma \vdash t_{1} : T_{1}$  and $(y \mapsto S), \Gamma \vdash t_{2} : T_{2}$ Thus $(y \mapsto S),\Gamma \vdash (Let \ x \ t_{1} \ in \ t_{2}) : T_{2}$  Holds by TLet	 

Subst
	$t = (Let \ x \ = \ t_{1} \ in \ t_{2}) : T_{2}$  
	Type inversion
		$(x \mapsto S), \Gamma \vdash t_{1} : T_{1}$ 
		$(x \mapsto S), \Gamma \vdash t_{2} : T_{2}$ 
	Induction hyp
		$\Gamma \vdash [x \mapsto s]t_{1} : T_{1}$ 
		$\Gamma \vdash [x \mapsto s]t_{2} : T_{2}$ 
	By TLet: $\Gamma \vdash [x \mapsto s]t : T_{2}$ so type pres over subst

Final
	$t = (Let \ x \ = \ t_{1} \ in \ t_{2}) : T_{2}$  
	Type inversion
		$t_{1} : T_{1}$ 
		$t_{2} : T_{2}$ 
	Type inf cases are all covered:
		If t1 is not a value then we eval (induc hyp applied here)
		Then once it is a value, we subst in t2 and this does not change the output as per previous lemma

GG