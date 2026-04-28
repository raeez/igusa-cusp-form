# Next Koszul Attack-Heal Report

Date: 2026-04-28.
Worktree: `/tmp/igusa-next-koszul`.
Branch: `agent/igusa-next-koszul-20260428`.

## Claim Attacked

The attacked shortcut was:
\[
\mathsf{Den}_{\Delta_5,E}
\quad\text{and its target-internal bar--cobar counit}\quad
\Omega_E^{\mathrm{ch}}\bar B_E^{\mathrm{ch}}
(\mathsf{Den}_{\Delta_5,E})\to\mathsf{Den}_{\Delta_5,E}
\]
construct the compact \(K3\times E\) chiral coalgebra \(C_X\), the bar
comparison \(b_X\), or the cobar quasi-isomorphism
\(\Theta_{\mathrm{Kos}}\).

Status: false.  The target current envelope is imported target
observable algebra.  The compact source coalgebra, its bar comparison,
the hybrid local/wrapped coalgebra coproducts, and the cobar
quasi-isomorphism are separate source-side certificate data.

## Manuscript Changes

- `main.tex:245`: the introduction now names \(C_X\), \(b_X\), and
  \(\Theta_{\mathrm{Kos}}\) explicitly in the conditional
  Dirac--Igusa certificate.
- `main.tex:4536`: added `def:chiral-koszul-source-certificate`, a
  finite-stage certificate
  \[
  \mathfrak K^{\mathrm{Kos}}_{X,R}
  =
  (\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}},C_{X,R},
  F^{\mathrm{co}}_{R,\bullet},\Delta_R^{\mathrm{ch}},
  b_{X,R},\Theta_{\mathrm{Kos},R}).
  \]
- `main.tex:4646`: added the certificate consequence: compatible finite
  stages give
  \[
  b_X:C_X\simeq\bar B_E^{\mathrm{ch}}(\mathcal F_X^{\mathrm{hyb}}),
  \qquad
  \Theta_{\mathrm{Kos}}:\Omega_E^{\mathrm{ch}}C_X\simeq
  \mathsf{Den}_{\Delta_5,E}.
  \]
- `main.tex:6691`: strengthened the \((D_X)\) clause of
  \(\mathfrak K_X=(L_X,H_X,O_X,D_X,R_X)\) so normal ordering and Koszul
  comparison are both finite-stage source data.
- `main.tex:7016`: primitive recognition now invokes the full chiral
  Koszul source certificate, not a bare \(\Theta_{\mathrm{Kos}}\).
- `main.tex:7231`: the open full-certificate obstruction now requires
  \(\mathfrak O_{\mathrm{Kos},R}=0\) compatibly in \(R\).

## Theorem Status

- Proved/imported target: \(\mathsf{Den}_{\Delta_5,E}\) and its
  constant-current denominator algebra are imported from the
  Borcherds--Gritsenko--Nikulin target and Beilinson--Drinfeld current
  envelope.
- Conditional certificate: if the finite Koszul certificates are supplied
  for all \(R\), then \(C_X=\varprojlim_R C_{X,R}\) and the maps
  \(b_X,\Theta_{\mathrm{Kos}}\) exist in the completed chiral category.
- Open construction: no compact \(E_3\)-source, hybrid wrapped Hall
  object, source coalgebra, orientation line, primitive representatives,
  Hall constants, or PBW/radical theorem is constructed from the
  determinant or scalar square.

## Exact Obstruction List

At finite height \(R\), the Koszul residual is
\[
\mathfrak O_{\mathrm{Kos},R}=
(\mathfrak o^C_R,\mathfrak o^{\mathrm{conil}}_R,
\mathfrak o^b_R,\mathfrak o^\Omega_R,
\mathfrak o^{\mathrm{hyb}}_R,\mathfrak o^\Pi_R,
\mathfrak o^{\Prim}_R).
\]
The entries are: source coalgebra existence; conilpotence and finite
charge filtration; bar quasi-isomorphism \(b_{X,R}\); cobar
quasi-isomorphism \(\Theta_{\mathrm{Kos},R}\); compatibility with
local/local, local/wrapped, and wrapped/wrapped operations; compatibility
with normal-ordered descent and the reduced \(E\)-quotient; and primitive
restriction after the closed Hopf-radical quotient.

## Remaining Open Obligations

1. Construct \(\mathcal A_X^{E_3}\) with finite HN stages, formality,
   framing, QME/anomaly control, descent, and compact-support control.
2. Construct \(\mathcal F_X^{\mathrm{hyb}}\) with rigidified wrapped
   prequotients and mixed local/wrapped correspondences before the
   reduced \(E\)-quotient.
3. Construct \(C_{X,R}\), \(b_{X,R}\), and
   \(\Theta_{\mathrm{Kos},R}\), and prove
   \(\mathfrak O_{\mathrm{Kos},R}=0\) compatibly in \(R\).
4. Prove primitive recognition: compact bases, parity split, Hall
   constants, Borcherds--Kac relations, completed Hopf radical,
   no-extra-relations, and PBW.  The first finite test remains the
   \(\delta_1+\delta_2+\delta_3\) channel with signed size \(-64\).

## Verification

- `git diff --check` and `git diff --cached --check` passed after the
  manuscript patch.
- `pdflatex -halt-on-error -interaction=nonstopmode
  -output-directory=/tmp/igusa-next-koszul-texcheck main.tex` passed.
  The run was intentionally one pass into `/tmp`; it reported expected
  first-pass unresolved references and citations and did not touch
  `out/main.pdf`.
