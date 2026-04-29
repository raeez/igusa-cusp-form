# Agent 27 Report: \(W_{\le3}\), \(\delta_{123}\), and the Source-Proof Gap

Scope: aggressive audit of the finite window \(W_{\le3}\), the first
timelike primitive degree \(\delta_{123}\), the target dimensions \(29|93\),
signed multiplicities, and the missing compact source proof.  Sources mined:
current `main.tex`, `compute/verify_square_root.py`,
`compute/verify_lattice.py`, `proj.bib`, the 2026-04-29 attack PDF text, and
prior primitive-recognition/PBW reports.

## Stable target arithmetic

Status: computed target arithmetic is stable.  It is target arithmetic only.

1. The local coefficient engine `python3 compute/verify_square_root.py`
   passed.  It prints:
   \[
   [qrs]\,D_5/(qrs)^{1/2}=93,
   \]
   the Laurent check
   \[
   A(B^2+C)=9r^{-3}-93r^{-2}+90r^{-1}-90+93r-9r^2,
   \]
   the first timelike target split \(29|93\), and
   \[
   m(\delta_1+\delta_2+\delta_3)=-93.
   \]
   Script anchors: `compute/verify_square_root.py:352-361`,
   `compute/verify_square_root.py:401-411`, `compute/verify_square_root.py:433-438`.

2. The first timelike degree is
   \[
   \delta_{123}:=\delta_1+\delta_2+\delta_3=2f_2-f_3+2f_{-2}.
   \]
   In the Weyl-sum coefficient convention it is
   \[
   (3-1)f_2-\frac{3-1}{2}f_3+(3-1)f_{-2}.
   \]
   Thus \(m(\delta_{123})=-64^{-1}c_\Delta(3,3,3)=-93\).
   Manuscript anchors: `main.tex:12838-12915`.

3. The target presentation split is:
   \[
   \rootmult_{\overline0}(\delta_{123})=29,\qquad
   \rootmult_{\overline1}(\delta_{123})=93.
   \]
   The even part is not a mystery number:
   \[
   29=2+3\cdot9.
   \]
   The \(2\) is the multidegree \((1,1,1)\) Witt dimension for the free Lie
   algebra on the three even real generators, represented by the three
   bracketings \(T_1,T_2,T_3\) modulo the single Jacobi relation
   \(T_1+T_2+T_3=0\).  The \(27\) is the three complementary real-isotropic
   families \([e_k,u_{ij,r}]\), with \(1\le r\le9\).  The \(93\) odd part is
   the negative-norm imaginary simple-root fibre in degree \(\delta_{123}\).
   Manuscript anchors: `main.tex:12854-12868`, `main.tex:12917-12938`.

4. The signed product exponent check is:
   \[
   29-93=-64=f(1,1)=\smult(\delta_{123}).
   \]
   This equality is a consistency check between the GN/Kac target
   presentation and the Borcherds product exponent.  It is not the source of
   the parity split.

5. The \(W_{\le3}\) target table is internally consistent:
   \[
   \delta_i:1|0,\qquad
   \delta_i+\delta_j:10|0,\qquad
   2\delta_i+\delta_j:1|0,\qquad
   \delta_{123}:29|93.
   \]
   Manuscript anchors: `main.tex:12941-12968`.

6. The root-string constants are stable.  The script prints
   `real_real_pairing=-2`, `real_real_exponent=3`,
   `complement_isotropic_pairing=-4`, `complement_isotropic_exponent=5`,
   `timelike_delta123_pairing=-2`, and
   `timelike_delta123_exponent=3`.  These constants support the real Serre
   exponents and the height-four obstruction.  Script anchors:
   `compute/verify_square_root.py:236-254`,
   `compute/verify_square_root.py:305-321`,
   `compute/verify_square_root.py:459-468`.

