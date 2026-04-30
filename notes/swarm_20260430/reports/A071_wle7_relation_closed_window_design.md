# A071 - W_{\le7} Relation-Closed Window Design

Proposal only. No files edited by the agent.

Use the relation-minimal positive window `W^+_{A071}`, then take

```tex
S_{A071}=W^+_{A071}\cup(-W^+_{A071})\cup\{0\}.
```

Let `a_{ij}=\delta_i+\delta_j`, `\tau=\delta_1+\delta_2+\delta_3`, and
for `{i,j,k}={1,2,3}`,

```tex
C_{k,s}=a_{ij}+s\delta_k.
```

## Degree Set

```tex
W^+_{A071}=W_{\le3}\cup R_4\cup I_4\cup C_{\le7}\cup\{2\tau\},
```

where

```tex
W_{\le3}
=\{\delta_i\}\cup\{a_{ij}\}\cup\{2\delta_i+\delta_j:i\ne j\}
\cup\{\tau\},
```

```tex
R_4=\{3\delta_i+\delta_j:i\ne j\},
\qquad
I_4=\{2a_{ij}:i<j\},
```

```tex
C_{\le7}=\{C_{k,s}:k=1,2,3,\ s=2,3,4,5\}.
```

Explicitly by height, added to `W_{\le3}`:

```text
h=4:
(3,1,0),(1,3,0),(3,0,1),(1,0,3),(0,3,1),(0,1,3)
(2,2,0),(2,0,2),(0,2,2)
(2,1,1),(1,2,1),(1,1,2)

h=5:
(3,1,1),(1,3,1),(1,1,3)

h=6:
(4,1,1),(1,4,1),(1,1,4),(2,2,2)

h=7:
(5,1,1),(1,5,1),(1,1,5)
```

Positive count: `35`. Full signed matrix packet count:
`2*35+1=71` degree blocks.

## Target Arithmetic

For every `\beta=(c_1,c_2,c_3)`, record

```tex
\gamma(\beta)=(c_1,c_1+c_2-c_3,c_2),\qquad
\smult(\beta)=f(nm,l).
```

Required checked target rows:

```text
W<=3:
delta_i: 1|0
a_ij: 10|0 = E_ij plus 9 isotropic simple directions
2delta_i+delta_j: 1|0
tau: 29|93, with 29-93=-64 and m(tau)=-93

R4:
3delta_i+delta_j has target quotient 0|0; this is the real-Serre terminal output.

I4:
2a_ij has smult=10, tau(2a_ij)=9, residual 1.

C_{k,2}:
smult=108, m=90, residual 18.

C_{k,3}:
smult=-64; full parity is available only after a separate target
justification. A080 proposes Weyl transport \(C_{k,3}=s_k(\tau)\), hence
\(29|93\), if the real-reflection parity-preserving target action is
included in the target fixture.

C_{k,4}:
smult=10; full parity is available only after a separate target
justification. A080 proposes Weyl transport \(C_{k,4}=s_k(a_{ij})\),
hence \(10|0\). This degree is nonzero even though it receives the
\(\tau\)-string terminal zero row.

C_{k,5}:
target quotient 0|0; complementary-string terminal output.

2tau:
smult=f(4,2)=4016, m(2tau)=-540; full parity presentation required.
```

Rows whose parity source is only `signed_only_blocked` cannot feed target
bases, PBW rows, or source comparison maps. The target fixture must
record whether a parity row comes from `gn_kac_base`, `weyl_transport`,
`serre_zero`, or `target_presentation_computed`.

## Source Packets

For every `\beta\in S_{A071}` and parity block, the certificate must
supply:

```tex
P^X_{R,\beta,\bar p},\quad
M_{\alpha,\beta},\quad
D^{\mu,\nu}_\rho,\quad
G_{\beta,\bar p},\quad
K_{\beta,\bar p},\quad
Q_{\beta,\bar p},\quad
A_{\beta,\bar p}.
```

with

```tex
B_{\alpha,\beta}
  =M_{\alpha,\beta}-(-1)^{|x||y|}M_{\beta,\alpha}\tau,
```

```tex
K_{\beta,\bar p}
  =\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^t,\qquad
P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p}.
```

Required identities:

```tex
QB(P\otimes K)=0,\qquad
QB(K\otimes P)=0,\qquad
(Q\otimes Q)DK=0,
```

```tex
M_{\alpha,\beta}^tG_{\alpha+\beta}
  =(G_\alpha\otimes G_\beta)D^{\alpha,\beta}_{\alpha+\beta}.
```

Also required: enlarged `relation_rows`, `pbw`, `no_extra`,
`transitions`, and `ml_stable_images` packets in the A067 schema, now
with `window=A071_Wle7_rel_closed`.

## Why It Closes

Real Serre closes because

```tex
\delta_j\to\delta_i+\delta_j\to2\delta_i+\delta_j\to3\delta_i+\delta_j
```

is entirely in `S_{A071}`, and the last degree is the terminal zero row.

Doubled isotropic closes because every

```tex
a_{ij}+a_{ij}=2a_{ij}
```

is retained, so mutual isotropic-copy rows are actual `QB` rows, not
deferred outputs.

Tau-simple odd interactions close because

```tex
\tau\to\tau+\delta_i\to\tau+2\delta_i\to\tau+3\delta_i
```

is retained, and `2\tau` is retained for odd-odd `\tau`-simple brackets.

Complementary strings close because

```tex
a_{ij}\to C_{k,1}=\tau\to C_{k,2}\to C_{k,3}\to C_{k,4}\to C_{k,5}
```

is retained through the height-7 terminal row.

## Anchors and Checks

Anchors: `main.tex` near lines 15004, 15268, and 15373; reports A058,
A063, A065, A066, and A067.

Read-only checks run: `compute/verify_lattice.py`,
`compute/verify_square_root.py`, plus a read-only enumeration of the
proposed degree set.
