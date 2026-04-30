# A065 - Height-Four Terminal Row Stress Test

## Claim Attacked

`W_{\le3}` certifies height-four terminal rows.

## Verdict

Rejected. The target arithmetic is computed; the source theorem is still
blocked. `W_{\le3}` alone is not relation-closed.

## Rows Leaving W_{\le3}

Real Serre terminal rows: for ordered `i != j`,

```tex
(\operatorname{ad}e_i)^3e_j=0,\qquad
\deg=3\delta_i+\delta_j,\quad \operatorname{ht}=4.
```

The first two brackets land in `a_{ij}` and `2\delta_i+\delta_j`, inside
`W_{\le3}`; the terminal zero row lands outside. Same for
`(\operatorname{ad}f_i)^3f_j`. This needs height-four source `M,B,Q`
rows, not just target Serre exponent `3`.

Doubled isotropic rows: for `a_{ij}=\delta_i+\delta_j`,

```tex
2a_{ij}=2\delta_i+2\delta_j,\qquad \operatorname{ht}=4.
```

Verified target arithmetic:

```tex
\smult(2a_{ij})=10,\qquad \tau(2a_{ij})=9,\qquad 10-9=1.
```

The residual `1` is the signed lower real-string contribution; it is not
a compact source vector until matrices/provenance exist.

First missing timelike bracket/product rows:

```tex
\beta_i=\delta_i+\delta_{123}
\in
\{2\delta_1+\delta_2+\delta_3,
\delta_1+2\delta_2+\delta_3,
\delta_1+\delta_2+2\delta_3\}.
```

Inputs are already in `W_{\le3}`: `\delta_i+\delta_{123}`,
`a_{ij}+a_{ik}`, and `\delta_j+(2\delta_i+\delta_k)`. The odd rows
`[e_i,w_s]` land here. Verified target arithmetic:

```tex
\smult(\beta_i)=108,\qquad m(\beta_i)=90,\qquad 108-90=18.
```

This is signed root multiplicity, additive simple coefficient, and
signed lower residual, not full source parity data.

## Required Source Packet

Compact bases with provenance for every height-four output, plus
`M,D,B,G,K,Q,A_\beta`, negative blocks, transition matrices, NO7 rows

```tex
QB(P\otimes K)=0,\quad
QB(K\otimes P)=0,\quad
(Q\otimes Q)DK=0,
```

Hopf adjointness, kernel equality, PBW associated-graded comparison, and
ML-stable transitions.

## Anchors

- `main.tex` near lines 15148, 15176, 15208, and 15268.
- `compute/verify_square_root.py` near line 447.
- Reports A055, A058, A059, A060, and A062 agree: target arithmetic
  only; no source matrices.

## Commands

Read-only `rg`, `find`, `nl -ba`, `sed`; ran
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`,
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`, and a
read-only height-four row enumeration.

## Files Changed

None by the agent.

## Open Obligation

Build an enlarged height-four source fixture, at least `W_{\le4}` or
`W_{\le3}` plus terminal outputs, with actual compact geometric
provenance and matrices. `W_{\le3}` alone cannot certify these rows.