7. The next target checks already show why height four cannot be certified by
   additive coefficients alone:
   \[
   m(2\delta_1+\delta_2+\delta_3)
   =m(\delta_1+2\delta_2+\delta_3)
   =m(\delta_1+\delta_2+2\delta_3)=90,
   \]
   but the signed root supermultiplicity in each degree is \(108\), leaving
   signed residual \(18\).  Also
   \[
   \smult(2\delta_i+2\delta_j)=10,\qquad \tau(2(\delta_i+\delta_j))=9,
   \]
   leaving residual \(1\) on doubled isotropic rays.  Manuscript anchors:
   `main.tex:13085-13203`.

8. The lattice script `python3 compute/verify_lattice.py` passed.  It checks
   the type-II simple-root Gram matrix
   \[
   \begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}
   \]
   and \(\rho=(1,-1/2,1)\).  Script anchors:
   `compute/verify_lattice.py:92-125`.

## Current manuscript anchors

The manuscript now has the right logical firewall.  It should be preserved.

1. The imported GN/Kac target is explicit.  The denominator algebra is the
   automorphic correction with real simple roots
   \(\delta_1,\delta_2,\delta_3\), imaginary simple-root data \(m(a)\) and
   \(\tau(a)\), and signed root supermultiplicities on active support.
   Anchors: `main.tex:5527-5542`, `main.tex:5560-5702`.

2. Primitive recognition is now a certificate, not an existence theorem.
   Its assumptions (S1)--(S10) require normal-ordered descent, Cartan/root
   matching, simple representatives and parities, Borcherds--Kac relations,
   completed Hopf pairing and radical quotient, no-extra-relations,
   generation, completed PBW, exact completion, and full parity dimensions.
   Anchors: `main.tex:12124-12476`.

3. The cofinal finite-window certificate is explicit.  It requires finite
   representatives, relation checks, two-integer parity dimensions,
   positive-negative pairing matrices, radical kernels, finite kernel
   equality, finite generation, PBW associated-graded isomorphism, and exact
   triangular completion.  Anchors: `main.tex:12479-12588`.

4. Low-degree bracket information is target-side and correctly says so.  It
   names the first unresolved compact test: produce \(29\) even and \(93\)
   odd compact primitives in degree \((1,1,1)\), compute the Hall constants
   for \([e_k^X,u^X_{ij,r}]\), impose Jacobi and real-string relations, and
   construct the Hopf-pairing matrix and radical quotient.  Anchors:
   `main.tex:12633-12802`.

5. The first timelike count is target-side and is not deduced from
   \(29-93=-64\).  Anchors: `main.tex:12838-12939`.

6. The first saturated target window \(W_{\le3}\) and its finite certificate
   are stated.  Anchors: `main.tex:12941-13203`.

7. The finite \(W_{\le3}\) NO7 source protocol is the right source-side
   matrix statement.  Anchors: `main.tex:13205-13274`.

8. The manuscript states what the denominator determines and forgets: signed
   integers only, not parity dimensions, structure constants, simple
   primitive representatives, no-extra-relations, completed PBW, or the
   closed Hopf radical.  Anchors: `main.tex:13603-13650`,
   `main.tex:13652-13699`.

9. The attack PDF makes the same hostile point.  It says the old primitive
   recognition theorem was nearly tautological because it assumed primitive
   representatives, parity split, relations, no-extra-relations, completed
   PBW, same radical quotient, and full parity dimensions before concluding
   the isomorphism.  It also gives the zero-bracket counterexample.
   Attack anchors:
   `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:448-485`,
   `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:631-673`,
   `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:15141-15145`,
   `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:15676-15680`.

## What \(29|93\) does and does not prove

What it proves, in the fixed target:

1. It proves the first timelike parity split inside the imported
   Gritsenko--Nikulin/Kac presentation, after using the Weyl-sum additive
   coefficient \(m(\delta_{123})=-93\), the isotropic multiplicity
   \(\tau(a_{ij})=9\), the real-root Jacobi relation, and PBW for the target
   presentation.

2. It proves that the signed exponent \(-64\) is not enough even in the
   first nontrivial timelike degree.  The target has \(29\) even and \(93\)
   odd directions, not just a virtual dimension.

3. It proves the source will be tested first in degree \((1,1,1)\), because
   this is where product exponents, simple-root additive coefficients, lower
   bracket words, parity, and radical/PBW data first collide.

What it does not prove:

