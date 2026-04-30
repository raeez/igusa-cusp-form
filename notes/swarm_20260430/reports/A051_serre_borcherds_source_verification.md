# A051 - Serre and Borcherds Relation Source Verification

## Claim Attacked

Whether `main.tex` verifies real-root Serre relations, imaginary-root
Borcherds relations, and super signs from retained compact source
brackets, rather than only from the imported target BKM algebra.

## Verdict

Not verified from retained source brackets. The manuscript correctly
imports the target Gritsenko-Nikulin/Kac BKM presentation and records
source verification as a finite-matrix recognition obligation. It
defines how source matrices would be computed from retained Hall
correspondences, but no concrete retained source bases, Hall product
matrices, coproduct matrices, pairing matrices, radical kernels, or
comparison maps are supplied.

## Failure Mode

- Target side is present: `G(\mathscr B_{\Delta_5})` is the completed
  free Lie superalgebra modulo the Borcherds-Kac ideal and GN/Kac
  radical, imported from GN/Kac; see `main.tex` near lines 12513 and
  12531. GN 1995 states the generalized Lorentzian Kac-Moody
  superalgebra correction, no odd real simple roots, and the rank-three
  matrix; GNII 1996 supplies the Part II automorphic-product context.
- Source side is conditional: the Hall representatives are required to
  satisfy BK relations in `(S4)`, but the proof explicitly consumes
  `(S4)` as the hypothesis placing `J_{\mathrm{BK}}` in the kernel; see
  `main.tex` near lines 12627 and 12823.
- Source matrix formulas exist only as a recipe from a supplied compact
  Hall source: `M,D,B,G,K,Q` are defined from compact Hall integrals and
  splittings near line 13836. The comparison to GN target brackets
  assumes parity-preserving maps `A_{\gamma,\bar p}` satisfying matrix
  equalities near line 14012.
- The determinant/product cannot prove brackets: the manuscript says
  signed multiplicities do not determine parity dimensions, brackets,
  PBW, no-extra-relations, or radical; see `main.tex` near lines 15773,
  15822, and 14867.

## Exact Constants and Relation Rows

Real simple roots are even:

```tex
((\delta_i,\delta_j)) =
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix}.
```

Hence the real-real Serre exponent is `3`:
`(\operatorname{ad} e_i)^3 e_j = 0` for `i != j`.

Primitive isotropic roots `a_{ij}=\delta_i+\delta_j` have
`\tau(a_{ij})=9`. Adjacent real roots are orthogonal, so the source must
check `[e_i,u_{ij,r}]=[e_j,u_{ij,r}]=0`. The complementary real root has
`(\delta_k,a_{ij})=-4`, so the exponent is `5`.

The first timelike root `\delta_1+\delta_2+\delta_3` has
`m=-93`, target parity `29|93`, and signed value
`29-93=-64=f(1,1)`. These are target presentation counts, not source
computations.

## Finite Source Checks Needed

For `W_{\le 3}\cup(-W_{\le 3})\cup\{0\}`, compute actual retained
source bases and matrices:

```tex
B_{\alpha,\beta}
  = M_{\alpha,\beta}
    - (-1)^{|x||y|}M_{\beta,\alpha}\tau,
\qquad
K_{\beta,\bar p}
  = \ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t}.
```

Then verify:

```tex
QB(P\otimes K)=0,\quad
QB(K\otimes P)=0,\quad
(Q\otimes Q)DK=0,\quad
M^tG=(G\otimes G)D.
```

Also verify Chevalley rows, real Serre rows, isotropic orthogonality,
odd Chevalley signs for the 93 odd `\delta_{123}` generators,
`T_1+T_2+T_3=0`, the 27 mixed maps `[e_k,u_{ij,r}]`, the kernel
equality

```tex
\ker\pi_W=(J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}})_W,
```

and the PBW associated-graded isomorphism. The finite criterion is
stated near `main.tex` line 15268; the NO7 protocol starts near line
15373.

## Critique Anchors

- A006: recognition conditional until source matrices exist.
- A010: GN target algebra imported; source citation/radical survival
  still needs tightening.
- A030: global recognition requires strict transitions, Mittag-Leffler
  control, closed radicals, and PBW strictness.
- Guide section 12 and CYQG AP-CY368/AP-CY378 agree: target arithmetic
  is not source matrices.

## Claim-Status Recommendation

Keep the manuscript at: target BK relations verified/imported in
`\mathfrak g_{\Delta_5}`; retained-source Serre/Borcherds/super-sign
verification remains conditional on finite source matrix certificates
and cofinal transition control. Do not claim source verification until
the `W_{\le3}` matrices and the height-four, height-six, and
height-seven terminal Serre rows are computed from retained geometry.

## Files Changed

None by the agent.

## Commands and Checks

Read-only `rg`, `sed`, `nl -ba`, `find`; arXiv lookup for GN/GNII source
pages. No build, no edits, no staging, no git mutation.

