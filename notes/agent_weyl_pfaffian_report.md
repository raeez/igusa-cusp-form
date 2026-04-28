# Weyl-Pfaffian attack-heal report

Date: 2026-04-28.

## Claim attacked

The attacked claim was any implication that Hall orientation monodromy is
constructed by the Maass character, by the Borcherds divisor, or by the
OP/DT scalar normalization.  The repaired chain separates:

- Hall side: a supplied reduced orientation line, a Weyl-equivariant lift
  (O1)+, and a local Pfaffian normal-mode model (O2).
- Group theory: once the three type-II simple signs are known and the
  lifted Coxeter action exists, the sign character factors through
  \(W^{(2)}(\Lambda^{2,1}_{II})_{\mathrm{ab}}\).
- Automorphic side: Maass/Gritsenko-Nikulin compute the target character
  \(\nu_{\Delta_5}\).

## Exact constants and signs

Type-II simple roots:

| root | Gram triple | Jacobi coefficient | local modes | Hall sign under O2 | Maass target |
|---|---:|---:|---:|---:|---:|
| \(\delta_1=2f_2-f_3\) | \((1,1,0)\) | \(f(0,1)=1\) | \(N_{\delta_1}=1\) | \(-1\) | \(-1\) |
| \(\delta_2=2f_{-2}-f_3\) | \((0,1,1)\) | \(f(0,1)=1\) | \(N_{\delta_2}=1\) | \(-1\) | \(-1\) |
| \(\delta_3=f_3\) | \((0,-1,0)\) | \(f(0,-1)=1\) | \(N_{\delta_3}=1\) | \(-1\) | \(-1\) |

The type-II Cartan matrix is
\[
\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}.
\]
Thus \(A_{ij}A_{ji}=4\) for \(i\ne j\), so all off-diagonal Coxeter
exponents are infinite and
\[
W^{(2)}(\Lambda^{2,1}_{II})_{\mathrm{ab}}\simeq(\mathbb Z/2)^3.
\]

The chamber-permuting roots
\[
f_{-2}-f_2,\qquad f_2-f_3,\qquad f_2+f_3
\]
have Maass value \(+1\).  They are automorphic target checks only; no
Hall orientation sign is asserted on them without a separately supplied
semidirect-product Hall lift.

## Theorem/proof status

- Proved group-theoretic consequence: a supplied lifted Coxeter action
  with the three local signs extends uniquely to a character on
  \(W^{(2)}(\Lambda^{2,1}_{II})\), factoring through \((\mathbb Z/2)^3\).
- Conditional Pfaffian computation: under O2, each type-II wall has local
  normal form \([\mathbb R\xrightarrow{u_i}\mathbb R]\), with
  \(s_{\delta_i}(u_i)=-u_i\).  The Pfaffian changes by \(-1\), while the
  determinant square is fixed.
- Unconditional automorphic target: Maass/Gritsenko-Nikulin give
  \(\nu_{\Delta_5}(s_{\delta_i})=-1\) and \(+1\) on the three
  \(\Aut(\Poly_{II})\)-reflections.
- Not proved here: construction of the reduced compact Hall orientation
  line, the Weyl-equivariant Hall lift, or the local normal-mode charts.

## Files changed

- `main.tex`
- `notes/agent_weyl_pfaffian_report.md`

## Commands run

- `sed`/`nl`/`rg` reads of `CLAUDE.md`, `AGENTS.md`, the three required
  notes, `proj.bib`, and the assigned `main.tex` regions.
- `python3 compute/verify_square_root.py`
- `python3 compute/verify_lattice.py`
- Inline Python check of the type-II Cartan matrix and Coxeter
  exponents.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-pdflatex-agent4 main.tex`

The temporary TeX run succeeded.  It was intentionally directed to
`/tmp/igusa-pdflatex-agent4` to avoid overwriting the shared
`out/main.pdf`; it produced the expected one-pass undefined-reference
and missing-bibliography warnings.

## Remaining obstruction

The geometric obstruction is still the construction of (O1), (O1)+, and
O2 on the reduced \(E\)-quotiented compact \(K3\times E\) Hall/CoHA
sector: determinant-line square root, finite-stabilizer linearization,
coherent Weyl action, and actual local Pfaffian normal charts on the
three type-II walls.