1. It does not exhibit compact primitive vectors
   \(v^{\overline0}_1,\ldots,v^{\overline0}_{29}\) and
   \(v^{\overline1}_1,\ldots,v^{\overline1}_{93}\) in
   \(P^{\Pi,\mathrm{red}}_{X,(1,1,1)}\).

2. It does not compute any compact Hall structure constants
   \(C^{\overline0}_{k;ijr,a}\) for
   \[
   [e_k^X,u^X_{ij,r}]
   =\sum_{a=1}^{29}C^{\overline0}_{k;ijr,a}v^{\overline0}_a.
   \]

3. It does not prove the compact Jacobi relation
   \(T_1^X+T_2^X+T_3^X=0\), the real-string relations, or the
   orthogonality relations in the source bracket.

4. It does not construct the positive-negative Hopf pairing in degree
   \(\pm\delta_{123}\), its parity blocks, its radical kernel, or the quotient
   map.

5. It does not prove that the source radical equals the GN/Kac radical.  It
   does not prove that the radical is a Lie ideal and a coideal.

6. It does not prove no-extra-relations:
   \[
   \ker\pi_{W_{\le3}}
   =
   \bigl(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}}
   \bigr)_{W_{\le3}}.
   \]

7. It does not prove PBW compatibility for the compact source.  Target PBW is
   already part of the imported GN/Kac algebra; transferring it to compact
   Hall primitives is exactly the missing theorem.

8. It cannot distinguish the target algebra from a graded super vector space
   with the same signed dimensions and zero bracket.  It also cannot detect
   adding \(M\oplus\Pi M\) cancelling pairs.  Therefore no source data can be
   inferred from \(29|93\), and still less from \(-64\).

## Required compact source data

For the first real test, the compact source must supply data on
\[
W_{\le3}\cup(-W_{\le3})\cup\{0\}.
\]
This is \(13\) positive root degrees, their \(13\) negatives, and the Cartan
degree.

Required finite source package:

1. Degree labels and parity-homogeneous primitive bases for every retained
   positive and negative degree:
   \[
   \delta_i,\quad a_{ij}=\delta_i+\delta_j,\quad
   2\delta_i+\delta_j,\quad \delta_{123},
   \]
   with Cartan basis in degree \(0\).  The degree
   \(\delta_{123}\) must have source quotient dimensions \(29|93\), not only
   signed dimension \(-64\).

2. Real simple representatives \(e_i^X,f_i^X,h_i^X\) for \(i=1,2,3\).

3. Isotropic simple representatives
   \(u^{+,X}_{ij,r}\in P^X_{a_{ij}}\) and
   \(u^{-,X}_{ij,r}\in P^X_{-a_{ij}}\), \(1\le r\le9\), plus the
   real-real commutator direction \(E_{ij}^X=[e_i^X,e_j^X]\).

4. Odd negative-norm simple representatives \(w_s^X\), \(1\le s\le93\), in
   degree \(\delta_{123}\), and the negative-half representatives in
   \(-\delta_{123}\).

5. Bracket matrices for all ordered decompositions retained by the window:
   \[
   a_{ij}=\delta_i+\delta_j=\delta_j+\delta_i,
   \]
   \[
   2\delta_i+\delta_j=\delta_i+a_{ij}=a_{ij}+\delta_i,
   \]
   and
   \[
   \delta_{123}
   =\delta_1+a_{23}
   =\delta_2+a_{13}
   =\delta_3+a_{12},
   \]
   with the corresponding reversed ordered maps and signs.

6. Source versions of the target templates:
   \[
   B_{\delta_i,\delta_j}=c_0,\qquad
   B_{\delta_j,\delta_i}=-c_0,
   \]
   adjacent simple-isotropic maps killing the \(u_{ij,r}\)-columns, and
   complementary maps landing in the even \(\delta_{123}\)-block.  The target
   templates are anchors, not source computations.

7. Positive-negative Hopf-pairing matrices in every retained degree, radical
   kernel bases, quotient maps, and proof that the kernels are preserved by
   finite transitions.

