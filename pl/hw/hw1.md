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




2 (c, e) 4/4
6 (a, b) 4/4
7 (a) 4/4
1 (a, b, c) 4/4
2 (a, b) 4/4

For transitive, must show why it is divisible (ie x-y=6a, y-z=6b x-z=6(a+b))