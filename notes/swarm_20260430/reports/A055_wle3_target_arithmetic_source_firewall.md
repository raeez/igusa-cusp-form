# A055 - W_{\le3} Target Arithmetic Source Firewall

## Claim Attacked

`W_{\le3}` target arithmetic can be used as compact source evidence.

## Verdict

Rejected. The finite-window arithmetic is stable as target
Borcherds/Gritsenko-Nikulin/Kac data. It is not evidence for compact
Hall source bases, products, coproducts, pairings, radicals, quotient
maps, PBW, or transitions.

## Verified Target Arithmetic

Using `compute/verify_square_root.py` and a read-only `W_{\le3}`
enumeration:

```tex
\gamma(c_1\delta_1+c_2\delta_2+c_3\delta_3)
  =(c_1,c_1+c_2-c_3,c_2).
```

```tex
((\delta_i,\delta_j)) =
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix}.
```

Target `W_{\le3}` table:

```tex
\delta_i:1|0,\qquad
\delta_i+\delta_j:10|0,\qquad
2\delta_i+\delta_j:1|0,\qquad
\delta_{123}:29|93.
```

For `\delta_{123}=\delta_1+\delta_2+\delta_3`:

```tex
\smult(\delta_{123})=-64,\qquad
m(\delta_{123})=-93,\qquad
29-93=-64.
```

The Laurent check is:

```tex
A(r)(B(r)^2+C(r))
  =9r^{-3}-93r^{-2}+90r^{-1}-90+93r-9r^2.
```

Height four:

```tex
m(2\delta_1+\delta_2+\delta_3)
=m(\delta_1+2\delta_2+\delta_3)
=m(\delta_1+\delta_2+2\delta_3)=90,
```

```tex
m(2\delta_{123})=-540,\qquad 108|90|18
```

in each of the three height-four timelike degrees.

Doubled isotropic:

```tex
\smult(2\delta_i+2\delta_j)=10,\qquad
\tau(2(\delta_i+\delta_j))=9,\qquad
10-9=1.
```

## Failure Mode

Target arithmetic gives the reference denominator algebra. It does not
construct the compact source. The determinant is blind to zero brackets,
wrong brackets, hidden `W\oplus\Pi W` cancelling pairs, bad radicals,
and extra relations. The manuscript states this correctly near
`main.tex` line 14867 and makes `W_{\le3}` recognition conditional near
line 15096.

Source recognition needs actual compact data:

```tex
M,D,B,G,K,Q,A_\beta,
```

with `QB(P\otimes K)=0`, `QB(K\otimes P)=0`, `(Q\otimes Q)DK=0`, Hopf
adjointness, kernel equality, PBW associated graded, and ML-stable
transitions. Anchors: `main.tex` near lines 15268 and 15373.

## Keep Target-Side Only

Keep these as target-side statements only:

- Low-degree active rows and Chevalley/Serre constants.
- Isotropic `10=1+9`, `\tau(ta_{ij})=9`.
- `\delta_{123}` count `29|93`.
- `W_{\le3}` parity table and target bracket templates.
- Height-four and doubled-isotropic checks.
- Target bases `e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s` until source
  bases and `A_{\beta,\bar p}` exist.

Critique anchors agree: guide section 12, A006, A030, A049, and
CYQG AP-CY378/AP-CY384.

## Files Changed

None by the agent.

## Commands and Checks

Read-only `sed`, `nl -ba`, `rg`, `find`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`;
read-only custom `W_{\le3}` enumeration.

## Residual Obligations

Construct the compact `W_{\le3}` source table: bases with provenance,
`M,D,B,G,K,Q,A_\beta`, the `29|93` source block, the 27 mixed maps,
radical coideal checks, no-extra-relations, PBW, and strict
transition/ML data.