8. Product matrices and coproduct matrices for every retained decomposition,
   or equivalent Hopf-adjointness data.

9. Finite no-extra-relations and PBW associated-graded comparison:
   the compact finite presentation map must have exactly the GN/Kac kernel,
   and the PBW filtration must match on associated gradeds in the finite
   window.

10. Exact triangular completion data, even for this first window if it is to
    be embedded in the cofinal global argument.

## NO7/PBW matrix checklist

For each retained degree \(\beta\), choose parity-homogeneous source bases
and write:
\[
G_\beta:P^\Pi_{R,\beta}\times P^\Pi_{R,-\beta}\to\mathbb C,
\qquad
K_\beta=\ker G_\beta\cap\ker G_{-\beta}^{t},
\]
\[
Q_\beta:P^\Pi_{R,\beta}\to P^\Pi_{R,\beta}/K_\beta.
\]
For each retained ordered pair \((\alpha,\beta)\), write bracket and product
matrices \(B_{\alpha,\beta}\), \(M_{\alpha,\beta}\).  For each retained
decomposition \(\rho=\mu+\nu\), write coproduct matrices
\[
D^{\mu,\nu}_{\rho}:P^\Pi_{R,\rho}\to
P^\Pi_{R,\mu}\otimes P^\Pi_{R,\nu}.
\]

The finite \(W_{\le3}\) NO7 check is the following matrix list.

1. Lie-ideal radical containment:
   \[
   Q_{\alpha+\beta}B_{\alpha,\beta}
   (P^\Pi_{R,\alpha}\otimes K_\beta)=0,
   \]
   \[
   Q_{\alpha+\beta}B_{\alpha,\beta}
   (K_\alpha\otimes P^\Pi_{R,\beta})=0.
   \]

2. Coideal radical containment:
   \[
   (Q_\mu\otimes Q_\nu)D^{\mu,\nu}_{\rho}K_\rho=0.
   \]

3. Frobenius/Hopf adjointness:
   \[
   \langle M_{\alpha,\beta}(x\otimes y),z\rangle_R
   =
   \langle x\otimes y,D^{\alpha,\beta}_{\alpha+\beta}z\rangle_R.
   \]

4. Quotient-tensor nondegeneracy for every retained tensor pairing
   \(\bar G_\mu\otimes\bar G_\nu\).

5. Transition preservation:
   \[
   \rho^P_{R^+R}(K_{R^+,\beta})\subset K_{R,\beta}.
   \]

6. Jacobi in the finite source, including
   \[
   T_1^X+T_2^X+T_3^X=0.
   \]

7. Borcherds--Kac relation matrix tests for the real Serre, isotropic
   orthogonality, Chevalley, and super-sign relations.

8. No-extra-relations kernel equality in the window:
   \[
   \ker\pi_{W_{\le3}}
   =
   \bigl(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}}
   \bigr)_{W_{\le3}}.
   \]

9. PBW associated-graded isomorphism:
   \[
   \operatorname{gr}_{\mathrm{PBW}}U(P_X^{\Pi,\mathrm{red}})_{W_{\le3}}
   \xrightarrow{\sim}
   \operatorname{gr}_{\mathrm{PBW}}U(\mathfrak g_{\Delta_5})_{W_{\le3}}.
   \]

Any one missing matrix kills source recognition.  Dimension equality does not
substitute for any of these checks.

## Suggested executable fixtures

No source fixture currently exists.  The existing scripts verify target
coefficients and target lattice arithmetic only.  A compact source proof needs
new executable data, not more product coefficients.

Suggested fixtures:

1. `compute/fixtures/wle3_target.json`
   - degree labels in the \(\delta\)-basis and \((n,l,m)\)-basis;
   - target parity dimensions;
   - ordered decompositions;
   - target bracket templates for \(B_{\delta_i,\delta_j}\),
     adjacent simple-isotropic maps, and complementary maps;
   - target root-string exponents.

