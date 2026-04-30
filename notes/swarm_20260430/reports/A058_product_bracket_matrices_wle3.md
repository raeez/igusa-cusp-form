# A058 - Product and Bracket Matrices in W_{\le3}

## Verdict

`CONDITIONAL / BLOCKED AS SOURCE THEOREM`. The `W_{\le3}` target GN/Kac
table is stable. It does not verify compact Hall source recognition. The
finite source certificate must supply actual source bases and matrices
`M,D,B,G,K,Q,A_\beta`.

## Target GN/Kac Rows

Let `a_{ij}=\delta_i+\delta_j`,
`\tau=\delta_1+\delta_2+\delta_3`. Target dimensions:

```tex
\delta_i:1|0,\quad
a_{ij}:10|0,\quad
2\delta_i+\delta_j:1|0,\quad
\tau:29|93.
```

The target `a_{ij}` basis is `E_{ij}=[e_i,e_j]` plus
`u_{ij,1},...,u_{ij,9}`. In `\tau_{\bar0}`:

```tex
T_1=[e_1,E_{23}],\quad
T_2=[e_2,E_{31}],\quad
T_3=[e_3,E_{12}],\quad
T_1+T_2+T_3=0.
```

With `E_{31}=-E_{13}`, target bracket templates are:

```tex
B^\Delta_{\delta_i,\delta_j}=c_0,\quad
B^\Delta_{\delta_j,\delta_i}=-c_0,\quad
c_0=(1,0,\ldots,0)^t\in\mathbb C^{10}.
```

Adjacent rows:

```tex
B^\Delta_{\delta_p,a_{ij}}=(1,0,\ldots,0)\quad(p=i,j),
```

so the `u_{ij,r}` columns vanish.

Complementary rows:

```tex
B^\Delta_{\delta_1,a_{23}}(E_{23})=T_1,\quad
B^\Delta_{\delta_1,a_{23}}(u_{23,r})=M_{23,r},
```

```tex
B^\Delta_{\delta_2,a_{13}}(E_{13})=-T_2,\quad
B^\Delta_{\delta_2,a_{13}}(u_{13,r})=M_{13,r},
```

```tex
B^\Delta_{\delta_3,a_{12}}(E_{12})=-T_1-T_2,\quad
B^\Delta_{\delta_3,a_{12}}(u_{12,r})=M_{12,r}.
```

Odd `\tau` rows are zero for these positive complementary maps. These
are target rows only.

## Source Hall Matrix Packet

For

```tex
S_{\le3}=W_{\le3}\cup(-W_{\le3})\cup\{0\},
```

the source must supply ordered product matrices

```tex
M^X_{\alpha,\beta}:P^X_{R,\alpha}\otimes P^X_{R,\beta}
  \to P^X_{R,\alpha+\beta}
```

for every retained ordered pair
`\alpha,\beta,\alpha+\beta\in S_{\le3}`, plus any declared zero-output
Serre/string relation row outside `S_{\le3}`.

The bracket sign convention is:

```tex
B^X_{\alpha,\beta}
 =
M^X_{\alpha,\beta}
-(-1)^{|x||y|}M^X_{\beta,\alpha}\tau_{\alpha,\beta},
```

where `\tau_{\alpha,\beta}(x\otimes y)=y\otimes x` is the ordinary flip.
Equivalently the second term uses the super-flip. Even-even rows are
ordinary commutators; odd-odd Chevalley rows, including the 93 odd
`\tau` generators against their negatives, are symmetric in the super
sense.

Required source identities:

```tex
K_{\beta,\bar p}
  =\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t},\quad
P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p},\quad
Q_{\beta,\bar p}=[0\ I],
```

```tex
QB(P\otimes K)=0,\quad QB(K\otimes P)=0,\quad
(Q\otimes Q)DK=0,
```

```tex
(M_{\alpha,\beta})^tG_{\alpha+\beta}
  =(G_\alpha\otimes G_\beta)D^{\alpha,\beta}_{\alpha+\beta}.
```

Then source-to-target maps

```tex
A_{\beta,\bar p}:L_{\beta,\bar p}\to
\mathfrak g_{\Delta_5,\beta,\bar p}
```

must intertwine source and target bracket, coproduct, pairing, Cartan
action, and transitions.

## Relation Rows to Verify in Source

Chevalley: all retained simple positive/negative pairs, not only real
roots:

```tex
[h,e_i^X]=(h,\alpha_i)e_i^X,\quad
[h,f_i^X]=-(h,\alpha_i)f_i^X,\quad
[e_i^X,f_j^X]=\delta_{ij}h_i^X.
```

This includes the 9 isotropic `u_{ij,r}` copies and the 93 odd `\tau`
generators.

Real Serre: target exponent `3` for `i != j`:

```tex
(\operatorname{ad}e_i)^3e_j=0,\quad
(\operatorname{ad}f_i)^3f_j=0.
```

The visible first two brackets use `B_{\delta_i,\delta_j}` and
`B_{\delta_i,a_{ij}}`. The terminal zero row lands in height `4`, so it
is not discharged by matrices whose outputs are only in `W_{\le3}`.

Isotropic orthogonality: adjacent rows

```tex
[e_i^X,u^X_{ij,r}]=[e_j^X,u^X_{ij,r}]=0,\quad
[f_i^X,u^X_{ij,r}]=[f_j^X,u^X_{ij,r}]=0,
```

and negative analogues. Mutual isotropic-copy rows on doubled rays are
height `4` data and remain outside the strict `W_{\le3}` packet.

Complementary real strings:

```tex
(\delta_k,a_{ij})=-4,\quad
(\operatorname{ad}e_k)^5u^X_{ij,r}=0,\quad
(\operatorname{ad}f_k)^5u^{-,X}_{ij,r}=0.
```

Only the first maps `[e_k,u_{ij,r}]\to\tau_{\bar0}` are in `W_{\le3}`.
The full terminal string needs intermediate/terminal height `4` through
`7` source rows or an explicit enlarged finite window.

Jacobi:

```tex
T_1^X+T_2^X+T_3^X=0
```

must hold in `L_{\tau,\bar0}` before or after applying
`A_{\tau,\bar0}`; target Jacobi alone is not source Jacobi.

## Anchors

Main anchors: `main.tex` near lines 12531, 13836, 15004, 15069, 15268,
and 15373. Guide section 12 agrees. CYQG has AP-CY378/AP-CY384 present;
AP-CY416 was not found by the agent because it was added by the master
thread afterward.

## Commands and Checks

Read-only `sed`, `nl -ba`, `rg`, `find`, `git status --short`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`.

## Files Changed

None by the agent.

## Residual Obligation

Construct retained source bases with provenance, compute `M,D,G`, derive
`B,K,Q,A_\beta`, prove the relation rows, NO7, no-extra-relations, PBW,
and strict transition/Mittag-Leffler compatibility.

