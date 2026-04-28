# Next primitive recognition attack-heal report

Date: 2026-04-28.

## Claim attacked

The attacked shortcut was:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})
=64^{-1}\Delta_5(2Z)
\quad\Longrightarrow\quad
\text{compact primitive recognition}.
\]

This shortcut remains false.  The determinant and the
Gritsenko--Nikulin denominator fix signed multiplicities after the target
Borcherds datum is fixed.  They do not construct the compact generators,
parity split, Hall brackets, Borcherds--Kac relations, Hopf pairing,
closed radical quotient, no-extra-relations theorem, generation, or
completed PBW comparison.

## Manuscript heal

- Strengthened `S9` in Theorem `thm:primitive-recognition`: full parity
  means equality of the two target integers
  \[
  \dim P^{\Pi,\mathrm{red}}_{X,\gamma,\overline p}
  =d^{\mathrm{GN}}_{\gamma,\overline p}
  :=\rootmult_{\overline p}(\alpha(\gamma)),\qquad p=0,1,
  \]
  not only equality of their difference.
- Strengthened the low-degree channel
  \(\delta_{123}=\delta_1+\delta_2+\delta_3\):
  \[
  \smult(\delta_{123})=f(1,1)=-64,
  \qquad
  d^{\mathrm{GN}}_{0,123}-d^{\mathrm{GN}}_{1,123}=-64.
  \]
  The compact source must match
  \(d^{\mathrm{GN}}_{0,123}\) and \(d^{\mathrm{GN}}_{1,123}\), not choose
  an arbitrary pair with difference \(-64\).
- Added the first real-string Borcherds--Kac test in this channel.  For
  \(a_{ij}=\delta_i+\delta_j\) and \(\{i,j,k\}=\{1,2,3\}\),
  \[
  (\delta_k,a_{ij})=-4,\qquad
  1-2(\delta_k,a_{ij})/(\delta_k,\delta_k)=5,
  \]
  hence the target relation includes
  \[
  (\operatorname{ad}e_k)^5u_{ij,r}=0
  \]
  and the analogous negative-generator relation.
- Made the compact test explicit: produce parity-homogeneous bases in
  degree \((1,1,1)\), compute the even Hall constants
  \[
  [e_k^X,u^X_{ij,r}]
  =
  \sum_{a=1}^{d^{\mathrm{GN}}_{0,123}}
  C^{\overline0}_{k;ijr,a}v^{\overline0}_a,
  \]
  verify \(T_1^X+T_2^X+T_3^X=0\), the real-string relations, the completed
  Hopf-pairing matrix between \(\delta_{123}\) and \(-\delta_{123}\), and
  the closed radical quotient.

## Constants and anchors

- `main.tex`: Theorem `thm:primitive-recognition`, clauses `S1`--`S9`.
- `main.tex`: Proposition `prop:low-degree-denominator-brackets`.
- Real Cartan matrix:
  \[
  ((\delta_i,\delta_j))=
  \begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}.
  \]
- Degree map:
  \[
  \alpha(n,l,m)
  =2nf_2-lf_3+2mf_{-2}
  =n\delta_1+m\delta_2+(n+m-l)\delta_3.
  \]
- First compact test:
  \[
  \gamma(\delta_{123})=(1,1,1),\qquad
  (\delta_{123},\delta_{123})=-6,\qquad
  \smult(\delta_{123})=-64.
  \]

## Remaining obstruction

Construct the compact finite-first Hall/factorization source and compute
the presentation-level data.  The first finite obstruction is still the
\(\delta_1+\delta_2+\delta_3\) channel: the GN target gives signed size
\(-64\), but not compact bases, full parity dimensions, Hall constants,
Jacobi/Serre verification, completed Hopf pairing, or the closed radical
quotient.

## Commands run

- `sed -n` / `nl -ba` reads of `.agents/skills/chriss-ginzburg-rectify/SKILL.md`,
  `CLAUDE.md`, `AGENTS.md`, ecosystem instruction excerpts, relevant
  `notes/` reports, and targeted `main.tex` regions.
- `rg` scans for primitive recognition, Hopf pairing, radical quotient,
  PBW, full parity dimensions, and the
  \(\delta_1+\delta_2+\delta_3\) channel.
- `python3 compute/verify_square_root.py`: confirmed
  \(f(1,1)=-64\) in the \(q^1r^1\) coefficient of \(\phi_{0,1}\).
- `git diff --check -- main.tex notes/next_recognition_attack_heal_report.md`:
  passed.
- `git diff --check`: passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-next-recognition-texcheck main.tex`:
  passed after creating the temporary output directory.  The single pass
  reports expected unresolved references/citations because it was not a
  full `make` build.
- `git add main.tex notes/next_recognition_attack_heal_report.md`
- `git diff --cached --check`: passed.
