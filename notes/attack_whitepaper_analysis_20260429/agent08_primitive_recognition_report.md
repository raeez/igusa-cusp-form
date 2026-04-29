# Agent 08 Primitive Recognition / PBW / Hopf Radical Report

Scope: primitive Hall bracket, normal-ordered pushforward, BKM recognition
certificate, no-extra-relations, PBW compatibility, Hopf
pairing/coproduct/radical matrices, \(W_{\le3}\), NO7, first timelike
presentation count, and the rule that the determinant does not determine
brackets.

Status: the current manuscript has mostly healed the old overclaim.  It now
treats primitive recognition as a certificate and open compact source problem,
not as a theorem constructing compact \(K3\times E\) Hall geometry.  The
remaining mathematical burden is finite source data: representatives, bracket
matrices, pairing/coproduct matrices, radical kernels, no-extra-relations, PBW
associated gradeds, and transition exactness.

## Required certificate data

The source primitive object must be
\[
P_X^\Pi
=H^0\Prim_{\mathrm{prot}}
(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)
\]
or its completed radical quotient, not the target current envelope and not the
determinant.  The compact source first lives upstairs over
\(\widehat\Gamma_X=\Gamma_X^{\mathrm{phys}}\oplus_B\Gamma_{\mathrm{gram}}\),
with bracket
\[
[\widetilde P_{X,\widehat c},\widetilde P_{X,\widehat c'}]
\subset \widetilde P_{X,\widehat c\star\widehat c'}.
\]
The descended primitive algebra is \(\Gamma_{\mathrm{gram}}\)-graded only after
the chain-level normal-ordered pushforward
\(\overline\Pi_{X,*}^{\Theta}\).  Current anchors:
`main.tex:12170-12224`, `main.tex:12043-12048`.

The recognition certificate must contain:

1. Cartan and degree matching:
\[
P^{\Pi,\mathrm{red}}_{X,0}\simeq \Lambda^{2,1}_{II}\otimes\mathbb C,
\qquad
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}.
\]

2. Parity-homogeneous compact representatives for all real and imaginary
simple-root fibres, including the negative primitive half.

3. Relation checks in the protected Hall bracket: Chevalley, real Serre,
Borcherds orthogonality, super signs, and the low-degree relations involving
the primitive isotropic fibres \(u_{ij,r}\).

4. Generation by Cartan plus simple primitives.

5. A completed positive-negative Hopf pairing, compatible coproduct, and a
closed homogeneous radical which is both a Lie ideal and a coideal.

6. A no-extra-relations theorem:
\[
\ker \pi
=\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}}.
\]

7. Completed PBW compatibility: finite-window associated graded PBW maps are
isomorphisms and transition maps preserve the PBW filtration strictly.

8. Exact triangular completion: closed images, strict HN transitions,
vanishing \(\lim^1\), and compatibility of finite kernels, radicals,
cokernels, PBW associated gradeds, and parity pieces.

9. Full parity dimensions, not only signed superdimensions.  In the first
timelike channel \((1,1,1)\), the source must match \(29|93\), not only
\(-64\).

Current anchors: `main.tex:12105-12120`, `main.tex:12226-12429`,
`main.tex:12479-12588`, `main.tex:14180-14192`.

## Current theorem tautologies

