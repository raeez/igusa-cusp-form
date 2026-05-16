# Sixth primitive recognition presentation attack-heal report

Date: 2026-04-28.

## Claim attacked

The attacked shortcut was:
\[
\text{signed denominator data through } W_{\le3}
\quad\Longrightarrow\quad
\text{presentation-level recognition of } \mathfrak g_{\Delta_5}.
\]

The attack succeeds.  Dimension equality and Borcherds product
coefficients do not produce compact generators, parities, relation
constants, a Hopf pairing, the closed radical quotient, a
no-extra-relations theorem, or completed PBW.  The strongest stable
statement remains the conditional finite-window theorem on \(W_{\le3}\).

The requested file `notes/sixth_attack_heal_swarm_20260428.md` is not
present in this isolated worktree.  The available prior recognition
reports were under `notes/notes/`, especially the third, fourth, next, and
fifth recognition/PBW reports.

## Repairs inscribed

- `main.tex`: extended Proposition
  `prop:first-saturated-primitive-recognition-window` past the existing
  \(W_{\le3}\) certificate.  The proposition now records a height-four
  obstruction rather than upgrading the recognition theorem.
- `main.tex`: added the first height-four timelike signed gaps:
  \[
  \smult(2\delta_1+\delta_2+\delta_3)
  =\smult(\delta_1+2\delta_2+\delta_3)
  =\smult(\delta_1+\delta_2+2\delta_3)=108,
  \]
  while the additive simple coefficients in the same degrees are \(90\).
  The signed residual is \(18\) in each degree.
- `main.tex`: added doubled isotropic checks:
  \[
  \smult(2\delta_i+2\delta_j)=10,\qquad
  \tau(2(\delta_i+\delta_j))=9,
  \]
  hence signed non-simple residual \(1\) on each doubled isotropic ray.
- `main.tex`: added the height-four real-string obligation from the odd
  \(\delta_{123}\) simple generators:
  \[
  (\delta_i,\delta_{123})=-2,\qquad
  1-2(\delta_i,\delta_{123})/(\delta_i,\delta_i)=3.
  \]
  Thus \((\operatorname{ad}e_i)^3w_s=0\) and the first odd maps
  \([e_i,w_s]\) land in the height-four timelike blocks.
- `compute/verify_square_root.py`: added exact checks for signed root
  supermultiplicities, additive \(m(a)\)-coefficients, doubled isotropic
  gaps, and real-string exponents.

## Exact constants

Already-stable first window:
\[
\delta_i:1|0,\qquad
\delta_i+\delta_j:10|0,\qquad
2\delta_i+\delta_j:1|0,\qquad
\delta_{123}:29|93.
\]

First timelike coefficient:
\[
[qrs]D_5/(qrs)^{1/2}=93,\qquad
m(\delta_{123})=-93,\qquad
29-93=-64=f(1,1).
\]

Next additive checks:
\[
m(2\delta_1+\delta_2+\delta_3)
=m(\delta_1+2\delta_2+\delta_3)
=m(\delta_1+\delta_2+2\delta_3)=90,
\]
\[
m(2\delta_{123})=-540.
\]

New height-four obstruction:
\[
\smult(2\delta_1+\delta_2+\delta_3)
=\smult(\delta_1+2\delta_2+\delta_3)
=\smult(\delta_1+\delta_2+2\delta_3)=108,
\]
so the net signed lower-word/radical residual is \(108-90=18\).

Doubled isotropic obstruction:
\[
\smult(2(\delta_i+\delta_j))=10,\qquad
\tau(2(\delta_i+\delta_j))=9,\qquad
10-9=1.
\]

Real-string checks:
\[
(\delta_i,\delta_j)=-2,\quad
1-2(\delta_i,\delta_j)/(\delta_i,\delta_i)=3,
\]
\[
(\delta_i,\delta_i+\delta_j)=0,\quad
(\delta_k,\delta_i+\delta_j)=-4,\quad
1-2(\delta_k,\delta_i+\delta_j)/(\delta_k,\delta_k)=5,
\]
\[
(\delta_i,\delta_{123})=-2,\quad
1-2(\delta_i,\delta_{123})/(\delta_i,\delta_i)=3.
\]

## Residual obstruction

Full primitive recognition is still blocked at presentation level.  A
compact source must still supply:

- parity-homogeneous compact representatives for every simple-root fibre;
- the Chevalley, real Serre, isotropic orthogonality, and real-string
  relations in the compact Hall bracket;
- compact \(29|93\) bases in \(\delta_{123}\), plus the height-four odd
  maps \([e_i,w_s]\);
- positive-negative Hopf-pairing matrices and closed radical kernels;
- equality of the compact radical with the standard GN/Kac radical;
- finite kernel equality for every saturated window;
- completed PBW compatibility and strict transition maps.

The height-four signed gap \(18\) is not a count of compact PBW words.  It
is the first reproducible signal that adding the new additive coefficients
does not extend the finite recognition theorem.

## Commands run

- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`,
  `/Users/raeez/ecosystem/INVARIANTS.md`,
  `/Users/raeez/ecosystem/AGENTS-HARNESS.md`, and the
  `chriss-ginzburg-rectify` skill.
- `rg` and `nl -ba` reads of the primitive recognition theorem, low-degree
  bracket proposition, finite-window proposition, imaginary simple-root
  definition, coefficient script, and prior recognition reports.
- `python3 compute/verify_square_root.py`: passed.  It printed the
  \(29|93\) split, \(90,90,90,-540\), the height-four
  `signed|m|gap` triples \(108|90|18\), doubled isotropic
  `signed|tau|gap` triples \(10|9|1\), and the real-string exponents
  \(3,5,3\).
- `python3 -m py_compile compute/verify_square_root.py`: passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-sixth-recognition-texcheck main.tex`:
  passed.  The single pass reported expected unresolved references and
  citations because it was not a full `make` build.

## Files changed

- `main.tex`
- `compute/verify_square_root.py`
- `notes/sixth_recognition_presentation_attack_heal_report.md`
