# A010 report: GN denominator algebra and BKM root data

Runtime id: `019ddbcc-420c-74b2-8ab6-267664bfa16b`.
Nickname: Maxwell.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Gritsenko--Nikulin denominator algebra and BKM root-data lane.

## Imported

The GN target algebra is imported, not locally constructed.

Anchors:
`main.tex:5719`, `main.tex:5817`.

Primary-source spine:

- GN 1997 constructs the correcting generalized Kac--Moody
  superalgebra for matrix
  \[
  \begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix},
  \]
  with no odd real simple roots, and denominator
  \(64^{-1}\Delta_5(2Z)\). Source: arXiv `alg-geom/9504006`.
- GNII Theorem 2.1 / Example 2.4 supplies product-lift data and the
  monic \(\Delta_5\) product in its normalization. Source: arXiv
  `alg-geom/9611028`.
- Kac/Borcherds presentation structure is imported via Kac plus the GN
  appendix, not derived from the determinant.

## Computed Locally

Lattice/root map:
\[
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}
=n\delta_1+m\delta_2+(n+m-l)\delta_3.
\]
Anchors:
`main.tex:5331`, `main.tex:5530`.

Gram matrix and Weyl vector:
\[
((\delta_i,\delta_j))=
\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix},
\quad
\rho=f_2-\tfrac12f_3+f_{-2}.
\]
Anchors:
`main.tex:5510`, `python3 compute/verify_lattice.py`.

Product/doubling normalization:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z)=64^{-1}\Delta_5(2Z).
\]
Anchor:
`main.tex:16977`.

Low-degree coefficient checks:
\[
f(1,1)=-64,\quad
m(\delta_1+\delta_2+\delta_3)=-93,\quad
29-93=-64.
\]
Anchor:
`main.tex:14901`, `python3 compute/verify_square_root.py`.

## Attack Findings

Attribution bug:
`main.tex:5818` says GNII Theorem 2.1 constructs
\(\mathfrak g_{\Delta_5}\). That theorem is the product-lift theorem.
The algebra construction should be attributed to GN Section 3 /
Proposition 3.1, with GNII used for product and row generalization.

The \(29|93\) split is plausible and locally checked, but the proof
should explicitly cite the Kac/Borcherds presentation theorem ensuring
the listed mixed brackets survive the standard radical. The determinant
only gives \(-64\).

No compact-source overclaim found in this lane. The manuscript repeatedly
states that \(\mathfrak g_{\Delta_5}\) is target-side and does not
construct compact Hall brackets, BPS state spaces, orientation data, or
\(\mathfrak D_X\).

Anchors:
`main.tex:785`, `main.tex:5868`, `main.tex:14867`.

## Residual Obligation

Patch the citation sentence at `main.tex:5818` and add one
source-backed sentence for survival of the low-degree presentation words
after the GN/Kac radical quotient.

Commands run by agent:
`sed`, `rg`, `nl -ba ... sed`, arXiv source `curl | gzip -dc | rg/sed`,
`python3 compute/verify_lattice.py`,
`python3 compute/verify_square_root.py`.
