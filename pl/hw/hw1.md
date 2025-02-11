13)
	1) 3.5.12, 3.5.8, 3.5.7
	2) 3.5.12 stays valid with no proof changes, 3.5.7/8 stay valid with no proof changes because they are about reducing something that can't be reduced. 3.5.11 depends on the language itself. The theorem will stay valid if the language is stateless but will have to change the proof. If the language has state then it is no longer valid. The other one is invalid
14)
	Does not apply for E-PredSucc, E-PredZero, E-IsZeroZero, E-IsZeroSucc since they use values
	E-Succ:
		If $t_{1} \rightarrow nv$ only one rule applies
	E-Pred:
		If $t_{1} \rightarrow 0$ only one rule applies
		If $t_{1} \rightarrow nv$ only one rule applies
	E-IsZero:
		If $t_{1} \rightarrow 0$ only one rule applies
		If $t_{1} \rightarrow nv$ only one rule applies
	Therefore by induction hypothesis, $\text{if } t_{1} \rightarrow t_{1}' \text{ and } t_{1} \rightarrow t_{1}''$ then $t_{1}' == t_{1}''$
	 
16)
	Intuition: The two statements agree because lets say that you have a statement `if nat t1 t2`, this would stall because there is no rule to apply to simplify this down so it would cause the language to malfunction. Likewise, `if badbool t1 t2` evaluates to wrong which gives the user the same info as the language stalling. So in essence, both ways of handling incorrect behavior tell the user the same information so they "agree"
	Proof:
	$$\frac{\text{if Nat} \space t_{1}\space t_{2} \rightarrow \text{if Nat} \space t_{1}\space t_{2}}{\text{if badbool} \space t_{1}\space t_{2} \rightarrow \text{wrong}}$$
	Likewise
	$$\frac{\text{if badbool} \space t_{1}\space t_{2} \rightarrow \text{wrong}}{\text{if Nat} \space t_{1}\space t_{2} \rightarrow \text{if Nat} \space t_{1}\space t_{2}}$$
	Therefore, the two statements are in agreement

17)
	WTS: $t \rightarrow^{*} v \iff t \Downarrow v$ 
	Let this not be true, instead let $t_{0} \rightarrow^{*} \text{false} \space and \space t_{0} \Downarrow \text{true}$. Then if we use small step, $\text{if } t_{1} \space t_{2} \space t_{3} \rightarrow^{*} \text{if } false \space t_{2} \space t_{3} \rightarrow^{*} t_{3}$ and $\text{if } t_{1} \space t_{2} \space t_{3} \Downarrow \text{if true} \space t_{2} \space t_{3} \Downarrow t_{2}$ so $\text{if } t_{1} \space t_{2} \space t_{3} \Downarrow t_{2} \ne \text{if } t_{1} \space t_{2} \space t_{3} \rightarrow^{*} t_{3}$ which is a contradiction because the same term must evaluate to the same thing therefore the original condition must be true 
18)
	There are a couple changes that need to be made. The original if else rule needs to be deleted (EIf) and this rule needs to be added
	$$\frac{t_{2} \rightarrow t_{2}' \quad t_{1} \rightarrow t_{1}' \quad t_{0} \rightarrow t_{0}'}{\text{if } t_{0} \space t_{1} \space t_{2} \rightarrow\text{if } t_{0}' \space t_{1}' \space t_{2}' }\text{IfNew}$$
	If inference rules are evaluated in order, if not
	$$\frac{t_{2} \rightarrow v_{2}}{\text{if } t_{0} \space t_{1} \space t_{2} \rightarrow\text{if } t_{0} \space t_{1} \space v_{2}} \frac{t_{1} \rightarrow v_{1}}{\text{if } t_{0} \space t_{1} \space v_{2} \rightarrow \text{if } t_{0} \space v_{1} \space v_{2} } \frac{t_{0} \rightarrow v_{0}}{\text{if } t_{0} \space v_{1} \space v_{2} \rightarrow \text{if } v_{0} \space v_{1} \space v_{2} }$$


