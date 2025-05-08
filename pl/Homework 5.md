# Question 0

## Type Rules

$$
\frac{\Gamma \vdash t_1:T_1 \quad \Gamma \vdash t_1:T_2}
{\Gamma \vdash \{t_1, t_2\}:T_2 \times T_2} \quad \text{T-Pair}
$$

$$
\frac{\Gamma \vdash t:T_1 \times T_2}
{\Gamma \vdash t.1:T_1} \quad \text{T-Proj1}
$$

$$
\frac{\Gamma \vdash t:T_1 \times T_2}
{\Gamma \vdash t.2:T_2} \quad \text{T-Proj2}
$$

## Inference Rules

$$
\frac{}{\{v_1, v_2\}.1 \to v_1} \quad \text{E-Pair1Value}
$$

$$
\frac{}{\{v_1, v_2\}.2 \to v_2} \quad \text{E-Pair2Value}
$$

> [!note]
> These rules specify if the items in a pair are values, we can just extract them to evaluate to get the first and second values of the pair.

$$
\frac{t \to t'}{t.1 \to t'.1} \quad \text{E-Proj1}
$$

$$
\frac{t \to t'}{t.2 \to t'.2} \quad \text{E-Proj2}
$$

> [!note]
> These rules specify that in order to get the values contained within pairs you must first evaluate the pair.

$$
\frac{t_1 \to t_1'}{\{t_1, t_2\} \to \{t_1', t_2\}} \quad \text{E-Pair1}
$$

$$
\frac{t_2 \to t_2'}{\{v_1, t_2\} \to \{v_1, t_2'\}} \quad \text{E-Pair2}
$$

> [!note]
> These rules specify that pairs must evaluate the first term before the second term.

# Problem 1

## Derived Forms

$\{t_1, t_2\}: T_1 \times T_2 \equiv (\lambda c: Bool. c\ (t_1: T_1)\ (t_2: T_2)): T_1 \times T_2$

$\{t_1, t_2\}.1: T_1 \equiv ((\lambda c: Bool. c\ (t_1: T_1)\ (t_2: T_2))\ (\lambda x: T_1.\lambda y: T_2. x): Bool): T_1$

$\{t_1, t_2\}.2: T_2 \equiv ((\lambda c: Bool. c\ (t_1: T_1)\ (t_2: T_2))\ (\lambda x: T_1.\lambda y: T_2. y): Bool): T_2$

## Typing Extensions

$T ::=\ ...\ |\ T \times T\ |\ Bool$

# Problem 2

We prove this by induction and cases.

Proof.

**Case 1**: `E-Pair1Value`

> In this case we assume $t_1$ and $t_2$ are values $v_1$ and $v_2$. If they are both values we can then evaluate the derived form of $\{t_1, t_2\}$ to get the following:
>
> $$
> \begin{align}
> \{v_1, v_2\}.1: T_1 \equiv & (\lambda c: Bool. c\ v_1\ v_2) (\lambda x: T_2.\lambda y: T_2. x): Bool): T_1 \\
> & ((\lambda x: T_1.\lambda y: T_2. x): Bool\ v_1\ v_2): T_1 \\
> & ((\lambda y: T_2. v_1): Bool\ v_2): T_1 \\
> & v_1: T_1 \\
> \end{align}
> $$
>
> Thus by looking at the inference rules and type rules we can see that the result of the derived form is equivalent to the expected result v_1 of type T_1.

**Case 2**: `E-Pair2Value`

> In this case we assume $t_1$ and $t_2$ are values $v_1$ and $v_2$. If they are both values we can then evaluate the derived form of $\{t_1, t_2\}$ to get the following:
>
> $$
> \begin{align}
> \{v_1, v_2\}.2: T_1 \equiv & (\lambda c: Bool. c\ v_1\ v_2) (\lambda x: T_2.\lambda y: T_2. y): Bool): T_2 \\
> & ((\lambda x: T_1.\lambda y: T_2. y): Bool\ v_1\ v_2): T_2 \\
> & ((\lambda y: T_2. y): Bool\ v_2): T_2 \\
> & v_2: T_2 \\
> \end{align}
> $$
>
> Thus by looking at the inference rules and type rules we can see that the result of the derived form is equivalent to the expected result, v_2 of type T_2.

**Case 3**: `E-Pair1`

> If we assume that $t_1 \to t_1'$, we can show that:
> 
> $$
> \begin{align}
> \{t_1, t_2\}: T_1 \times T_2 & \equiv (\lambda c: Bool. c\ (t_1: T_1)\ (t_2: T_2)): T_1 \times T_2 \\ 
> & \implies \\
> \{t_1', t_2\}: T_1 \times T_2 & \equiv (\lambda c: Bool. c\ (t_1': T_1)\ (t_2: T_2)): T_1 \times T_2 \\ 
> \end{align}
> $$
> 
> So the inference rule for evaluation of left before right holds true by induction and properties of equivalences.

**Case 4**: `E-Pair2`

> If we assume that $t_2 \to t_2'$ and $t_1$ is a value $v_1$, we can show that:
> 
> $$
> \begin{align}
> \{v_1, t_2\}: T_1 \times T_2 & \equiv (\lambda c: Bool. c\ (t_1: T_1)\ (t_2: T_2)): T_1 \times T_2 \\ 
> & \implies \\
> \{v_1, t_2'\}: T_1 \times T_2 & \equiv (\lambda c: Bool. c\ (t_1': T_1)\ (t_2: T_2)): T_1 \times T_2 \\ 
> \end{align}
> $$
> 
> So the inference rule for evaluation of right after left holds true by induction and properties of equivalences.

**Case 5**: `E-Proj1`

> Assuming $t \to t'$ then:
> 
> $$
> \begin{align}
> t.1 & \equiv ((t: T_1 \times T_2)\ (\lambda x: T_1. \lambda y: T_2. x): Bool) \\
> & \implies \\
> t'.1 & \equiv ((t': T_1 \times T_2)\ (\lambda x: T_1. \lambda y: T_2. x): Bool) \\
> \end{align}
> $$
>
> By induction and equivalences this must be true and we must evaluate the term t before we extract the first value.

**Case 6**: `E-Proj:`

> Assuming $t \to t'$ then:
> 
> $$
> \begin{align}
> t.2 & \equiv ((t: T_1 \times T_2)\ (\lambda x: T_1. \lambda y: T_2. x): Bool) \\
> & \implies \\
> t'.2 & \equiv ((t': T_1 \times T_2)\ (\lambda x: T_1. \lambda y: T_2. x): Bool) \\
> \end{align}
> $$
>
> By induction and equivalences this must be true and we must evaluate the term t before we extract the second value.

For the type rules, cases 1-6 show that the equivalently typed lambda calculus produces the same typing results as the rules. Specifically cases 1 and 2 show the `T-Proj1` and `T-Proj2` results, the equivalences and subsequent cases show how `T-Pair` is upheld within lambda calculus.