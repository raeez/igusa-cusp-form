# A068 - GN/GNII/Kac/Borcherds Citation and Convention Patch

## Claim Attacked

Citation/convention split around `\mathfrak g_{\Delta_5}`, `\autcor`,
GN/GNII product data, and Borcherds-Kac presentation/PBW.

## Verdict

One real citation bug, one presentation-source gap. No file edits by the
agent.

## Primary Fault

`main.tex` near line 5818 says GNII Theorem 2.1 constructs `\autcor`.
That is too strong. GNII supplies the explicit Borcherds
product/product-lift data. The corrected Lorentzian BKM algebra should
be attributed primarily to GN Sections 3-4 / Proposition 3.1. The
manuscript already has the correct split near line 17008: Borcherds95 +
GNII for product, GN Proposition 3.1 for the Lorentzian correction and
denominator function.

## Correct Source Partition

Product lift / scalar product:

- `main.tex` near lines 1948, 2606, and 16977.
- Use Borcherds95 Theorem 10.1 for the general lift.
- Use GNII Theorem 2.1 / Example 2.4 / equations (2.15)-(2.16) for the
  explicit `\phi_{0,1}` product.
- Use GN Theorem 4.1 for theta normalization `D_5=64^{-1}\Delta_5`.

GN algebra construction:

- `main.tex` near lines 5726 and 17011.
- Use GN Sections 3-4, especially Proposition 3.1, for the automorphic
  correction algebra and denominator `D_5(2Z)=64^{-1}\Delta_5(2Z)`.

BKM presentation / PBW:

- `main.tex` near lines 12488, 12513, 12627, 12743, 15586, and 15639.
- Current `\cite{GN,GNPartI,GNII,KAC:1}` near line 12531 is plausible
  but incomplete for generalized Kac-Moody presentation conventions.
- Add Borcherds 1988, *Generalized Kac-Moody algebras*, J. Algebra
  115(2), 501-512, DOI `10.1016/0021-8693(88)90275-X`. The agent
  verified the author PDF at
  `https://math.berkeley.edu/~reb/papers/gkma/gkma.pdf`.

## Minimal Patch Proposal

1. Replace the first sentence of the proof near `main.tex` line 5818
   with the source split used near line 17008: GNII for the product and
   correction coefficients; GN Sections 3-4 / Proposition 3.1 for
   `\autcor`.
2. Add a `BorcherdsGKM88` bibliography entry and cite it near line 12531
   and/or line 15639 for the generalized Kac-Moody generator-relation
   convention with imaginary simple roots. Keep Kac for ordinary
   real-root/PBW conventions.
3. Add one sentence near `main.tex` line 14993: the `2+27=29` count is a
   target-side GN/Kac/Borcherds presentation count after the standard
   radical quotient, not a consequence of the denominator product alone.

## Constants Checked

```tex
\alpha(n,l,m)
  =2nf_2-lf_3+2mf_{-2}
  =n\delta_1+m\delta_2+(n+m-l)\delta_3.
```

```tex
((\delta_i,\delta_j))=
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix},
\qquad
\rho=f_2-\tfrac12 f_3+f_{-2}.
```

```tex
D_5=64^{-1}\Delta_5,\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z).
```

Computations confirmed `m(\delta_{123})=-93`, target split `29|93`,
`29-93=-64=f(1,1)`, `\tau(ta)=9` on primitive isotropic rays, adjacent
isotropic pairing `0`, complementary pairing `-4`, real-string exponent
`5`, and real-real exponent `3`.

## Commands

Read-only `sed`, `nl -ba`, `rg`; `python3 compute/verify_lattice.py`;
`python3 compute/verify_square_root.py`; `git status --short`; one web
lookup for Borcherds 1988 metadata. No build.

## Files Changed

None by the agent.

