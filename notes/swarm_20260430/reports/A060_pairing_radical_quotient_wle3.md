# A060 - Pairing, Radical, and Quotient Matrices in W_{\le3}

## Claim Attacked

Whether the source provides pairing matrices `G`, two-sided radical
kernels `K`, complements `L`, quotient maps `Q`, quotient tensor
nondegeneracy, and stable radicals for the finite `W_{\le3}` window.

## Verdict

The manuscript supplies a finite algebraic criterion and formal matrix
recipes. It does not supply the actual compact `W_{\le3}` source
matrices.

## Local Anchors

- `main.tex` near line 9581: NO7 states the radical ideal/coideal test.
- `main.tex` near line 12680: S5 requires completed Hopf pairing and
  closed radical quotient.
- `main.tex` near line 12903: R4 requires positive-negative pairing
  matrices, kernels, coideal stability, and transitions.
- `main.tex` near line 13836: formal construction of `M,D,G,K,L,Q` from
  a compact Hall source.
- `main.tex` near line 15004: `W_{\le3}` target table and target bracket
  templates.
- `main.tex` near line 15268: finite source matrix recognition criterion.
- `main.tex` near line 15373: finite `W_{\le3}` NO7 source protocol.

## Core Formulas

```tex
K_{\beta,\bar p}
  =\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t},
\qquad
P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p},
\qquad
Q_{\beta,\bar p}=[0\ I].
```

```tex
B_{\alpha,\beta}
 =
M_{\alpha,\beta}-(-1)^{|x||y|}M_{\beta,\alpha}\tau .
```

Required descent rows:

```tex
Q_{\alpha+\beta}B_{\alpha,\beta}(P_\alpha\otimes K_\beta)=0,
\qquad
Q_{\alpha+\beta}B_{\alpha,\beta}(K_\alpha\otimes P_\beta)=0,
```

```tex
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_\rho K_\rho=0,
\qquad
M_{\alpha,\beta}^{t}G_{\alpha+\beta}
  =(G_\alpha\otimes G_\beta)D_{\alpha+\beta}^{\alpha,\beta}.
```

The quotient tensor pairing must be nondegenerate, and transition maps
must preserve `K_\beta`, PBW filtrations, pairings, and stable images.

## Finite Rows Needed

```tex
\delta_i:1|0,\quad
\delta_i+\delta_j:10|0,\quad
2\delta_i+\delta_j:1|0,\quad
\tau=\delta_1+\delta_2+\delta_3:29|93.
```

The source must provide both positive and negative blocks for these
degrees, with parity-block `G_\beta` matrices: `1 x 1`, `10 x 10`,
`1 x 1`, and `29 x 29` even plus `93 x 93` odd in degree `\tau`.

Target templates include `B_{\delta_i,\delta_j}=c_0`,
`B_{\delta_j,\delta_i}=-c_0`, adjacent simple-isotropic maps killing the
`u_{ij,r}` columns, and the 27 mixed maps `[e_k^X,u^X_{ij,r}]` into the
even `\tau` block. None are computed as compact source matrices.

## Parity and Pairing

Parity enters twice. The Pfaffian product only sees

```tex
\dim P_{\gamma,\bar0}-\dim P_{\gamma,\bar1},
```

with even vectors contributing `(1-x^\gamma)` and odd vectors
`(1-x^\gamma)^{-1}`. Primitive recognition needs the two dimensions
separately, especially `29|93`, and the pairing/radical matrices in
parity blocks.

Positive-negative pairing is separate from cusp-positive Pfaffian
support: negative representatives belong to the BKM double and are
tested only through primitive recognition and the matrices
`G_\beta:P_\beta x P_{-\beta}->C`.

## Guide and Report Alignment

- Guide section 12 says `M,D,B,G,K,Q,A_\beta` are source data, not target
  arithmetic.
- Guide section 15 keeps the retained theorem conditional on matrix and
  transition identities.
- A030, A049, A053, A054, A055, and A056 agree: conditional criterion,
  no compact source certificate yet.
- CYQG AP-CY382 requires strict transitions and `R^1 lim=0`; AP-CY384
  forbids treating target bases as source bases.

## Claim-Status Recommendation

Keep `W_{\le3}` primitive recognition as a finite-matrix-checkable
conditional criterion. Do not state that the compact source provides
`G,K,L,Q`, quotient tensor nondegeneracy, stable radicals, PBW, or
no-extra-relations until actual retained source bases and matrices are
inscribed.

## Files Changed

None by the agent.

## Commands and Checks

Read-only `rg`, `sed`, `nl`, `wc`, `git status --short`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`.

## Residual Obligation

Construct the compact `W_{\le3}\cup(-W_{\le3})\cup\{0\}` source fixture
with provenance for every basis vector, compute `M,D,B,G,K,L,Q,A_\beta`,
verify `QB`, `QD`, Hopf adjointness, quotient tensor nondegeneracy,
kernel equality, PBW associated gradeds, and strict transition/ML
closedness.

