# A064 - PBW Associated-Graded Rank Checks in W_{\le3}

## Claim Status

`CONDITIONAL / NOT PROVED AS COMPACT SOURCE THEOREM`.

The manuscript correctly treats PBW for `W_{\le3}` as a finite
source-to-target recognition obligation, not as a consequence of target
arithmetic or radical descent. Ordinary PBW is proved only in the formal
sense: once a finite-dimensional Lie superalgebra quotient exists,
`gr_PBW U(L) = Sym(L_0) \otimes Lambda(L_1)`. The needed theorem is
stronger: the compact source quotient must have PBW associated gradeds
isomorphic to the GN/Kac target quotient.

## Required Data

Finite window:

```tex
W_{\le3}=
\{c_1\delta_1+c_2\delta_2+c_3\delta_3:
c_i\ge0,\ 1\le c_1+c_2+c_3\le3\}.
```

Target parity blocks:

```tex
\delta_i:1|0,\quad
a_{ij}=\delta_i+\delta_j:10|0,\quad
2\delta_i+\delta_j:1|0,\quad
\tau=\delta_1+\delta_2+\delta_3:29|93.
```

Positive total: `68|93`. Full double with Cartan: `139|186`.

Source quotient:

```tex
K_{\beta,\bar p}
  =\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t},\qquad
P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p},\qquad
Q_{\beta,\bar p}=[0\ I].
```

Target quotient:

```tex
G(\mathscr B_{\Delta_5})_{\le W}
 =
\widehat{\mathfrak F}(\mathscr B_{\Delta_5})_{\le W}/
(\overline{J_{\rm BK}+\operatorname{Rad}_{\rm GN}})_{\le W}.
```

PBW comparison required:

```tex
\operatorname{gr}_{\rm PBW}U(P_X^{\Pi,\mathrm{red}})_{\le W}
\xrightarrow{\sim}
\operatorname{gr}_{\rm PBW}U(\mathfrak g_{\Delta_5})_{\le W}.
```

Rank identity, parity-refined:

```tex
H_X(t,z,x)=\prod_{\beta\in W_{\le3}}
(1-tx^\beta)^{-\dim L_{\beta,\bar0}}
(1+ztx^\beta)^{\dim L_{\beta,\bar1}},
```

and

```tex
[t^d z^{\bar p}x^\eta]H_X
 =
[t^d z^{\bar p}x^\eta]H_\Delta
\qquad(\eta\in W_{\le3}).
```

## Explicit Target PBW Ranks

Positive degree:

```tex
\delta_i:\ d=1:\ 1|0.
```

```tex
a_{ij}:\ d=1:\ 10|0,\quad d=2:\ 1|0.
```

```tex
2\delta_i+\delta_j:\ d=1:\ 1|0,\quad d=2:\ 10|0,\quad d=3:\ 1|0.
```

```tex
\tau:\ d=1:\ 29|93,\quad d=2:\ 30|0,\quad d=3:\ 1|0.
```

The negative window has the same ranks. Mixed positive-negative words and
Cartan powers are controlled by the triangular completion clauses, not
by a naive finite PBW rank count.

## Attack Result

Radical descent requires

```tex
QB(P\otimes K)=0,\quad
QB(K\otimes P)=0,\quad
(Q\otimes Q)DK=0,
```

and Hopf adjointness

```tex
M_{\alpha,\beta}^{t}G_{\alpha+\beta}
  =(G_\alpha\otimes G_\beta)D_{\alpha+\beta}^{\alpha,\beta}.
```

These make the quotient legitimate. They do not prove no-extra-relations
or PBW comparison. AP-CY418 is exactly this failure mode.

The no-extra-relations condition remains separate:

```tex
\ker\pi_W
  =
(\overline{J_{\rm BK}+\operatorname{Rad}_{\rm GN}})_{\le W}.
```

Transition control is also separate:

```tex
T^U_{R'R}(F^d_{\rm PBW}U_{R'})
  =
T^U_{R'R}(U_{R'})\cap F^d_{\rm PBW}U_R,
```

and stable images require

```tex
\operatorname{rank}M_{\mu\nu}
=\operatorname{rank}M_{\mu_0\nu}
=\operatorname{rank}[M_{\mu\nu}\ M_{\mu_0\nu}].
```

## Local Anchors

- `main.tex` near lines 12469 and 12743: primitive recognition data.
- `main.tex` near lines 12848 and 12933: finite-window datum.
- `main.tex` near lines 13836 and 14007: source matrices and ordinary
  PBW.
- `main.tex` near lines 14012 and 14111: source-to-target PBW
  comparison.
- `main.tex` near line 14137: target normal form.
- `main.tex` near lines 15004 and 15096: `W_{\le3}` table and
  obligations.
- `main.tex` near line 15268: finite matrix criterion.
- `main.tex` near line 15373: NO7 source protocol.
- `main.tex` near lines 785 and 11217: Dirac/Pfaffian firewall.
- CYQG AP-CY416 and AP-CY418.

## Decision

The manuscript proves the GN/Kac target PBW normal form and proves a
finite algebraic criterion. It assumes the compact source PBW
associated-graded rank comparison until actual source bases, matrices,
kernel equality, and transition ML ranks are supplied.

## Files Changed

None by the agent.

## Commands and Checks

Read-only `rg`, `sed`, `nl`, `git status --short`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`.
Target checks passed: `29|93`, `m(\tau)=-93`, height-four `108|90|18`,
doubled isotropic `10|9|1`.

## Residual Obligation

Construct the compact `W_{\le3}\cup(-W_{\le3})\cup\{0\}` source fixture
with provenance, compute `M,D,B,G,K,Q,A_beta`, prove radical
ideal/coideal, quotient tensor nondegeneracy, kernel equality, PBW
associated-graded ranks above, and strict transition/ML stable-image
ranks.

