# Next D0 attack-heal report

Date: 2026-04-28.
Worktree: `/tmp/igusa-next-d0`.
Branch: `agent/igusa-next-d0-20260428`.

## Claim attacked

The attacked claim was that the finite first-order `D0` inscription could
still be read as an existence theorem once the words "transition maps",
"source observable shadow", and "Pfaffian normalization" appeared.

Status: false as an existence theorem.  Safe as a conditional finite
certificate after the residuals below are supplied and vanish.

## Manuscript changes

- `main.tex`: rewrote hypothesis `(D0)` of
  `thm:dirac-pfaffian-recognition-conditional` so it requires finite
  stages `D_{0,R}`, transition maps, source/observable comparison maps,
  and vanishing stage residual tuple `\mathfrak O_{D_0,R}` before forming the
  HN-completed object.
- `main.tex`: strengthened `def:first-order-d0-certificate` by adding the
  nonzero-degree target exponent
  \[
  a_\Delta(n,l,m)=
  \begin{cases}
  f(nm,l),& (n,l,m)\in\Gamma_{\mathrm{eff}},\\
  0,& (n,l,m)\notin\Gamma_{\mathrm{eff}},
  \end{cases}
  \]
  so the finite Pfaffian test detects extra signed primitive support
  outside the Borcherds cone.
- `main.tex`: added finite transition residuals
  `\mathfrak o^{\mathrm{tr}}_{R'R}` and a finite
  source/observable residual `\mathfrak o^{obs}_R`.
- `main.tex`: enlarged
  `\mathfrak O_{D_0,R}` to include transition, observable, Hochschild,
  triple, Jacobi, cyclic, support/parity, and leading-coefficient
  defects.
- `main.tex`: retitled the theorem as a finite first-order certificate
  theorem and sharpened the open problem so D0 remains a construction
  target, not a theorem of this paper.

## Constants and formulas

- Normal-ordered product:
  \[
  (c,T)\star(c',T')=(c+c',T+T'+B(c,c')),\qquad
  \overline\Pi_X(c,T)=\Pi_X(c)-T.
  \]
- Finite support:
  \[
  \widehat\Gamma_R=\{(c,T)\mid c\in\Gamma_R^{HN},\ T\in\mathcal T_R(c)\},
  \qquad
  \Gamma_R^\Pi=\overline\Pi_X(\widehat\Gamma_R).
  \]
- Pfaffian normalization target:
  \[
  \operatorname{pf}_{X,R}|_{\mathfrak c_\infty}
  =
  64q^{1/2}r^{1/2}s^{1/2}
  \prod_{\substack{\gamma\in\Gamma_R^\Pi\\ \gamma\ne0}}
  (1-x^\gamma)^{\operatorname{sdim}P^\Pi_{R,\gamma}},
  \qquad
  \mathfrak o^{\mathrm{par}}_{R,\gamma}
  =
  \operatorname{sdim}P^\Pi_{R,\gamma}-a_\Delta(\gamma).
  \]
- Residual tuple:
  \[
  \mathfrak O_{D_0,R}=
  (\{\mathfrak o^{\mathrm{tr}}_{R'R}\}_{R'\ge R},
  \{\mathfrak o^{or}_{R,\mathcal C}\}_{\mathcal C},
  \mathfrak o^{obs}_R,
  \mathfrak o^{\mathrm{Hoch}}_{\Theta,R},
  \mathfrak o^{\mathrm{tri}}_{\Theta,R},
  \mathfrak o^{\mathrm{Jac}}_{\Theta,R},
  \mathfrak o^{\mathrm{cyc}}_{\Theta,R},
  \{\mathfrak o^{\mathrm{par}}_{R,\gamma}\}_{\gamma\in\Gamma_R^\Pi,\ \gamma\ne0},
  \mathfrak o^{\mathrm{lead}}_R).
  \]

## Proof-status recommendation

- Proved: finiteness of `\widehat\Gamma_R` and additivity of
  `\overline\Pi_X` are lattice consequences of the finite-HN support
  lemma and `lem:b-cocycle-central-extension`.
- Imported: `\mathsf{Den}_{\Delta_5,E}`, `\mathfrak g_{\Delta_5}`, and
  the product with leading coefficient `64`.
- Conditional: a supplied finite-stage `D0` certificate with
  `\mathfrak O_{D_0,R}=0` for all stages supplies every later use of
  `(D0)`.
- Open: construction of the compact state-side Hall object, transition
  cocycles, quotient/orientation trivializations, source/observable
  comparison, negative-cyclic normal-ordering lift, Pfaffian line, and
  compact parity pieces.

## Remaining obligations

Construct the finite stages `D_{0,R}`.  Prove transition compatibility.
Compute and trivialize `\mathfrak O_{D_0,R}` for all stages.  Only then
may the HN-completed compact first-order object be formed and compared
with the imported Borcherds target.

## Commands run

- `git diff --check` -- passed.
- `python3 compute/verify_lattice.py` -- passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-next-d0-texcheck main.tex` -- passed as a one-pass syntax check; expected unresolved reference and citation warnings remain because BibTeX and reruns were not invoked.
