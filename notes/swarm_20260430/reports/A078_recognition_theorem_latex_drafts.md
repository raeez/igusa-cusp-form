# A078 - Recognition Theorem LaTeX Drafts

No files edited by the agent. The agent used the repo-local
`chriss-ginzburg-rectify` skill, A067-A076, and the live anchors around
`main.tex` lines 15011, 15275, and 15380. Target checks passed via
`compute/verify_lattice.py` and `compute/verify_square_root.py`.

A071 caveat: its 35-positive-degree packet is relation-minimal, not the
full downward-saturated height window. The statement below calls it
`W_{\mathrm{rel}}^{+}` and says to use its downward closure only when
invoking the cofinal-window definition literally.

## W_{\le3} Certificate Snippet

At `main.tex` near line 15011, replace the current first-window
proposition by:

```tex
\begin{theorem}[\(W_{\le3}\) primitive-recognition certificate]
\label{prop:first-saturated-primitive-recognition-window}
\label{thm:wlethree-primitive-recognition-certificate}
Let
\[
W_{\le3}=\{\beta=\sum_i c_i\delta_i:c_i\ge0,\ 1\le\sum_i c_i\le3\},
\qquad
S_{\le3}=W_{\le3}\cup(-W_{\le3})\cup\{0\}.
\]
Assume a compact Hall stage \(R\) supplies an A067 source fixture
\(\mathcal C_{\le3}(R)\) on \(S_{\le3}\): neutral source bases with
geometric provenance, parity blocks, matrices \(M,D,B,G,K,Q,A\), exact
super-sign convention, relation rows, NO7 radical rows, no-extra kernel
equality, PBW associated-graded rows, and strict transition/ML rows.
Target labels \(e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s\) occur only in the
target fixture and in the codomain columns of \(A_{\beta,\bar p}\).

The target dimensions on active positive degrees are
\[
\delta_i:1|0,\qquad
a_{ij}:=\delta_i+\delta_j:10|0,\qquad
2\delta_i+\delta_j\ (i\ne j):1|0,\qquad
\tau:=\delta_1+\delta_2+\delta_3:29|93,
\]
and all non-root degrees in \(W_{\le3}\) have zero quotient source piece.
The fixture verifies the Chevalley, adjacent isotropic orthogonality,
Jacobi \(T_1^X+T_2^X+T_3^X=0\), the \(27\) mixed maps
\([e_k^X,u_{ij,r}^X]\), NO7, no-extra-relations, PBW, and strict
transition gates inside \(S_{\le3}\). Terminal real-Serre and
complementary-string rows whose outputs leave \(S_{\le3}\) are marked
deferred.

Then the comparison induced by the \(A_{\beta,\bar p}\) is an isomorphism
\[
\Phi_{R,\le3}:
P^{\Pi,\mathrm{red}}_{X,R,\le W_{\le3}}
\xrightarrow{\sim}
G(\mathscr B_{\Delta_5})_{\le W_{\le3}}
\]
of finite Gram-graded Lie superalgebras with parity. The equality
\(29-93=-64=f(1,1)\) is only the target signed trace; it is not this
certificate.
\end{theorem}
```

Proof skeleton: relation rows put the finite Borcherds-Kac ideal in
`\ker\pi_{R,\le3}`; NO7 and Hopf adjointness make the source radical a
Lie ideal and coideal; the maps `A_{\beta,\bar p}` intertwine bracket,
coproduct, pairing, and Cartan action; no-extra kernel equality gives
injectivity; generation gives surjectivity; PBW ranks exclude hidden
relations invisible to signed dimensions.

## A071 Relation-Closed Snippet

Insert after the height-four obstruction discussion, before the generic
verifier theorem:

```tex
\begin{theorem}[A071 relation-closed primitive certificate]
\label{thm:a071-relation-closed-primitive-certificate}
Put \(a_{ij}=\delta_i+\delta_j\), \(\tau=\delta_1+\delta_2+\delta_3\),
and, for \(\{i,j,k\}=\{1,2,3\}\),
\[
C_{k,s}=a_{ij}+s\delta_k.
\]
Let
\[
W_{\mathrm{rel}}^{+}
=
W_{\le3}^{\mathrm{act}}\cup R_4\cup I_4\cup C_{\le7}\cup\{2\tau\},
\]
where
\[
W_{\le3}^{\mathrm{act}}
=\{\delta_i,\ a_{ij},\ 2\delta_i+\delta_j\ (i\ne j),\ \tau\},
\]
\[
R_4=\{3\delta_i+\delta_j:i\ne j\},\qquad
I_4=\{2a_{ij}:i<j\},\qquad
C_{\le7}=\{C_{k,s}:k=1,2,3,\ 2\le s\le5\}.
\]
Set \(S_{\mathrm{rel}}=W_{\mathrm{rel}}^{+}
\cup(-W_{\mathrm{rel}}^{+})\cup\{0\}\).
If Definition~\ref{def:cofinal-primitive-recognition-datum} is invoked
literally, replace \(W_{\mathrm{rel}}^{+}\) by its downward closure.

Assume a compact Hall stage \(R\) supplies the same A067 packet on
\(S_{\mathrm{rel}}\), with full target parity fixtures and source
provenance in every retained degree. The relation rows include the
height-four real-Serre terminal rows \((\operatorname{ad}e_i)^3e_j=0\),
the doubled isotropic rows \(a_{ij}+a_{ij}=2a_{ij}\), the
\(\tau\)-real strings through \(\tau+3\delta_i\), the odd-odd
\(\tau\)-rows through \(2\tau\), and the complementary terminal rows
\[
(\operatorname{ad}e_k)^5u_{ij,r}=0
\quad\text{in degree } C_{k,5}.
\]
They are source matrix rows, not consequences of the signed product
coefficients.

Then
\[
\Phi_{R,\mathrm{rel}}:
P^{\Pi,\mathrm{red}}_{X,R,\le W_{\mathrm{rel}}^{+}}
\xrightarrow{\sim}
G(\mathscr B_{\Delta_5})_{\le W_{\mathrm{rel}}^{+}}
\]
is an isomorphism on the A071 relation window, and every defining
relation whose first nontrivial prefix appears in \(W_{\le3}\) is closed
by an actual terminal source row.
\end{theorem}
```

