# A062 - Transition and Mittag-Leffler Control for Finite Fixtures

## Claim Attacked

Finite retained source fixtures `R' -> R` already give the completed
primitive recognition theorem by inverse limit.

## Verdict

Rejected as an unconditional claim. The manuscript proves a conditional
algebraic criterion:

```tex
\text{strict finite transitions + stable-image ML}
  \Rightarrow R^1\varprojlim=0
```

It does not prove the stable-image condition for the actual compact
source fixtures. It states it as supplied data / hypothesis.

## Exact Transition Identities

For primitive source transition matrices

```tex
T^P_{R'R,\beta,\bar p}:P^X_{R',\beta,\bar p}
  \to P^X_{R,\beta,\bar p},
```

the compact fixture must include:

```tex
T^P_{R''R}=T^P_{R'R}T^P_{R''R'},\qquad
T^P_{RR}=1.
```

Product/bracket:

```tex
T^P_{\alpha+\beta}M^{R'}_{\alpha,\beta}
  =M^R_{\alpha,\beta}(T^P_\alpha\otimes T^P_\beta),
```

hence

```tex
T^P_{\alpha+\beta}B^{R'}_{\alpha,\beta}
  =B^R_{\alpha,\beta}(T^P_\alpha\otimes T^P_\beta).
```

Coproduct:

```tex
(T^P_\mu\otimes T^P_\nu)D^{R',\mu,\nu}_{\rho}
  =D^{R,\mu,\nu}_{\rho}T^P_\rho .
```

Pairing:

```tex
G^{R'}_\beta=(T^P_\beta)^tG^R_\beta T^P_{-\beta}.
```

Radicals:

```tex
K_{R,\beta,\bar p}
  =\ker G_{R,\beta,\bar p}\cap\ker G^t_{R,-\beta,\bar p},
\qquad
T^P_{R'R,\beta,\bar p}(K_{R',\beta,\bar p})
  \subset K_{R,\beta,\bar p}.
```

With quotient maps `Q`:

```tex
Q_{\alpha+\beta}B_{\alpha,\beta}(P_\alpha\otimes K_\beta)=0,\quad
Q_{\alpha+\beta}B_{\alpha,\beta}(K_\alpha\otimes P_\beta)=0,
```

```tex
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_\rho K_\rho=0.
```

Source-to-target comparison:

```tex
A_{R,\beta}Q_{R,\beta}T^P_{R'R,\beta}
  =T^\Delta_{R'R,\beta}A_{R',\beta}Q_{R',\beta}.
```

PBW:

```tex
T^U_{R'R}(F^d_{\mathrm{PBW}}U_{R'})
  \subset F^d_{\mathrm{PBW}}U_R
```

strictly:

```tex
T^U_{R'R}(F^d_{\mathrm{PBW}}U_{R'})
  =T^U_{R'R}(U_{R'})\cap F^d_{\mathrm{PBW}}U_R.
```

No-extra-relations:

```tex
\pi_R\rho^{\mathfrak F}_{R'R}
  =T^{\mathrm{red}}_{R'R}\pi_{R'},
```

and

```tex
\ker\pi_W
  =(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}})_{\le W}
```

must commute with the HN/window transitions.

## Local Anchors

- `main.tex` near lines 5965 and 6061: target/reference tower is not
  source data.
- `main.tex` near line 6066: compact realization requires preserving
  product, coproduct, radicals, PBW, and transitions.
- `main.tex` near lines 6895 and 7018: source coalgebra transition
  square and residual.
- `main.tex` near line 7290: Koszul ML is assumed.
- `main.tex` near line 11114: finite-slice ML datum and stable images.
- `main.tex` near line 12680: primitive recognition requires closed
  radicals, no-extra-relations, PBW, and exact completion.
- `main.tex` near line 12903: cofinal finite-window datum R4-R8.
- `main.tex` near lines 14445 and 14600: conditional global theorem and
  exact-limit hypothesis.
- `main.tex` near lines 15268 and 15373: executable finite source
  criterion and `W_{\le3}` NO7 protocol.

## Proof / Failure

The manuscript proves the formal implication: once finite-dimensional
source towers, transition matrices, strict filtrations, closed radical
subsystems, and stable images are supplied, the Weibel ML criterion kills
`R^1\varprojlim`. It does not construct those source towers or prove
stable images for them. Lines 15356-15370 explicitly say the scripts
verify target arithmetic only, not source bases, pairings, radicals,
coproducts, or PBW matrices.

A030 and A053-A056 agree. A042 adds that quotient orientation is also a
transition-compatible finite Cech-Borel criterion, not a constructed
global theorem. CYQG AP-CY382 is exactly the failure mode: finite windows
do not automatically have a good limit. AP-CY384 blocks target basis
labels from becoming source bases.

## Status Recommendation

Keep the layer as: conditional finite-matrix-checkable recognition plus
conditional exact inverse-limit theorem.

Do not promote to "stable images proved" or "`R^1\varprojlim=0`
established for compact source fixtures" until actual `R' -> R` source
matrices and stable-image ranks are supplied.

## Files Changed

None by the agent.

## Commands and Checks

Read-only `sed`, `nl -ba`, `rg`; read A030, A042, A053, A054, A055,
A056; guide sections 12 and 15; CYQG AP-CY382/AP-CY384.

Ran `PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py` and
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`.
Target arithmetic passed, including `29|93`, height-four `108|90|18`,
and doubled isotropic `10|9|1`.

## Residual Obligations

Construct actual compact `W_{\le3}` source bases with provenance; compute
`M,D,B,G,K,Q,A_\beta`; verify radical ideal/coideal, Hopf adjointness,
quotient tensor nondegeneracy, PBW associated gradeds,
no-extra-relations, and transition matrices preserving radicals and PBW
strictly; then prove finite-slice stable-image ML for every source
coalgebra, bar/cobar, radical, kernel/cokernel, parity, and PBW tower.

