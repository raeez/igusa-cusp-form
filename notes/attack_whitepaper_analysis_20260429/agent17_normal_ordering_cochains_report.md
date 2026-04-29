# Agent 17 Normal-Ordering Cochains Report

Scope: normal-ordering, cochain-level repairs, \(B(c,c')\), \(\Pi_X\), NO1--NO7, finite diagrams, raw pushforward no-go, flag formulas, Hochschild/Picard dg language, and the exact insertion point for the chain-level normal-ordered pushforward.

Status: the formal lattice core is strong. The manuscript proves the correct quadratic defect, the \(B\)-twisted extension, additivity of \(\overline\Pi_X\), and a fixed-lift raw-descent obstruction. The remaining attack surface is local but serious: the paper still blurs raw placement with the split section, ordinary group-cohomology wording with Picard dg cochains, physical-charge cochains with \(\widehat\Gamma_X\)-cochains, and a raw pushforward theorem whose object is not defined before it is attacked.

## Stable formal facts

1. **Raw Gram map is quadratic.** For
\[
\Gamma_X^{\mathrm{form}}=\Lambda_S\oplus\Lambda_S,\qquad c=(Q,P),
\]
the Gram-index lattice is
\[
\Gamma_{\mathrm{gram}}=\mathbb Z^3,
\]
and
\[
\Pi_X(Q,P)=\left(\frac{Q^2}{2},Q\cdot P,\frac{P^2}{2}\right).
\]
This is a Fourier/root-degree map, not an additive Hall charge grading.

2. **The polarization defect is explicit.**
\[
B((Q,P),(Q',P'))=(Q\cdot Q',\,Q\cdot P'+Q'\cdot P,\,P\cdot P').
\]
Then
\[
\Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+B(c,c'),\qquad B(c,c)=2\Pi_X(c).
\]
This is pure lattice polarization. It has no dependence on orientation, Bott elements, Pfaffian signs, Hilbert-space parity, or OP scalar normalization.

3. **\(B\) is a normalized symmetric bilinear 2-cocycle.**
\[
B(c,0)=B(0,c)=0,
\]
and
\[
B(a,b)+B(a+b,c)=B(b,c)+B(a,b+c).
\]
This is the degree shadow of every two-step flag coherence.

4. **The normal-ordered extension is the right additive degree object.**
\[
\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
\]
with
\[
(c,T)\star(c',T')=(c+c',T+T'+B(c,c')).
\]
It is an abelian group. The unit is \((0,0)\), and
\[
(c,T)^{-1}=(-c,-T+B(c,c)).
\]

5. **The normal-ordered Gram map is additive.**
\[
\overline\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}},\qquad
\overline\Pi_X(c,T)=\Pi_X(c)-T,
\]
and
\[
\overline\Pi_X((c,T)\star(c',T'))=
\overline\Pi_X(c,T)+\overline\Pi_X(c',T').
\]

6. **The raw placement and the split section are different.**
\[
i_0(c)=(c,0),\qquad s(c)=(c,\Pi_X(c)).
\]
Then
\[
\overline\Pi_X(i_0(c))=\Pi_X(c),\qquad
\overline\Pi_X(s(c))=0.
\]
\(i_0\) is the one-particle/Hall placement for a visible raw Gram degree. It is not additive for \(\star\). The section \(s\) is additive and splits the extension, but it kills the visible Gram degree. Confusing these two maps destroys the interpretation of generators.

7. **Flag formula.** For elementary defect-zero placements,
\[
(c_1,0)\star\cdots\star(c_k,0)
=\left(\sum_i c_i,\sum_{i<j}B(c_i,c_j)\right),
\]
and therefore
\[
\overline\Pi_X\bigl((c_1,0)\star\cdots\star(c_k,0)\bigr)
=\sum_i\Pi_X(c_i).
\]
This is the finite HN word law. The second coordinate is the accumulated normal-ordering counterterm.

8. **Ordinary cocycle class versus linear-trivialization obstruction.** In ordinary additive cochains with
\[
(\delta q)(c,c')=q(c)+q(c')-q(c+c'),
\]
one has
\[
B=-\delta\Pi_X.
\]
Thus the ordinary cocycle class of \(B\) is zero once quadratic cochains are admitted. The residual obstruction is narrower and stronger: no additive homomorphism
\[
L:\Gamma_X^{\mathrm{form}}\to\Gamma_{\mathrm{gram}}
\]
can satisfy
\[
B(c,c')=L(c)+L(c')-L(c+c')
\]
unless \(\Pi_X\equiv0\). Do not call this residual a nonzero ordinary cohomology class.

9. **Picard dg cochain is the categorified normal-ordering datum.** With central translations
\[
(\mathsf T_\eta V)_\gamma=V_{\gamma+\eta},
\]
the chain cocycle is
\[
B_{\mathrm{ch}}(c,c')=\mathsf T_{B(c,c')}.
\]
The physical-charge cochain is
\[
\Theta_\Pi(c)=\mathsf T_{-\Pi_X(c)}
\]
and it satisfies
\[
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}
\]
in \(\mathsf{Pic}^{\mathrm{dg}}_{\Gamma_{\mathrm{gram}}}\). On normal-ordered labels the character is
\[
\widehat\Theta_\Pi(c,T)=\mathsf T_{-\overline\Pi_X(c,T)}
=\mathsf T_{T-\Pi_X(c)},
\]
and
\[
d_{\mathrm{Hoch}}\widehat\Theta_\Pi=0.
\]

10. **Raw fixed-lift pushforward no-go.** If \(P=\oplus_cP_c\) is \(\Gamma_X^{\mathrm{form}}\)-graded and
\[
[P_c,P_{c'}]\subset P_{c+c'},
\]
a strict fixed-lift raw \(\Pi_X\)-pushforward is \(\Gamma_{\mathrm{gram}}\)-graded only on bracket channels satisfying
\[
[P_c,P_{c'}]\ne0\quad\Rightarrow\quad B(c,c')=0.
\]
For distinct type-II real simple generators, the target has
\[
[e_i,e_j]\ne0,\qquad [e_i,[e_i,e_j]]\ne0,\qquad (\operatorname{ad}e_i)^3e_j=0.
\]
The first bracket forces \(B(c_i,c_j)=0\). The second forces \(B(c_i,c_i+c_j)=0\). But
\[
B(c_i,c_i+c_j)=B(c_i,c_i)+B(c_i,c_j)=2\Pi_X(c_i)=2\gamma_i\ne0.
\]
Thus raw fixed-lift descent cannot realize the full BKM real-root strings. This does not exclude isolated \(B\)-isotropic channels or a fibre-summed raw construction.

## Current manuscript defects

1. **\(H^2_{\mathrm{sym}}\) language is unsafe.** `main.tex:4366-4368` and `main.tex:4813-4822` say \([B]=0\) and then describe a nontriviality "as a class in linear cochains." That is not a standard ordinary cohomology statement. The stable claim is: ordinary class zero by quadratic primitive; no additive linear trivialization.

2. **Raw placement \(i_0\) is not defined beside \(s\).** `main.tex:4672-4682` and `main.tex:4832-4860` define the split section \(s(c)=(c,\Pi_X(c))\), while `main.tex:10425-10428` later places one-particle generators in \((c,0)\). The text needs the comparison display immediately at the extension definition:
\[
i_0(c)=(c,0),\quad s(c)=(c,\Pi_X(c)),\quad
\overline\Pi_X(i_0(c))=\Pi_X(c),\quad
\overline\Pi_X(s(c))=0.
\]

3. **Flag normal-ordering formula is missing from the lattice theorem.** The finite \(D_0\) support uses composite HN words and accumulated \(T\)-labels, but `main.tex:4614-4881` does not state the general word formula. This should be a lemma immediately after `lem:normal-ordered-extension-group-law`.

4. **Raw pushforward is attacked before it is defined.** `main.tex:4883-4897` says "strict fixed-lift raw pushforward" but does not define the fixed-lift or raw homogeneous pushforward variant first. The proof is correct once the object is defined.

5. **The abstract still uses the older phrase.** `main.tex:146-166` says "strict fixed-lift raw Gram descent." The attack transcript asks for "raw homogeneous \(\Pi_X\)-pushforward" for the general criterion, with the fixed-lift variant defined separately.

6. **`main.tex:5678-5690` is too loose.** The phrase "the \(\Gamma_{\mathrm{ind}}\)-grading ... is the \(\Pi\)-image, well defined modulo the cocycle \(B\)" should be replaced. The target grading is additive internally. A Hall source reaches it only by \(\overline\Pi_X\) or by a \(B\)-isotropic raw channel.

7. **Open problem mixes lattice cochain with Picard dg cochain.** `main.tex:8330-8337` writes \(d_{\mathrm{Hoch}}\Theta_\Pi=B\) and then \(d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}\). The first equation must be \(d_{\mathrm{Hoch}}(-\Pi_X)=B\) in \(\Gamma_{\mathrm{gram}}\)-valued cochains. The second is the Picard dg equation.

8. **NO3 quantifier bug.** `main.tex:9192-9199` quantifies \(c,c'\in\widehat\Gamma_{R^+}\) but uses \(B_{\mathrm{ch},R}(c,c')\), defined on physical charges. It must either quantify \(c,c'\in\Gamma_X^{\mathrm{phys}}\), or write \(\widehat c=(c,T)\), \(\widehat c'=(c',T')\) and use \(d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0\).

9. **D0-N display is conceptually right but underdefined.** `main.tex:10501-10516` writes a degree-shift \(\Theta_{(c,T),(c',T')}\) on normal-ordered labels. It should say this is induced from the physical cochain plus recorded \(T,T'\)-shifts, or define \(\widehat\Theta_{\Pi,R}(c,T)=\mathsf T_{T-\Pi_X(c)}\) and state its Hochschild boundary is zero.

10. **The universal \(s_L\) algebraic lift is absent.** The attack transcript repeatedly requests a theorem: choose a group homomorphism
\[
L:\Gamma_{\mathrm{gram}}\to\Gamma_X^{\mathrm{form}},
\]
define
\[
s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma),
\]
prove \(s_L(\gamma+\eta)=s_L(\gamma)\star s_L(\eta)\), and regrade \(\mathfrak g_{\Delta_5,\gamma}\) along \(s_L\). This is optional for a minimal paper, but if the paper wants a universal algebraic Dirac-Igusa target, it is the exact construction.

11. **Chain-level normal ordering is sometimes over-read as formal.** `main.tex:8414-8417`, `main.tex:8692-8696`, and `main.tex:8980-8997` correctly say the lattice homomorphism does not produce Hall strictification. That discipline must survive every rewrite. The finite Picard lift is formal only after the finite coefficient dg category exists; the source-side Hall, orientation, cyclic, Frobenius, and radical data remain non-formal.

## Exact replacement language/formulas

1. **Replace the \(H^2_{\mathrm{sym}}\) wording.**

Use:

> The ordinary additive cocycle class of \(B\) is zero once quadratic cochains are allowed: \(B=-\delta\Pi_X\). The remaining obstruction is not a nonzero ordinary cohomology class. It is the absence of a linear trivialization: no additive \(L:\Gamma_X^{\mathrm{form}}\to\Gamma_{\mathrm{gram}}\) satisfies \(B(c,c')=L(c)+L(c')-L(c+c')\) unless \(\Pi_X\equiv0\).

2. **Add raw versus split placement after the extension definition.**

\[
i_0(c)=(c,0),\qquad s(c)=(c,\Pi_X(c)),
\]
\[
\overline\Pi_X(i_0(c))=\Pi_X(c),\qquad
\overline\Pi_X(s(c))=0.
\]

Text:

> The map \(i_0\) is the raw one-particle placement used by Hall generators before any composite counterterm has been accumulated. It is not a homomorphism for \(\star\). The map \(s\) is the split section of the abelian extension. It is a homomorphism, but it lands in normal-ordered Gram degree zero; it is not the visible Gram-degree placement of a generator.

3. **Add the flag lemma.**

Statement:
\[
(c_1,0)\star\cdots\star(c_k,0)
=\left(\sum_i c_i,\sum_{1\le i<j\le k}B(c_i,c_j)\right).
\]
Consequently,
\[
\overline\Pi_X\bigl((c_1,0)\star\cdots\star(c_k,0)\bigr)
=\sum_i\Pi_X(c_i).
\]

Proof:

> Induct on \(k\). The case \(k=2\) is the definition of \(\star\). Multiplying the \(k\)-fold formula by \((c_{k+1},0)\) adds \(B(\sum_{i\le k}c_i,c_{k+1})=\sum_{i\le k}B(c_i,c_{k+1})\). Applying \(\overline\Pi_X\) subtracts the accumulated pairwise sum from \(\Pi_X(\sum_i c_i)=\sum_i\Pi_X(c_i)+\sum_{i<j}B(c_i,c_j)\).

4. **Define raw homogeneous \(\Pi_X\)-pushforward before the no-go.**

Use:

> A raw homogeneous \(\Pi_X\)-pushforward of a \(\Gamma_X^{\mathrm{form}}\)-graded Lie superalgebra \(P=\oplus_cP_c\) is the attempted \(\Gamma_{\mathrm{gram}}\)-graded object
> \[
> (\Pi_{X,*}^{\mathrm{raw}}P)_\gamma=\bigoplus_{\Pi_X(c)=\gamma}P_c
> \]
> with bracket induced from \(P\), without inserting \(T\)-labels or \(\Theta\)-translations. A strict fixed-lift raw pushforward is the special case in which, for each retained \(\gamma\), a chosen lift \(L(\gamma)\) is used and only \(P_{L(\gamma)}\) contributes.

Then:

> On any nonzero bracket channel \(P_c\otimes P_{c'}\to P_{c+c'}\), raw homogeneity is equivalent to \(B(c,c')=0\).

5. **Replace denominator grading comparison.**

Use:

> The denominator algebra is additively graded by \(\Gamma_{\mathrm{ind}}\cong\mathbb Z^3\) and by its Lorentzian image \(\alpha(\Gamma_{\mathrm{ind}})\). A Hall source is additively graded upstairs by \(\Gamma_X^{\mathrm{form}}\), or after normal ordering by \(\widehat\Gamma_X\). Its comparison with the denominator grading is made by \(\overline\Pi_X\). The raw quadratic map \(\Pi_X\) is not a bracket-recognition target unless every visible bracket channel is \(B\)-isotropic.

6. **Repair the open-problem cochain equations.**

Use:
\[
d_{\mathrm{Hoch}}(-\Pi_X)=B
\quad\text{in }\Gamma_{\mathrm{gram}}\text{-valued cochains},
\]
and
\[
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}
\quad\text{in }\mathsf{Pic}^{\mathrm{dg}}_{\Gamma_{\mathrm{gram}}},
\qquad
\Theta_\Pi(c)=\mathsf T_{-\Pi_X(c)}.
\]

7. **Repair NO3.**

Use either physical-label version:

> For every finite physical charge pair \(c,c'\) whose \(T\)-recorded channels occur at height \(R\),
> \[
> d_{\mathrm{Hoch}}\Theta_{\Pi,R}^{\mathrm{phys}}(c,c')=B_{\mathrm{ch},R}(c,c'),
> \qquad
> (b+uB_C)\Theta_{\Pi,R}^{-}=B_{\mathrm{ch},R}^{-}.
> \]

or normal-ordered-label version:
\[
\widehat\Theta_{\Pi,R}(c,T)=\mathsf T_{T-\Pi_X(c)},\qquad
d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0.
\]
Do not mix the two quantifier domains.

8. **Optional universal algebraic lift.**

If retained, state:

> For any group homomorphism \(L:\Gamma_{\mathrm{gram}}\to\Gamma_X^{\mathrm{form}}\), the map
> \[
> s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)
> \]
> is a group homomorphism \(\Gamma_{\mathrm{gram}}\to\widehat\Gamma_X\) and satisfies \(\overline\Pi_X(s_L(\gamma))=\gamma\). Regrading \(\mathfrak g_{\Delta_5,\gamma}\) to degree \(s_L(\gamma)\) gives a \(\widehat\Gamma_X\)-graded algebra whose normal-ordered pushforward is \(\mathfrak g_{\Delta_5}\).

Add the warning: \(L\) is not canonical; different \(L\)'s give equivalent pushforwards but different upstairs labels.

## Finite certificate tests

NO1--NO7 are the chain-level place where the normal-ordered pushforward must be defined. The exact object is not the lattice map alone. It is the finite inverse-system pushforward
\[
(\overline\Pi_{R,*}^{\Theta}V_R)_\gamma
=
\prod_{\substack{(c,T)\in\widehat\Gamma_R\\
\overline\Pi_X(c,T)=\gamma}}(V_R)_{(c,T)}
\]
with finite fibres at height \(R\), followed by
\[
(\overline\Pi_{X,*}^{\Theta}V)_\gamma
=
\varprojlim_R(\overline\Pi_{R,*}^{\Theta_R}V_R)_\gamma.
\]

The seven tests are:

1. **NO1 finite fibres.** The square
\[
\rho^\Pi_{R^+R}\overline\Pi_{R^+,*}^{\Theta_{R^+}}
=
\overline\Pi_{R,*}^{\Theta_R}\rho_{R^+R}
\]
must commute. This proves finite fibre products over \(\overline\Pi_X\) before completion.

2. **NO2 product, coproduct, pairing.** The transported product \(m_R^\Theta\), coproduct \(\Delta_R^\Theta\), and pairing must commute with successor transitions. No infinite uncontrolled tensor product is allowed.

3. **NO3 Hochschild and negative-cyclic equations.** Physical cochain:
\[
d_{\mathrm{Hoch}}\Theta_{\Pi,R}^{\mathrm{phys}}=B_{\mathrm{ch},R}.
\]
Normal-ordered character:
\[
d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0.
\]
Cyclic refinement:
\[
(b+uB_C)\Theta_{\Pi,R}^{-}=B_{\mathrm{ch},R}^{-}.
\]

4. **NO4 triple flag.** For every two-step Hall flag,
\[
(\mathsf A_{a,b,c}\circ(\vartheta_{a,b}\otimes1)\circ\vartheta_{a+b,c})
-
((1\otimes\vartheta_{b,c})\circ\vartheta_{a,b+c})=0.
\]
The lattice shadow is \(B(a,b)+B(a+b,c)-B(b,c)-B(a,b+c)=0\); the chain equality is extra data.

5. **NO5 Jacobi.** The transported bracket must have zero finite Jacobiator:
\[
\operatorname{Jac}_{\Theta,R}(x,y,z)=0.
\]

6. **NO6 Frobenius.**
\[
\langle[x,y]_\Theta,z\rangle_R
+(-1)^{|x||y|}\langle y,[x,z]_\Theta\rangle_R=0.
\]

7. **NO7 Hopf radical.** Let
\[
G_\beta:P^\Pi_{R,\beta}\times P^\Pi_{R,-\beta}\to\mathbb C,
\quad
K_\beta=\ker G_\beta\cap\ker G_{-\beta}^{t},
\quad
Q_\beta:P^\Pi_{R,\beta}\to P^\Pi_{R,\beta}/K_\beta.
\]
For every retained bracket matrix \(B_{\alpha,\beta}\) and coproduct matrix \(D_\rho^{\mu,\nu}\), verify
\[
Q_{\alpha+\beta}B_{\alpha,\beta}(P^\Pi_{R,\alpha}\otimes K_\beta)=0,
\]
\[
Q_{\alpha+\beta}B_{\alpha,\beta}(K_\alpha\otimes P^\Pi_{R,\beta})=0,
\]
\[
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_{\rho}K_\rho=0.
\]
Also verify Hopf adjointness
\[
\langle M_{\alpha,\beta}(x\otimes y),z\rangle_R
=
\langle x\otimes y,D^{\alpha,\beta}_{\alpha+\beta}z\rangle_R,
\]
quotient-tensor nondegeneracy, and transition preservation
\[
\rho^P_{R^+R}(K_{R^+,\beta})\subset K_{R,\beta}.
\]
Signed determinant data and target bracket templates do not supply these matrices.

## main.tex anchors

- `main.tex:131-166`: abstract charge/normal-ordering summary; still uses "strict fixed-lift raw Gram descent."
- `main.tex:4309-4382`: dyonic Mukai lattice, \(\Pi_X\), \(B\), \(\widehat\Gamma_X\), \(\overline\Pi_X\); contains unsafe \(H^2_{\mathrm{sym}}\) wording.
- `main.tex:4384-4395`: remarks that the split requires quadratic \(\Pi_X\); good but should be tied to \(i_0\) versus \(s\).
- `main.tex:4431-4454`: Gram-index warning; stable.
- `main.tex:4523-4588`: primitive torsion-one lift; stable formal pointwise lift only.
- `main.tex:4590-4810`: \(B\)-cocycle, \(\star\), split extension, no linear trivialization; repair cohomology language.
- `main.tex:4811-4830`: current cohomology-status remark; replace with ordinary-zero / no-linear-trivialization language.
- `main.tex:4832-4881`: normal-ordered extension definition; add \(i_0\) versus \(s\) and flag formula immediately after.
- `main.tex:4883-4975`: raw-descent no-go; define raw homogeneous/fixed-lift pushforward before theorem.
- `main.tex:5678-5690`: denominator grading comparison; replace "well defined modulo \(B\)" wording.
- `main.tex:8305-8346`: open problem for normal-ordered descent; repair \(d_{\mathrm{Hoch}}\Theta_\Pi=B\) versus \(B_{\mathrm{ch}}\).
- `main.tex:8348-8525`: coefficient dg category and finite Picard lift; good core; use it to repair NO3.
- `main.tex:8603-8998`: conditional chain-level descent theorem; stable if kept explicitly conditional.
- `main.tex:9132-9319`: NO1--NO7; fix NO3 quantifier domain.
- `main.tex:9397-9461`: finite Hopf-adjointness radical test; stable.
- `main.tex:9463-9511`: negative-cyclic route; stable only as a conditional route, not a construction from (P) alone.
- `main.tex:10414-10440`: D0-C uses \(i_0(c)=(c,0)\) implicitly; tie back to the new warning.
- `main.tex:10498-10590`: D0-N; define whether \(\Theta_{(c,T),(c',T')}\) is induced from physical \(\Theta_\Pi\) or is \(\widehat\Theta_\Pi\).
- `main.tex:12001-12048`: full certificate correctly places \(\overline\Pi_{X,*}^{\Theta}\); keep.
- `main.tex:13062-13083`: \(W_{\le3}\) NO7 matrix requirements; stable.
- `main.tex:13205-13274`: finite \(W_{\le3}\) NO7 source protocol; stable.
- `main.tex:13314-13336`: open \(D_0\)-descent obligations; stable.

## Patch queue

1. Replace every informal "well-defined modulo \(B\)" with "normal-ordered image under \(\overline\Pi_X\)" unless the channel is explicitly \(B\)-isotropic.

2. Define \(i_0(c)=(c,0)\) beside \(s(c)=(c,\Pi_X(c))\), and state which one is used for one-particle Hall generators.

3. Add the flag normal-ordering lemma after the extension group-law lemma.

4. Introduce a definition of raw homogeneous \(\Pi_X\)-pushforward and its strict fixed-lift special case before `thm:raw-gram-descent-no-go`.

5. Rewrite the no-go theorem title to: "Raw homogeneous fixed-lift \(\Pi_X\)-pushforward cannot realize the type-II real-root strings." Keep the fibre-summed caveat.

6. Replace the \(H^2_{\mathrm{sym}}\) and "linear cochains" wording with the ordinary-zero / no-linear-trivialization statement.

7. In the open problem, replace
\[
d_{\mathrm{Hoch}}\Theta_\Pi=B
\]
with
\[
d_{\mathrm{Hoch}}(-\Pi_X)=B
\]
in \(\Gamma_{\mathrm{gram}}\)-valued cochains, followed by
\[
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}
\]
in the Picard dg groupoid.

8. Fix NO3 by choosing one of the two domains:
physical \(c,c'\) with \(d_{\mathrm{Hoch}}\Theta_{\Pi,R}^{\mathrm{phys}}=B_{\mathrm{ch},R}\), or normal-ordered \((c,T)\) with \(d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0\).

9. In D0-N, define
\[
\widehat\Theta_{\Pi,R}(c,T)=\mathsf T_{T-\Pi_X(c)}
\]
or explicitly say the displayed shift is induced from physical \(\Theta_{\Pi,R}\) plus recorded \(T,T'\)-shifts.

10. If the manuscript keeps the construction-first universal target, add the \(s_L\) theorem and the curve-universal \(\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}\). If the manuscript stays minimal, omit \(s_L\) and say the compact algebraic lift is not constructed.

11. Keep \(\overline\Pi_{X,*}^{\Theta}\) first defined in the coefficient dg/finite HN section, not in the abstract. The abstract may mention the normal-ordered extension; the chain-level pushforward belongs at `main.tex:8348-8525` and `main.tex:8603-8998`.

## Residual proof obligations

1. **Finite source kernel.** Build actual finite \(R\)-stage Hall source objects, extension stacks, flag stacks, products, coproducts, pairings, and transition maps before claiming chain-level normal ordering.

2. **Orientation/cyclic input.** Construct the Joyce--Upmeier orientation cocycle on the compact/wrapped reduced sector and its \(S^1\)-equivariant negative-cyclic lift. The determinant and OP scalar square do not supply it.

3. **NO3 chain trivialization.** Exhibit \(\Theta_{\Pi,R}\), \(\Theta_{\Pi,R}^{-}\), and their quasi-isomorphisms on actual correspondence targets. The formal Picard translation formula alone is not enough.

4. **NO4 flag coherence.** Prove the two translated products agree on every finite two-step Hall flag after Hall associator and orientation transport. The lattice cocycle identity is only the degree shadow.

5. **NO5 Jacobi.** Prove the transported bracket is actually a Lie superbracket on \(H^0\) at finite stage, then compatibly in the inverse limit.

6. **NO6 Frobenius.** Supply a finite CY-\(3\) cyclic trace or equivalent Serre-functor argument for the actual Hall bracket, not an auxiliary model.

7. **NO7 Hopf radical.** Compute source-side pairing, bracket, product, coproduct, quotient, and transition matrices. The first \(W_{\le3}\) window already requires explicit radical bases and quotient maps; target signed dimensions are not enough.

8. **Closed inverse-limit radical.** Prove the finite radical kernels are transition-compatible and closed in the HN topology before passing to the completed quotient.

9. **Fibre-summed raw descent.** The current no-go excludes fixed-lift raw descent. It does not exclude a fibre-summed raw construction. If the manuscript wants to rule that out, it needs a separate theorem.

10. **Algebraic \(s_L\) target dependence.** If \(s_L\) is added, classify dependence on \(L\): torsor, groupoid of lifts, or merely a noncanonical choice. Do not call any \(L\) canonical.

11. **Compact support versus formal lattice.** Every use of \(\Gamma_X^{\mathrm{form}}\) must still be filtered through algebraic/effective support. Formal primitive lifts do not prove nonempty compact Hall moduli.

Verdict: normal ordering is the correct degree law and should be the main new formal theorem. The chain-level pushforward must be defined exactly in the finite coefficient dg/HN section, with NO1--NO7 as its verification diagrams. The manuscript is close, but the above local repairs are required before this lane is proof-grade.