Proof skeleton: apply the finite verifier theorem to the A071 packet.
The added degrees are exactly the outputs missing from `W_{\le3}`:
real-Serre terminals, doubled isotropics, `\tau`-real strings, `2\tau`,
and complementary height-seven terminals. NO7 descends the Hopf
structure; no-extra and PBW identify the quotient with the GN/Kac
presentation. The target arithmetic checks only the expected rows; the
source certificate supplies the proof.

## Generic Verifier Snippet

At `main.tex` near line 15275, retitle and sharpen the generic criterion:

```tex
\begin{theorem}[Finite primitive-recognition certificate verifier]
\label{thm:executable-finite-source-matrix-criterion}
Let \(W\subset Q_+\setminus\{0\}\) be a finite certificate window, and put
\(S_W=W\cup(-W)\cup\{0\}\). A compact Hall stage \(R\) passes the finite
primitive-recognition verifier on \(W\) if it supplies exact source bases
and matrices
\[
M_{\alpha,\beta},\quad D^{\mu,\nu}_{\rho},\quad
G_{\beta,\bar p},\quad K_{\beta,\bar p},\quad Q_{\beta,\bar p},\quad
A_{\beta,\bar p}
\]
on \(S_W\), with
\[
B^X_{\alpha,\beta}
=M_{\alpha,\beta}-(-1)^{|x||y|}M_{\beta,\alpha}\tau,\qquad
K_{\beta,\bar p}=\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t},
\]
and splittings \(P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p}\),
\(Q_{\beta,\bar p}=[0\ I]\). It must verify:
\[
QB^X(P\otimes K)=0,\qquad QB^X(K\otimes P)=0,\qquad
(Q\otimes Q)D^XK=0,
\]
Hopf adjointness, quotient-pairing nondegeneracy, all retained
Borcherds--Kac relation rows, the comparison equations for \(A\), the
kernel equality
\[
\ker\pi_{R,W}
=
\bigl(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}}\bigr)_{\le W},
\]
the PBW associated-graded isomorphism, and strict transition/ML
stable-image identities. Then radical descent, no-extra-relations, PBW,
and exact finite-window recognition hold on \(W\).
\end{theorem}
```

Proof skeleton: `QB` and `QD` give a well-defined quotient bracket and
coproduct. Hopf adjointness gives compatibility with the pairing. The
relation gate gives `J_{\mathrm{BK}}\subset\ker\pi_{R,W}`. Kernel
equality gives injectivity after the GN radical quotient; generation and
the `A`-comparison give surjectivity. PBW and ML strictness allow passage
through associated gradeds and later inverse limits.

## NO7 Sub-Verifier Snippet

At `main.tex` near line 15380, demote the NO7 protocol to a true
sub-verifier:

```tex
\begin{corollary}[\(W_{\le3}\) NO7 sub-verifier]
\label{prop:finite-wlethree-no7-source-protocol}
\label{cor:wlethree-no7-subverifier}
Assume the \(W_{\le3}\) source packet supplies \(G,K,Q,M,D,B\) and passes
\[
QB(P\otimes K)=0,\qquad QB(K\otimes P)=0,\qquad
(Q\otimes Q)DK=0,
\]
together with Hopf adjointness, quotient-pairing nondegeneracy, and
transition preservation of \(K_{\beta,\bar p}\). Then the radical
quotient carries a well-defined finite bracket and coproduct on
\(S_{\le3}\).

This sub-verifier does not prove no-extra-relations, PBW compatibility,
full parity matching, source-to-target recognition, or the
\(W_{\le3}\) certificate theorem.
\end{corollary}
```

Proof skeleton: the two `QB` containments are exactly lift-independence
of the bracket modulo the radical. The `QD` containment is
lift-independence of the coproduct. Hopf adjointness and nondegeneracy
make the quotient pairing a Hopf pairing. Nothing here computes
`\ker\pi_{R,W}`, PBW ranks, or the comparison maps
`A_{\beta,\bar p}`.

