# A057 - Delta_123 29|93 Source Realization

## Claim Attacked

Whether the compact source constructs the `\delta_{123}` block as `29`
even and `93` odd primitive source vectors, with retained-stratum
provenance, orientation/parity data, source matrices, radical quotient,
and comparison maps.

## Verdict

Not constructed. The current manuscript imports the `29|93` block as
target Gritsenko-Nikulin/Kac presentation data and states a conditional
source-matrix criterion. It does not exhibit compact source basis
vectors, retained-stratum labels, evaluated `M,D,B,G,K,Q` matrices, or
source-built `A_{\beta,\bar p}` comparison maps.

## Local Proof Anchors

Target count near `main.tex` line 14901:

```tex
m(\delta_{123})=-93,\qquad
\rootmult_{\bar0}(\delta_{123})=29,\quad
\rootmult_{\bar1}(\delta_{123})=93.
```

The proof explicitly says this is target-side and not a compact Hall
computation near lines 14928 and 14999.

The source requirement near `main.tex` line 15268 requires compact
source bases, `M,D,B,G,K,Q`, provenance, splittings `K\oplus L`, kernel
equality, PBW, and transitions. Its proof says the scripts supply only
target lattice/GN arithmetic near line 15360.

## Mixed Brackets

The guide calls them `V_{k;ij,r}`. The manuscript target notation uses

```tex
M_{12,r}=[e_3,u_{12,r}],\quad
M_{13,r}=[e_2,u_{13,r}],\quad
M_{23,r}=[e_1,u_{23,r}]
```

near `main.tex` line 15058. The source version is only an obligation:

```tex
[e_k^X,u^X_{ij,r}]
  =\sum_a C^{\bar0}_{k;ijr,a}v^{\bar0}_a
```

near line 14820. No `C`-matrix is evaluated.

## Jacobi and Radical

`T_1+T_2+T_3=0` is target Jacobi for even real generators near
`main.tex` lines 14775 and 14854. The source relation
`T_1^X+T_2^X+T_3^X=0` is required, not proved, near line 15100.

The source radical test is conditional on `G,K,Q,D,B` matrices and NO7:

```tex
QB(P\otimes K)=0,\quad
QB(K\otimes P)=0,\quad
(Q\otimes Q)DK=0.
```

Anchors: `main.tex` near lines 12680, 15300, and 15373.

## Source Labels

Target labels `e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s` are target
fixtures. A056 quarantines them until `Q` and `A_{\beta,\bar p}` exist.

## Cross-Checks

- Guide section 12: target arithmetic does not supply source matrices.
- A006, A049, A050, A053, A055, and A056 agree: recognition remains
  conditional.
- CYQG AP-CY378 and AP-CY384 match the failure mode: target arithmetic
  is not source matrices, and target basis is not source basis.
- CYQG AP-CY411 blocks using type-II root labels as retained wall atoms
  without geometry.

## Commands and Checks

Read-only `rg`, `nl -ba`, `sed`, `git status --short`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`.

The scripts confirmed the target data: Gram matrix,
`[qrs]D_5/(qrs)^{1/2}=93`, `29|93`, `m(\delta_{123})=-93`,
height-four `108|90|18`, and doubled-isotropic `10|9|1`. They did not
compute compact source matrices.

## Files Changed

None by the agent.

## Claim-Status Recommendation

Keep `\delta_{123}:29|93`, `T_1+T_2+T_3=0`, the mixed bracket
templates, and `W_{\le3}` matrices as target/reference data. Keep
compact source realization conditional/open until actual `W_{\le3}`
source bases with provenance, `M,D,B,G,K,Q,A_{\beta,\bar p}`, radical
ideal/coideal checks, kernel equality, PBW, and ML-compatible
transitions are supplied.

