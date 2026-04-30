# A059 - Coproduct and Coalgebra Matrices in W_{\le3}

## Claim Attacked

Finite `W_{\le3}` source coproduct / coalgebra matrices are computed well
enough to prove primitive recognition, NO7 Hopf radical descent,
product-coproduct adjunction, and source coalgebra compatibility.

## Verdict

Not proved. The manuscript has a precise conditional recipe and finite
matrix criterion. It does not contain actual retained `W_{\le3}` source
coproduct matrices, source primitive bases, radical kernels, or
protected compact-support integrals.

## Needed D Matrices

For each retained stage `R`, one needs

```tex
D^{\mu,\nu}_\rho:
P^X_{R,\rho}\to P^X_{R,\mu}\otimes P^X_{R,\nu}
```

for every retained ordered decomposition

```tex
(\rho;\mu,\nu)\in\mathrm{Dec}^{\pm}_{\le3}(R),\qquad
\rho,\mu,\nu\in W_{\le3}\cup(-W_{\le3})\cup\{0\},\quad
\rho=\mu+\nu.
```

At minimum this includes the positive target-template decompositions:

```tex
D^{\delta_i,\delta_j}_{a_{ij}},\quad
D^{\delta_j,\delta_i}_{a_{ij}},
```

```tex
D^{\delta_i,a_{ij}}_{2\delta_i+\delta_j},\quad
D^{a_{ij},\delta_i}_{2\delta_i+\delta_j},
```

and the six `\tau=\delta_1+\delta_2+\delta_3` decompositions

```tex
D^{\delta_1,a_{23}}_\tau,\ D^{a_{23},\delta_1}_\tau,\quad
D^{\delta_2,a_{13}}_\tau,\ D^{a_{13},\delta_2}_\tau,\quad
D^{\delta_3,a_{12}}_\tau,\ D^{a_{12},\delta_3}_\tau.
```

The negative analogues and all retained mixed positive-negative
decompositions are also required by the NO7 protocol, not just the
displayed positive templates.

## Exact Identities

Primitive recognition uses

```tex
P_R=\ker(\Delta_R-1\otimes\mathrm{id}-\mathrm{id}\otimes1)
    \cap\ker\epsilon_R.
```

Radicals are

```tex
K_{\beta,\bar p}
  =\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t},
\qquad
P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p},
\qquad
Q_{\beta,\bar p}=[0\ I].
```

NO7 requires

```tex
QB(P\otimes K)=0,\qquad
QB(K\otimes P)=0,\qquad
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_\rho K_\rho=0,
```

and Hopf adjointness

```tex
M_{\alpha,\beta}^{t}G_{\alpha+\beta}
  =(G_\alpha\otimes G_\beta)D^{\alpha,\beta}_{\alpha+\beta}.
```

The source-to-target comparison also requires

```tex
(A_\mu\otimes A_\nu)(Q_\mu\otimes Q_\nu)D^{X,\mu,\nu}_\rho
  =D^{\Delta,\mu,\nu}_\rho A_\rho Q_\rho.
```

## Failure

The manuscript proves: if the compact source supplies the bases,
matrices, compact-support pull-push identities, quotient tensor
nondegeneracy, PBW/no-extra-relations, and strict transitions, then
recognition follows.

It does not supply those matrices. The scripts verify target arithmetic
only. They do not integrate over retained stacks or produce
`M,D,G,K,Q,A_\beta`.

Coassociativity is assigned to finite flag stacks and the chiral bar cut
maps. Jacobi gives `d_{\mathrm{CE},R}^2=0`. A separate explicit
`W_{\le3}` coJacobi/coderivation matrix computation is not present; it
remains part of the source coalgebra certificate.

## Local Anchors

- `main.tex:9581-9646`: NO7 finite matrix test.
- `main.tex:9742-9783`: Hopf-adjointness radical lemma.
- `main.tex:11392-11400`: primitive subobject definition.
- `main.tex:13737-13833`: source chiral coalgebra, coassociativity via
  cut/flag maps.
- `main.tex:13836-14010`: recipe for `M,D,G,K,Q` from compact Hall
  source.
- `main.tex:14012-14063`: `A_\beta` comparison equations.
- `main.tex:15004-15146`: `W_{\le3}`, `29|93`, target templates, and
  source-data obligation.
- `main.tex:15268-15370`: finite source matrix criterion.
- `main.tex:15373-15442`: `W_{\le3}` NO7 protocol.

## Cross-Report Alignment

A030, A051, A053, A054, A055, and A056 agree: source recognition is
conditional. CYQG AP-CY378/AP-CY382/AP-CY384 say target arithmetic is
not source matrices, finite windows need strict limits, and target bases
are not compact source bases.

## Commands and Checks

Read-only `sed`, `nl -ba`, `rg`; ran
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py` and
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`.

The scripts confirmed target data: `W_{\le3}` table
`1|0,10|0,1|0,29|93`, `29-93=-64=f(1,1)`, and height-four gaps
`108|90|18`. They produced no source matrices.

## Files Changed

None by the agent.

## Open Obligations

Construct actual `W_{\le3}\cup(-W_{\le3})\cup\{0\}` source bases with
provenance; compute `M,D,B,G,K,Q`; verify `(Q\otimes Q)DK=0`, Hopf
adjointness, coassociativity/coJacobi/coderivation compatibility,
kernel equality, PBW associated gradeds, `A_\beta` comparison maps,
compact-support/protected integration admissibility, and strict
transition/ML conditions.

