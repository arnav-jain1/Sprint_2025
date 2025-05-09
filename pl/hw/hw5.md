0. Straight from class notes
$$
\frac{}{\,\langle v_{1},v_{2}\rangle.1 \;\to\; v_{1}\;}\quad(\mathrm{PairLeft})
$$

$$
\frac{}{\,\langle v_{1},v_{2}\rangle.2 \;\to\; v_{2}\;}\quad(\mathrm{PairRight})
$$

$$
\frac{\,t_{1}\to t_{1}'\,}{\,\langle t_{1},t_{2}\rangle \;\to\;\langle t_{1}',t_{2}\rangle\;}\quad(\mathrm{EPairL})
$$

$$
\frac{\,t_{2}\to t_{2}'\,}{\,\langle v_{1},t_{2}\rangle \;\to\;\langle v_{1},t_{2}'\rangle\;}\quad(\mathrm{EPairR})
$$

$$
\frac{\,t\;\to\;t'\,}{\,t.1\;\to\;t'.1\;}\quad(\mathrm{EProjL})
$$

$$
\frac{\,t\;\to\;t'\,}{\,t.2\;\to\;t'.2\;}\quad(\mathrm{EProjR})
$$

Type rules
$$
\frac{\,\Gamma\vdash t_{1}:T_{1}\quad \Gamma\vdash t_{2}:T_{2}\,}
{\,\Gamma\vdash\langle t_{1},t_{2}\rangle : T_{1}\times T_{2}\;}\quad(\mathrm{TPair})
$$

$$
\frac{\,\Gamma\vdash t : T_{1}\times T_{2}\,}
{\,\Gamma\vdash t.1 : T_{1}\;}\quad(\mathrm{TProj1})
$$
$$
\frac{\,\Gamma\vdash t : T_{1}\times T_{2}\,}
{\,\Gamma\vdash t.2 : T_{2}\;}\quad(\mathrm{TProj2})
$$
1. 

$\{t_1, t_2\}: T_1 \times T_2 \equiv \lambda c. c\ t_{1}\ t_{2}$ 
$\{t_1, t_2\}.1: T_1 \equiv \lambda c. c\ t_{1}\ t_{2} \ true$  
$\{t_1, t_2\}.2: T_1 \equiv \lambda c. c\ t_{1}\ t_{2} \ false$  


2. Proof by induction:
Case 1: Pair
	Also assume that $l$ and $r$ are values corresponding to t1 and t2, .1/.2 is instead True or False respectively in accordance with the inference rules. Then
	PairLeft
		$\{v_{1}, v_{2}\}: T_{1} \times T_{2} .1  \equiv$ 
		$\lambda c. c \ l\ r \ True \ \Rightarrow \text{ True } l \ r \Rightarrow \lambda x.\lambda y. x \ l \ r \Rightarrow l$      
		Since $l \equiv t_{1}$ (stated in assumptions), $l \equiv t_{1}$ so PairLeft holds
	PairRight
		$\{v_{1}, v_{2}\}: T_{1} \times T_{2} .2  \equiv$ 
		$\lambda c. c \ l\ r \ False \ \Rightarrow \text{ False } l \ r \Rightarrow \lambda x.\lambda y. y \ l \ r \Rightarrow r$      
		Since $r \equiv t_{2}$ (stated in assumptions), $r \equiv t_{2}$ so PairRight holds
Case 2: EPair
	Assumptions: $t_{1} \rightarrow t_{1}'$ (given, same for t2) and $l = t_{1}$ and $r = t_{2}$
	EPairL
		$\langle t_{1}, t_{2} \rangle \equiv$
		$\lambda c. c \ l\ r = \lambda c. c \ t_{1} \ r \Rightarrow \lambda c. c \ t_{1}' \ r$  (by inductive hypothesis since we assume the rest is correct) 
		$\equiv \langle t_{1}', t_{2} \rangle$ 
	EPairR
		For this one assume $l = v_{1}$ so l can't be evald further
		$\langle v_{1}, t_{2} \rangle \equiv$
		$\lambda c. c \ l\ r = \lambda c. c \ l \ t_{2} \Rightarrow \lambda c. c \ l \ t_{2}'$  (by inductive hypothesis since we assume the rest is correct) 
		$\equiv \langle v_{1}, t_{2}' \rangle$ 
	This satisfies EPair
Case 3: EProj	
	Assumptions: $t \rightarrow t'$ (given)
	For neatness sake, I will remove typing.  Let $t : T$ 
	EProjL
		$t.1 \equiv$
		$\lambda t. t\ True= \lambda t. t' \ True$  (by inductive hypothesis since we assume the rest is correct) 
		$\equiv t'.1$  
	EProjR
		$t.2 \equiv$
		$\lambda t. t\ False= \lambda t. t' \ False$  (by inductive hypothesis since we assume the rest is correct) 
		$\equiv t'.2$  
	This satisfies EProj