The attack transcript correctly said that the earlier primitive recognition
theorem was nearly tautological: it assumed oriented Hall data, protected
integration, primitive representatives, parity split, all defining relations,
no-extra-relations, completed PBW, the same radical quotient, and full parity
dimensions, then concluded \(P_X^\Pi\simeq\mathfrak g_{\Delta_5}\).  Attack
anchor: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:448-485`.

The current manuscript has converted that defect into honest status.  The
theorem is now titled "Primitive recognition certificate; no source
construction" and states that none of its source-side data is inferred from the
Borcherds product, determinant, or signed dimensions alone.  Current anchors:
`main.tex:12124-12193`, `main.tex:12448-12476`.

The tautological clauses are now visible and acceptable as certificate clauses:

- `(S5)` assumes the Hopf radical quotient agrees with the
  Gritsenko--Nikulin/Kac radical; this is exactly the quotient theorem.
- `(S6)` assumes the kernel equality; this is exactly injectivity.
- `(S8)` assumes PBW associated graded compatibility; this is exactly the
  filtered enveloping-algebra comparison.
- `(S9)` assumes exact completion; this is exactly the passage from finite
  windows to the completed theorem.
- `(S10)` assumes full parity dimensions; this is exactly what blocks the
  zero-superdimension and cancelling-pair determinant counterexamples.

Thus the theorem is not an existence theorem.  It is a checklist whose proof is
the universal property of the Borcherds--Kac presentation plus the supplied
finite Hopf/PBW/no-extra-relations data.  This framing is correct.

## Exact finite tests

### Normal-ordered pushforward

The degree correction is now a proved lattice statement:
\[
(c,T)\star(c',T')=(c+c',T+T'+B(c,c')),
\qquad
\overline\Pi_X(c,T)=\Pi_X(c)-T,
\]
and \(\overline\Pi_X\) is additive.  Raw fixed-lift \(\Pi_X\)-descent cannot
realize the type-II real-root strings because it would force
\[
B(c_i,c_j)=0,\qquad
B(c_i,c_i+c_j)=B(c_i,c_i)+B(c_i,c_j)=2\Pi_X(c_i)\ne0.
\]
Current anchors: `main.tex:4614-4810`, `main.tex:4832-4975`.

At chain level, the finite tests are NO1--NO7.  NO1 checks finite fibres and
transition compatibility.  NO2 checks product, coproduct, and pairing
transitions.  NO3 checks Hochschild and negative-cyclic equations.  NO4 checks
two-step Hall flag coherence.  NO5 checks Jacobi.  NO6 checks Frobenius.  NO7
checks the Hopf radical as Lie ideal plus coideal.  Current anchor:
`main.tex:9132-9319`.

### NO7 matrix test

For each retained finite window, choose homogeneous bases and write:
\[
G_\beta:P^\Pi_{R,\beta}\times P^\Pi_{R,-\beta}\to\mathbb C,\quad
K_\beta=\ker G_\beta\cap\ker G_{-\beta}^t,\quad
Q_\beta:P^\Pi_{R,\beta}\to P^\Pi_{R,\beta}/K_\beta.
\]
Let \(B_{\alpha,\beta}\) be bracket matrices, \(M_{\alpha,\beta}\) product
matrices, and \(D^\mu_{\rho,\nu}\) coproduct matrices.  The finite source must
verify:
\[
Q_{\alpha+\beta}B_{\alpha,\beta}(P^\Pi_{R,\alpha}\otimes K_\beta)=0,
\]
\[
Q_{\alpha+\beta}B_{\alpha,\beta}(K_\alpha\otimes P^\Pi_{R,\beta})=0,
\]
\[
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_\rho K_\rho=0,
\]
plus Hopf adjointness
\[
\langle M_{\alpha,\beta}(x\otimes y),z\rangle_R
=
\langle x\otimes y,D^{\alpha,\beta}_{\alpha+\beta}z\rangle_R,
\]
quotient-tensor nondegeneracy, and transition preservation of radical
kernels.  Current anchors: `main.tex:9236-9301`, `main.tex:9397-9438`,
`main.tex:13205-13274`.

### \(W_{\le3}\) recognition window

The first downward-saturated test window is
\[
W_{\le3}=\{\beta=c_1\delta_1+c_2\delta_2+c_3\delta_3:
c_i\ge0,\ 1\le c_1+c_2+c_3\le3\}.
\]
The target parity dimensions are:
\[
\delta_i:1|0,\qquad
\delta_i+\delta_j:10|0,\qquad
2\delta_i+\delta_j:1|0,\qquad
\delta_{123}:29|93.
\]
Current anchor: `main.tex:12941-12968`.

The compact source must supply, on
\(W_{\le3}\cup(-W_{\le3})\cup\{0\}\):
representatives, Chevalley/Serre/orthogonality/super-sign relations, the
Jacobi relation \(T_1^X+T_2^X+T_3^X=0\), the \(27\) mixed maps
\([e_k^X,u^X_{ij,r}]\), positive-negative pairing matrices, closed radical
kernels, finite kernel equality, and associated-graded PBW isomorphism.
Current anchors: `main.tex:12969-13083`, `main.tex:13205-13274`.

### First timelike presentation count

Verified locally by `python3 compute/verify_square_root.py`.  The script
prints:

- \([qrs]\,64^{-1}\Delta_5/(qrs)^{1/2}=93\).
- first timelike target split \(29|93\).
- \(m(\delta_1+\delta_2+\delta_3)=-93\).
- height-four timelike signed/additive/gap checks \(108|90|18\).
- doubled isotropic signed/simple/gap checks \(10|9|1\).

Script anchors: `compute/verify_square_root.py:401-438`,
`compute/verify_square_root.py:447-468`.  Manuscript anchors:
`main.tex:12712-12802`, `main.tex:12838-12939`,
`main.tex:13085-13203`.

The count is target-side only.  It is not a compact Hall computation.  The
compact source must produce \(29\) even and \(93\) odd source primitives in
degree \((1,1,1)\), the corresponding bracket coordinates, the pairing
matrix, radical kernel, quotient map, and PBW finite-window comparison.

### Determinant forgetfulness

The determinant sees only the class in
\[
K_0(\Gamma_{\mathrm{eff}}\text{-graded finite super vector spaces}).
\]
A graded super vector space with the same signed dimensions and zero bracket
has the same determinant but the wrong Lie algebra.  Adding
\(M\oplus\Pi M\) changes parity dimensions, possible brackets, and radicals
without changing the signed determinant.  Current anchors:
`main.tex:12804-12836`, `main.tex:13652-13699`.  Attack anchors:
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:640-688`,
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:15676-15688`.

## Replacement theorem language

The safe theorem language is:

**Normal-ordered charge theorem.**  The group
\(\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}}\)
and homomorphism \(\overline\Pi_X(c,T)=\Pi_X(c)-T\) provide the additive
degree bridge from any supplied compact Hall source to the Igusa Gram degrees.
Raw fixed-lift \(\Pi_X\)-descent cannot realize the full BKM real-root
strings.

**Primitive recognition certificate; no source construction.**  If a compact
Hall/factorization source supplies the normal-ordered primitive Lie
superalgebra, primitive representatives, relations, Hopf pairing, closed
radical quotient, no-extra-relations, completed PBW, exact completion, and full
parity dimensions, then its normal-ordered primitive radical quotient is
\(\mathfrak g_{\Delta_5}\).  This is a certificate theorem, not a construction
of the compact source.

**Finite-window recognition certificate.**  A global recognition proof is
equivalent to a cofinal system of downward-saturated finite certificates.  On
each \(W_\nu\), the source must provide representatives, relation checks,
pairing matrices, radical kernels, finite kernel equality, generation, PBW
associated-graded isomorphism, and exact triangular completion.

**NO7 finite Hopf-radical test.**  The radical quotient is available only when
the finite radical blocks are stable under bracket, coideal for coproduct,
nondegenerate after quotient, and preserved by transition maps.  A determinant
or target table cannot supply these matrices.

Avoid theorem titles or prose that imply:

- signed root multiplicity determines primitive Hall states;
- the denominator algebra constructs a compact Hall source;
- target PBW transfers to the compact source;
- equality of radicals follows from equality of ranks;
- the target current envelope supplies the source coalgebra;
- a determinant identity is a bracket theorem.

## Current anchors

- First-page primitive-recognition caveat:
  `main.tex:260-296`.
- Formal normal-ordered degree theorem and raw-descent no-go:
  `main.tex:4312-4382`, `main.tex:4614-4810`, `main.tex:4832-4975`.
- Normal-ordering coefficient dg category:
  `main.tex:8348-8405`.
- Finite normal-ordering diagrams NO1--NO7:
  `main.tex:9132-9319`.
- Finite normal-ordering closure criterion N1--N7:
  `main.tex:9654-9722`.
- Dirac--Igusa certificate levels:
  `main.tex:11750-12122`.
- Primitive recognition certificate theorem:
  `main.tex:12124-12476`.
- Cofinal finite-window certificate:
  `main.tex:12479-12631`.
- Low-degree bracket information:
  `main.tex:12633-12802`.
- Determinant does not determine compact Hall constants:
  `main.tex:12804-12836`.
- First timelike presentation count:
  `main.tex:12838-12939`.
- First saturated \(W_{\le3}\) window:
  `main.tex:12941-13203`.
- Finite \(W_{\le3}\) NO7 source protocol:
  `main.tex:13205-13274`.
- State-side construction open problem:
  `main.tex:13276-13414`.
- What the determinant forgets:
  `main.tex:13652-13699`.
- Claim-strength synthesis:
  `main.tex:14031-14265`.
- Primary bibliography anchors:
  Kac 1990 at `proj.bib:47-52`; Gritsenko--Nikulin 1997 at
  `proj.bib:100-110`; Gritsenko--Nikulin I/II 1998 at
  `proj.bib:112-134`; Kontsevich--Soibelman CoHA 2011 at
  `proj.bib:311-321`; Beilinson--Drinfeld 2004 and Francis--Gaitsgory 2012
  for chiral/Koszul language at `proj.bib:61-78`.

## Residual computations/actions

1. No edit to `main.tex` is needed for this lane before integration.  The
current manuscript already carries the certificate-not-construction language.

2. The compact source matrices remain unconstructed.  The first concrete
source computation is the \(W_{\le3}\) certificate: compact \(29|93\) bases in
\(\delta_{123}\), the \(27\) mixed maps, Jacobi/Serre checks, positive-negative
pairing matrices, coproduct matrices, radical kernels, quotient maps, and PBW
associated-graded comparison.

3. The NO7 obstruction is the sharp residual.  A source can match the quotient
target bracket table on \(W_{\le3}\) and still fail if
\[
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_\rho(k)\ne0
\qquad(k\in K_\rho).
\]
This must be checked on source matrices, not inferred from signed dimensions.

4. The attack transcript suggests an optional universal algebraic
normal-ordered lift \(s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)\) and an
algebraic \(\widehat\Gamma_X\)-graded lift of
\(\mathfrak g_{\Delta_5}\).  Attack anchors:
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:15944-16158`,
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:24325-24340`.
`main.tex` does not currently include an \(s_L\) theorem.  This is optional:
it would give a non-geometric algebraic comparison target, but it would not
construct compact Hall geometry.

5. Commands run:
`python3 compute/verify_square_root.py` passed and verified \(29|93\), the
height-four \(108|90|18\) gaps, doubled isotropic \(10|9|1\), and real-string
exponents.  `python3 compute/verify_lattice.py` passed and verified the
type-II Gram matrix and Weyl vector.
