# Sets
These are all different ways of writing the same set starting with the most simple grammar

## Grammar
$$ \text{t = true | false | (if t t t) | 0 | succ t | pred t | isZero t}$$
These are the possible value of t 

Inductive defn:
$$\text{\{true, false, 0\}} \subseteq T$$
true, false and 0 are all in T
$$\forall t : T \text{\{succ t, pred t, isZero t\}} \subseteq T$$
succ t, pred t, and isZero t are all in T if t is in T
$$\forall t_{0}, t_{1}, t_{2} : T \{\text{if} \space t_{0} t_{1} t_{2}\} \in T$$
(if t0, t1, t2) is in T if t0, t1, t2 are all in T


## Inference rules
Recall: Numerator is the if part (antecedent), if numerator is true then the denom (consequence) is true
	If there is no numerator, then the consequence must be true and it is axiom (something we just have to accept)


$$\frac{}{\text{true} \in T \text{ false} \in T \text{ 0} \in T}$$
Here, true/false/0 being in T is an axiom, something we just have to accept

$$\frac{t \in T}{\text{succ t} \in T} \frac{t \in T}{\text{pred t} \in T} \frac{t \in T}{\text{isZero t} \in T}$$
if t is in T, then succ/pred/isZero is in T

This is inductive because since succ t is in the set, then succ succ succ ...  succ t is in the set

Notice how this depends on this terminating so you have to prove that the search does/doesn't terminate instead of just running it (halting problem, can't do)


If the set is finite then yay we are good but that means it's weak

## Fixed point

$S_{0} = \emptyset$ 
S0 is the empty set we start with nothing
$S_{n+1} = \text{\{true, false, 0\}} \cup \text{\{succ t ... \}}$ 
Sn+1 is every term we can construct from Sn 
$T = \cup S_{i}$
T is the union of all Si where i ranges over the natural numbers



# Equational reasoning 

**Defining terms:**
Define consts: a function that finds the set of unique constants in a term from T
$\text{consts true} = \{true\}$
$\text{consts false} = \{false\}$
$\text{consts 0} = \{0\}$
$\text{consts succ t} = \text{ consts t }$
...
$\text{consts (if } t_{0} t_{1} t_{2}) = \text{consts } t_{0} \cup \text{consts } t_{1} \cup \text{consts } t_{2}$   

This is like trying to find all the values (terms that cant be reduced further)
Also, you can substitute true with the set containing true


**Evaluating terms:**
If A = B then you can replace A with B wherever A occurs (Leibniz Equality)

consts (if true (succ 0) (pred 0))  = ... = {true, 0}

*Note that this is a proof and program execution*

This is also complete because we have a rule for every term


# Induction
**Math induction**: If P(0) holds and $\forall n \dot P(n) \Rightarrow P(n+1)$ then P holds for every n

For an example, prove that number of constants is always less than or equal than the number of terms
Prove: $\forall t, \text{|consts t|} \leq \text{terms t}$
- Case `true`, |consts true| $\leq$ terms true
	- |{true}| $\leq 1$
	- 1 $\leq$ 1
- Case `false`, |consts false| $\leq$ terms false
	- |{false}| $\leq 1$
	- $1 \leq 1$
- Case `succ`: $\forall t$, | const t| $\leq$ terms t $\Rightarrow$ | consts succ t | $\leq$ terms succ t


- Depth induction 
	- For each term t, given p(r) holds for all r where depth(r) < depth(t), then p(t) holds for t
- Size induction
	- For each term t, given p(r) for all r such that size(r) < size(t) we can show P(t) holds for all t
- Structural induction:
	- If for each term t, given P(r) for all immediate subterms r of t, we can show P(t)
	- If true for the parts, its true for the whole



## Small step operational semantics
the definitions of consts and terms (how these terms are defined) are the semantics of the function
single step is when one term evals to another in 1 step 
$$t\rightarrow t'$$
Homogenous relation (we go from same domain to range or terms in my language evaluate to terms in my language)
	Good because we can string together steps


