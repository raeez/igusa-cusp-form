# A061 - Comparison Maps A_beta

## Claim Attacked

Whether the manuscript constructs the maps
`A_{\beta,\bar p}:L_{\beta,\bar p}\to
\mathfrak g_{\Delta_5,\beta,\bar p}`, or only assumes them after source
quotient complements are supplied.

## Verdict

It assumes them. The decisive line is `main.tex` near line 14026:
"Assume, as part of the source matrix data." The manuscript constructs a
target normal form and target point atlas, but the compact source
comparison map is a conditional datum, not a theorem.

## Required Equalities

After source matrices exist:

```tex
A_{\alpha+\beta}Q_{\alpha+\beta}B^X_{\alpha,\beta}
  =
B^\Delta_{\alpha,\beta}(A_\alpha Q_\alpha\otimes A_\beta Q_\beta),
```

```tex
(A_\mu\otimes A_\nu)(Q_\mu\otimes Q_\nu)D^{X,\mu,\nu}_\rho
  =
D^{\Delta,\mu,\nu}_\rho A_\rho Q_\rho,
```

```tex
G^\Delta_\gamma(A_\gamma x,A_{-\gamma}y)=G^X_\gamma(x,y).
```

Before these, the source must supply `M,D,B,G,K,Q`, with

```tex
B_{\alpha,\beta}
  =M_{\alpha,\beta}-(-1)^{|x||y|}M_{\beta,\alpha}\tau,\qquad
K_{\beta,\bar p}
  =\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^t,
```

and

```tex
QB(P\otimes K)=0,\quad QB(K\otimes P)=0,\quad
(Q\otimes Q)DK=0,\quad M^tG=(G\otimes G)D.
```

## Parity and Basis Requirement

`A_{\beta,\bar p}` is block diagonal in parity, invertible on
`L_{\beta,\bar p}`, has `A_0=\iota_H`, and is written only after neutral
source basis vectors `b^X_{R,\beta,\bar p,a}` with provenance and
quotient status are chosen.

## Constants Pinned by Local Checks

```tex
\alpha(n,l,m)
  =2nf_2-lf_3+2mf_{-2}
  =n\delta_1+m\delta_2+(n+m-l)\delta_3,
```

```tex
((\delta_i,\delta_j))=
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix}.
```

For `W_{\le3}`: `\delta_i:1|0`,
`\delta_i+\delta_j:10|0`, `2\delta_i+\delta_j:1|0`,
`\delta_{123}:29|93`, with `m(\delta_{123})=-93` and
`29-93=-64=f(1,1)`. Real Serre exponent `3`; complementary isotropic
exponent `5`.

## Leakage Risk

- `main.tex` near line 15048 introduces
  `e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s` as target bases. They must stay
  target-side or codomain-column labels for `A_{\beta,\bar p}`.
- `main.tex` near lines 12603 and 12657 use `e_i^X,u^X_{ij,r}`. Safe
  only as normalized source representatives after provenance, `Q`, and
  `A`; unsafe as raw source basis names.
- `main.tex` near lines 14137 and 14345 are target
  normal-form/point-atlas constructions. They are not compact `K3 x E`
  source bases.
- Quarantine refinement: source basis IDs should be neutral, for example
  `b^X_{R,\beta,\bar p,a}`. Target labels may appear only after an
  equation `A_{\beta,\bar p}Q_{\beta,\bar p}b^X
  =t^\Delta_{\beta,\bar p,r}`.

## Anchors

Finite comparison maps: `main.tex` near line 14012; finite source
criterion near line 15268; NO7 protocol near line 15373; guide section
12; CYQG AP-CY384.

## Claim Status

Conditional finite recognition criterion retained. Constructed
`A_\beta`: not proved. Source recognition is blocked until actual
compact `W_{\le3}` bases, matrices, comparison maps, kernel equality,
PBW associated-graded isomorphism, and strict transitions exist.

## Files Changed

None by the agent.

## Checks

Read `CLAUDE.md`, `AGENTS.md`, requested reports A049-A056; A057 was not
present when the agent ran. Ran
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py` and
`compute/verify_square_root.py`; both confirmed the target arithmetic
above.