2. `compute/fixtures/wle3_source_schema.json`
   - source basis IDs by degree and parity;
   - source-to-target quotient map \(Q_\beta\);
   - positive-negative pairing matrices \(G_\beta\);
   - radical bases \(K_\beta\);
   - bracket matrices \(B_{\alpha,\beta}\);
   - product matrices \(M_{\alpha,\beta}\);
   - coproduct matrices \(D^{\mu,\nu}_{\rho}\);
   - transition matrices \(\rho^P_{R^+R}\);
   - PBW word ordering and expected associated-graded ranks.

3. `compute/verify_wle3_target.py`
   - reproduces the \(W_{\le3}\) table from `verify_square_root.py`;
   - prints the \(13\) positive degrees and all ordered decompositions;
   - asserts the \(29|93\) split and the root-string exponents;
   - has no source-recognition claims.

4. `compute/verify_wle3_no7.py`
   - consumes a source fixture;
   - checks the \(QB\), \(QD\), Frobenius/Hopf-adjointness,
     quotient-nondegeneracy, and transition-preservation equations;
   - fails on a fixture with correct dimensions and zero bracket;
   - fails on a fixture where \(k\in K_\rho\) has
     \((Q_\mu\otimes Q_\nu)D^{\mu,\nu}_{\rho}k\ne0\).

5. `compute/verify_wle3_pbw.py`
   - consumes a source fixture and target fixture;
   - constructs the finite presentation map;
   - checks finite kernel equality against the listed BK/radical relations;
   - compares associated graded PBW ranks and transition strictness.

6. A negative fixture should be committed with the verifier when the source
   harness is built: correct signed dimensions, correct \(29|93\), and zero
   bracket.  It must fail.  That failure is the regression guard against
   determinant-only recognition.

## Patch queue

No source file was edited by this agent.  The following patches are the next
useful queue, in order.

1. Add a target-only \(W_{\le3}\) table mode to the compute harness.  It
   should print the \(13\) positive degrees, target parity dimensions,
   ordered decompositions, \(29|93\), height-four residuals, and root-string
   exponents in one canonical output.  This is a reporting patch, not a
   mathematical proof patch.

2. Add a source-fixture schema and NO7 verifier.  Without this, the manuscript
   has a good checklist but no executable source test.

3. Add a PBW finite-window verifier once the bracket and radical matrices
   exist.  The PBW verifier must consume matrices; it must not regenerate a
   proof from target dimensions.

4. In prose, keep every occurrence of \(29|93\) tied to "target presentation
   count" or "GN/Kac target parity dimensions."  Never let it drift into
   "compact Hall count" unless the source fixture has been supplied and
   verified.

5. Preserve the attack-PDF counterexample in the manuscript spine: same signed
   dimensions plus zero bracket gives the same determinant and the wrong
   algebra.  This is the simplest reader-facing defense against the
   determinant shortcut.

6. If future compression moves material to an appendix, do not move the
   source/target firewall.  The first timelike arithmetic can be compact, but
   the statement "target data do not imply source recognition" must remain in
   the main proof spine.

## Residual open proof

The remaining theorem is not coefficient arithmetic.  It is the following
source construction.

Construct a finite compact Hall stage \(R\) whose normal-ordered descended
primitive quotient contains \(W_{\le3}\cup(-W_{\le3})\cup\{0\}\), with
parity-homogeneous bases, source primitive representatives, bracket matrices,
product/coproduct matrices, positive-negative Hopf-pairing matrices, radical
kernels, quotient maps, and transition maps.  Prove the Borcherds--Kac
relations, the \(27\) mixed maps into the even \(\delta_{123}\)-block, the
Jacobi relation, the real-string relations, the NO7 ideal/coideal equations,
finite no-extra-relations, and PBW associated-graded compatibility.

Then prove these finite data sit in a cofinal exact triangular system: closed
radicals, strict transitions, no new inverse-limit relations, no hidden
zero-superdimension summands, and vanishing of the relevant \(\lim^1\) terms.

Until that source package exists, the strongest honest statement is:

\[
\text{GN/Kac target arithmetic on }W_{\le3}\text{ is verified;}
\]
\[
\text{compact primitive recognition on }W_{\le3}\text{ remains open.}
\]

The number \(29|93\) is the first sharp target that a compact source must hit.
It is not evidence that the compact source has been constructed.
