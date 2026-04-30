# A036 report: associativity/coherence for local-wrapped operations

Runtime id: `019ddbe9-4e5c-7c31-ad3a-03242bc5e9f4`.
Nickname: Poincare.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Binary LL/LW/WL/WW operations plus two-step flags already assemble into
a coherent hybrid algebra/factorization object.

## Verdict

Not proved. The manuscript correctly fences the gap in the definition,
but later language risks using the object as a factorization algebra
before the colored-tree, unit, quotient, anchor, TS, and overlap
coherences are constructed.

## Local Anchors

`main.tex:7832` defines the eight two-step words and binary
associativity defects.

`main.tex:7887` explicitly says this is not full hybrid factorization.

`main.tex:8118` packages the missing higher data as
\(\mathfrak o^{\mathrm{col}}_R\).

`main.tex:13744` then calls the reduced object a "geometric hybrid
factorization algebra," but the preceding proposition supplies only
binary/flag data.

`main.tex:14263` also has the separate formal-normal-form error:
local/wrapped color is assigned by the third Gram coordinate \(m\), not
by geometric support degree.

## Exact Missing Coherence Equations

Colored-tree refinement:
\[
\alpha_{T\to T''}=\alpha_{T'\to T''}\circ \alpha_{T\to T'}
\]
for every contraction/refinement chain \(T\to T'\to T''\), plus
common-refinement independence for any two trees with the same ordered
colored leaves.

Four-input pentagon, for all colors:
\[
a_{1,2,3+4}\circ a_{1+2,3,4}
=(1\ast a_{2,3,4})\circ a_{1,2+3,4}
\circ(a_{1,2,3}\ast1).
\]

Unit equations, with unit \(\mathbf 1_R\in\mathcal F^{\mathrm{loc}}_{0,R}\):
\[
\mu^{LL}_{0,\alpha}(\mathbf1,x)=x,\quad
\mu^{LL}_{\alpha,0}(x,\mathbf1)=x,
\]
\[
\mu^{LW}_{0,\eta}(\mathbf1,y)=y,\quad
\mu^{WL}_{\eta,0}(y,\mathbf1)=y.
\]
No wrapped unit should be introduced unless separately constructed.

Mac Lane triangle:
\[
(1_\xi\ast l_\zeta)\circ a_{\xi,0,\zeta}
=r_\xi\ast1_\zeta .
\]

Anchor transport, for every binary correspondence and every tree:
\[
\Lambda_{\xi+\xi'}(C)=\Lambda_\xi(A)+\Lambda_{\xi'}(B),
\qquad
\Lambda_T=\sum_i\Lambda_{\xi_i},
\]
with \(\Lambda=\lambda\) on wrapped colors and the local
configuration/AJ anchor on local colors. This must commute with
intermediates, tree contractions, \(R'\to R\), and \(Q_{E,R}\).

Thom-Sebastiani associativity:
\[
\operatorname{TS}_{(12),3}\circ(\operatorname{TS}_{12}\boxtimes1)
=
\operatorname{TS}_{1,(23)}\circ(1\boxtimes\operatorname{TS}_{23})
\]
on each two-step flag stack, plus the same refinement equation on all
colored trees and unit identities
\[
\operatorname{TS}_{0,\xi}=\operatorname{id}=\operatorname{TS}_{\xi,0}.
\]

Quotient pseudofunctor coherence:
\[
(\phi_{g,f}\ast1)\circ\phi_{g\circ f,e}
=
(1\ast\phi_{f,e})\circ\phi_{g,f\circ e}
\]
for composable correspondences, with unit triangles and naturality for
all flag/tree \(2\)-morphisms. For associators specifically:
\[
a^{\mathrm{red}}_{123}\circ\theta^Q_{(12),3}\circ(\theta^Q_{12}\otimes1)
=
\theta^Q_{1,(23)}\circ(1\otimes\theta^Q_{23})\circ Q(a^E_{123}).
\]

Protected integration on colored trees:
\[
I_R^{\mathrm{prot}}\mu_R^T(x_1,\ldots,x_k)
=
\prod_i I_R^{\mathrm{prot}}(x_i),
\qquad
I_R^{\mathrm{prot}}(\mathbf1)=1,
\]
independent of the chosen tree/refinement and compatible with \(R'\to R\).

## Claim-Status Recommendation

Keep the binary associative Hall/module claim conditional. Do not call
the geometric object a factorization algebra, nor apply chiral Koszul
machinery to it, until \(\mathfrak o^{\mathrm{col}}_R\) is expanded into
the equations above and trivialized. Also fix the formal color rule:
local/wrapped color comes from \(b_R^{\mathrm{geom}}\), not from
\(m=\operatorname{pr}_3\overline\Pi_X\).

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, `find`, and
`git status --short`; no mutations.