$\frac{}{true \rightarrow true} \frac{}{false \rightarrow false} \frac{}{0 \rightarrow 0}$ 
Note that this means nothing is actually happening 
$\frac{}{succ\space 0 \rightarrow succ \space 0}$  We don't have 1 so we are just keeping successor
$\frac{}{pred \space 0 \rightarrow pred \space 0}$ THIS IS BAD

Here is the thing, these don't actually evaluate so why add a rule. WHen we get to true we are chilling so they don't evaluate 


what we want to show is that pre


We dont write evaluation rules for values (not yet)
Instead, succ and pred of 0 dont evaluate 
However pred (succ ( 0)) = 0
so 
$$\frac{}{\text{pred (succ 0)} \rightarrow 0}$$

Also: $$\frac{}{\forall t\space  \text{pred (succ t)} \rightarrow t}$$

Each rule should capture **one** step so no need to do pred (succ (pred (succ ...))) because they are multiple steps

Nested computations:
$$\frac{t\rightarrow t'}{\text{succ t} \rightarrow \text{succ t'}}$$ 
Same for isZero and pred
What these rules do is that they allow for evaluating subterms 
	They say evaluate the subterms before evaluating the terms

$$\frac{}{\text{if true } t_{0} \space t_{1} \rightarrow t_{0}}  \frac{}{\text{if false } t_{0} \space t_{1} \rightarrow t_{1}}  \frac{t_{\alpha}\rightarrow t_{\alpha}'}{\text{if } t_{\alpha} \space t_{0} \space t_{1} \rightarrow t_{\alpha}' \space t_{0} \space t_{1}}$$

### Rules of thumb
1. No inference rules for things that dont eval
2. Each rule only has one step
3. evaluate subterms before terms
4. no term has >1 inference rule


*Instance:*  instanciation of metavars in an inference rule
*Satisfies*: For each instance of a rule, either the conclusion is in a relation or one of its preconditions is not
	
*One-step Evaluation relation:* Smallest binary relation relying on terms satisfying all inference rules (t -> t')
	How a term becomes another term in one step
Derivable when (t, t') is in the evaluation relation t -> t' is derivable 
	You can do it
	Also called a judgement



## Pierce style language
Specify syntax and rules for eval

Definitions:
	*Normal form*: Term is in normal form if there are no eval rules that apply to it
	*value:* Term is a value if it represents the conclusion of computation
	Every value is in normal form
<mark style="background: #FF5582A6;">Is every term in normal form also a value</mark>
### Syntax
t ::= true | false | (if t t t)
	terms (everything)
v ::= true | false
	values (cant be simplified further)
Rules are as expected


Theorem: Determinicity of one step eval 
If t -> t' and t -> t'' then t' == t''

Proof by induction on t
- true - precondition is false (does not eval)
- false - same thing
- if
	- if c = true then only one rule applies 
	- if c = false then only one rule applies 
	- c -> c' by induction hypothesis 


Thm: Values are normal form
Proof by cases on t:
- true and false are values so no rule applies 
- All other terms are not values by def

Thm: Normal forms are values:
Proof:
- true, false are normal forms so no rule applies 
- if c t e
	- c $\in$ {true, false} so rules apply
	- c -> c' - rules apply

That means all normal forms are values which are normal forms 
	This is good because everything will evaluate to a value

### Multistep
Multi step eval (r ->* r') is the reflexive transitive closure of the single step relation (r -> r')
	Take all the one steps you can take and glue them together (if a->b and b-> c then a->* c)

1. if t -> t' then t ->* t'
2. t ->* t for all t
3. if t ->* t' and t' -> t'' then t ->* t''

Defining with inference rules
Reflexive rule:
$$\frac{}{t \rightarrow^{*} t} \text{refl}$$
Step rules:
$$\frac{t \rightarrow t'}{t \rightarrow^{*} t'} \text{step}$$ This one is saying that if t evals to t', then t eval* t'

This one is transitive property
$$\frac{t \rightarrow^{*} t' \quad t' \rightarrow t''}{t \rightarrow^{*} t''} \text{trans}$$

Theorem: Uniqueness of normal forms 
	If t ->* u and t ->* u' then u == u'


Prove:$$\frac{}{\text{if true false true} \rightarrow \text{false}}$$
One of the axioms is that if true t e -> t so thats the proof. 
	Don't do these proofs