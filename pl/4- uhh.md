
\section*{Add Boolean, and IF}

\subsection*{Syntax}

$t::=\ ...|\ true\ |\ false\ |\ \text{if }t \text{ then }t \text{ else } t$

$v::=\ ...|\ true\ |\ false$

$T::=\ ...\ |\ Bool$

\subsection*{Evaluation Rules}

$$
\frac{t_1 \to t_1'}
{\text{if } t_1 \text{ then } t_2 \text{ else } t_3  \to
\text{if } t_1' \text{ then } t_2 \text{ else } t_3} \quad EIfFirst
$$

$$
\frac{}
{\text{if } true \text{ then } t_2 \text{ else } t_3  \to t_2} \quad EIfTrue
$$

$$
\frac{}
{\text{if } false \text{ then } t_2 \text{ else } t_3  \to t_3} \quad EIfFalse
$$

\subsection*{Type Rules}

$$
\frac{}{true:Bool}
$$

$$
\frac{}{false:Bool}
$$

$$
\frac
{\Gamma \vdash t_1:Bool \quad \Gamma \vdash t_2:T \quad \Gamma \vdash t_3:T}
{(\text{if } t_1 \text{ then } t_2 \text{ else } t_3):T} \quad TIf
$$

\section*{Placeholder}

\subsection*{Proof Of Progress}

if $\Gamma \vdash t:T$ then $t$ is a value or $t \to t',\ \exists t'$

\begin{itemize}

\item $true$ is a value and as such, it the theorem holds true as it doesn't evaluate further.

\item $false$ is a value and as such, it the theorem holds true as it doesn't evaluate further.

\item $\Gamma \vdash (\text{if } t_1 \text{ then } t_2 \text{ else } t_3):T$ - We assume progress for $t_1$ $t_2$, $t_3$

\begin{itemize}
    \item  Case 1: $t_1$ is not a value because it is not $true$ or $false$. Then $t_1 \to t_1'$ (inductive hypothesis) and EIf applies.
    
    \item Case 2: $t_1$ is a value $true$ and $t_2:T$, $t_2:T$ then $t$ evaluates to $t_3$  (inductive hypothesis) and EIfTrue applies.
    
    \item Case 3: $t_1$ is a value $false$ and $t_2:T$, $t_2:T$ then $t$ evaluates to $t_2$ (inductive hypothesis) and EIfFalse applies.
\end{itemize}
\end{itemize}
```