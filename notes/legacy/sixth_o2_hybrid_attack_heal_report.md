# Sixth O2/Hybrid Attack-Heal Report

Date: 2026-04-28.
Role: S03 O2/Hybrid.
Worktree: `/tmp/igusa-sixth-o2-hybrid`.
Branch: `agent/igusa-sixth-o2-hybrid-20260428`.
Owned paths: `main.tex`, `notes/sixth_o2_hybrid_attack_heal_report.md`.

## Trusted Context Loaded

- `CLAUDE.md`, `AGENTS.md`, `~/ecosystem/INVARIANTS.md`,
  `~/ecosystem/AGENTS-HARNESS.md`.
- `chriss-ginzburg-rectify` skill from the repo-local skill path.
- Current `main.tex` O2, orientation, hybrid, D0, and compact
  Dirac-Igusa certificate regions.
- Fifth-swarm O2 and hybrid reports:
  `notes/notes/fifth_o2_walls_attack_heal_report.md`,
  `notes/notes/fifth_hybrid_real_attack_heal_report.md`.
- Prior hybrid/O2 reports and integration ledgers under `notes/notes/`.

The named sixth swarm ledger `notes/sixth_attack_heal_swarm_20260428.md`
is not present in this worktree.  `find notes -type f -iname '*sixth*'`
returned no files before this report was created.

## Claim Attacked

Obligations (4) and (5):

1. compute the Pfaffian local model `(O2)` geometrically on the three
   type-II walls;
2. construct the real hybrid source
   `\mathcal F_X^{\mathrm{hyb}}`.

Status: no full construction exists in the worktree.  The stable repair
is a sharper compatibility obstruction.  A compact source cannot claim
O2 wall charts and a hybrid wrapped source independently.  The O2
reduced self-Ext chart must be localized from the same finite hybrid
correspondence source, before the reduced `E` quotient, and must commute
with quotient descent and protected integration.

## Local Computations and Target Checks

The type-II simple roots are

```tex
\delta_1=2f_2-f_3,\qquad
\delta_2=2f_{-2}-f_3,\qquad
\delta_3=f_3.
```

`python3 compute/verify_lattice.py` verified the type-II Gram matrix

```tex
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix}
```

and the Weyl vector

```tex
\rho=f_2-\frac12 f_3+f_{-2}
=\frac12(\delta_1+\delta_2+\delta_3).
```

The inverse degree labels used in the new compatibility obstruction are

```tex
\delta_1\leftrightarrow(1,1,0),\qquad
\delta_2\leftrightarrow(0,1,1),\qquad
\delta_3\leftrightarrow(0,-1,0).
```

Thus the `\delta_2` wall is the immediate wrapped test: its target
monomial has `s`-degree one.  It cannot be supplied by ordinary
projection-finite `Ran(E)` locality.

`python3 compute/verify_square_root.py` verified

```tex
f(0,-1)=1,\qquad f(0,0)=10,\qquad f(0,1)=1,
```

and the existing target checks `[qrs]D_5=93`,
`m(\delta_1+\delta_2+\delta_3)=-93`, and height-four checks
`90,90,90,-540`.  These are target-side checks.  They do not compute
`N_{\delta_i}^{\mathrm{Pf}}`.

## Attacks

`S03-O2H-01` independent-local-chart attack.  A reduced chart
`(U_{\delta_i},u_{\delta_i},K^{red}_{\delta_i})` detached from
`\mathsf{Corr}^{E,hyb}_R` computes at most a local model in another
category.  It does not show that the O2 normal Pfaffian is the local
normal complex of the compact hybrid source.

`S03-O2H-02` wrapped wall attack.  The label
`\delta_2\leftrightarrow(0,1,1)` has positive elliptic degree.  By the
projection-to-`E` obstruction, no finite-support `Ran(E)` chart can be
the source of this wall object.  A local model for `\delta_2` must pass
through rigidified wrapped prequotients and anchors.

`S03-O2H-03` Ext-decomposition attack.  The desired local model must
produce a finite restriction of the unreduced hybrid deformation theory
to a wall object,
`K^E_{\delta_i,R}`, and a quotient-compatible splitting into tangent and
normal factors.  The existing manuscript did not require the O2
splitting to be induced from the hybrid finite stage.

`S03-O2H-04` unit-character attack.  Even if a normal block
`[\mathbb R \xrightarrow{u_i} \mathbb R]` is supplied after quotient, the
unit `\upsilon_{\delta_i,R}` may acquire a quotient or finite-stabilizer
character unless its descent through `Q_{E,R}` is part of the same
finite diagram.

`S03-O2H-05` quotient-first attack.  Forming object quotients before
local/wrapped correspondences destroys anchors and prevents localization
of mixed deformation data at the wall.  Then the reduced normal complex
has no proved source in the unreduced hybrid category.

`S03-O2H-06` Fock-only attack.  A detached Fock/Hecke factor can carry a
scalar `s`-degree and reproduce determinant coefficients.  It has no
wall object, no self-Ext complex, no tangent/normal splitting, no
invariant Pfaffian unit, no mixed correspondence action, and no primitive
bracket.

`S03-O2H-07` protected-integration attack.  The local Pfaffian class must
integrate with the correct `s`-degree and commute with
`\mathfrak o^{I,\mathrm{tr}}_{R'R}`.  A trace degree assigned after
decategorification does not define this compatibility.

## Repair Inscribed

`main.tex` now contains
`prop:o2-hybrid-compatibility-obstruction`.

The proposition inserts the finite compatibility package required for
any real compact source claiming both O2 and the hybrid wrapped object:

```tex
\mathsf{BM}^{E,\mathrm{hyb}}_R
  \to K^E_{\delta_i,R}
  \to K^{E,\mathrm{tan}}_{\delta_i,R}\oplus K^{E,\mathrm{nor}}_{\delta_i,R}
```

must commute with

```tex
Q_{E,R}:\mathsf{BM}^{E,\mathrm{hyb}}_R
\to \mathsf{BM}^{\mathrm{red},\mathrm{hyb}}_R
```

and with the reduced O2 chart

```tex
K^{\mathrm{red}}_{\delta_i,R}
\to K^{\mathrm{tan}}_{\delta_i,R}\oplus K^{\mathrm{nor}}_{\delta_i,R}.
```

It names the new finite residual

```tex
\mathfrak O^{\mathrm{O2/hyb}}_{\delta_i,R}
=
\left(
\mathfrak o^{\mathrm{wall}}_{\delta_i,R},
\mathfrak o^{\mathrm{Ext}\text{-}\mathrm{split}}_{\delta_i,R},
\mathfrak o^{\mathrm{unit}}_{\delta_i,R},
\mathfrak o^{Q,\mathrm{wall}}_{\delta_i,R},
\mathfrak o^{I,\mathrm{wall}}_{\delta_i,R}
\right).
```

Vanishing of this residual means:

- the wall object is an object of the finite hybrid source;
- the reduced self-Ext complex is localized from the unreduced hybrid
  deformation theory;
- the tangent/normal splitting descends through the quotient;
- the normal Pfaffian unit is invariant after quotient orientation
  trivializations;
- protected integration sends the local Pfaffian class to the monomial
  with the displayed `s`-degree and is transition-compatible.

`main.tex` also now points from the local O2 obstruction proposition to
this O2/hybrid compatibility obstruction.

## Exact Remaining Obstructions

For each `i=1,2,3` and finite height `R`, construct:

```tex
x_{\delta_i,R}\in \mathsf{Corr}^{E,\mathrm{hyb}}_R,
\qquad
K^E_{\delta_i,R}
\to K^{E,\mathrm{tan}}_{\delta_i,R}\oplus K^{E,\mathrm{nor}}_{\delta_i,R},
```

compatible with `Q_{E,R}` and the reduced wall chart.

Then prove:

```tex
K^{\mathrm{nor}}_{\delta_i,R}
\simeq [\mathbb R\xrightarrow{u_{\delta_i,R}}\mathbb R],
\qquad
s_{\delta_i}(u_{\delta_i,R})=-u_{\delta_i,R},
```

with invariant unit

```tex
s_{\delta_i}(\upsilon_{\delta_i,R})=\upsilon_{\delta_i,R}
```

and protected integration degree

```tex
I_R^{\mathrm{prot}}
\bigl(Q_{E,R}\operatorname{pf}_{\delta_i,R}\bigr)
\in s^m\mathbb C[q^{\pm1},r^{\pm1}]
```

for `(n,l,m)` equal to the displayed wall label.  The `\delta_2` case
requires wrapped prequotient data because `m=1`.

No actual `x_{\delta_i,R}`, self-Ext complex, rank-one decomposition,
wrapped prequotient, quotient functor, protected integration map, or
transition null-homotopy was constructed in this pass.

## Commands Run

- `pwd`
- `git -C /tmp/igusa-sixth-o2-hybrid status --short --branch`
- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`,
  `/Users/raeez/ecosystem/INVARIANTS.md`,
  `/Users/raeez/ecosystem/AGENTS-HARNESS.md`, and the
  `chriss-ginzburg-rectify` skill.
- `find notes -type f -iname '*sixth*' -print`
- `rg -n` searches for O2, hybrid, type-II walls, Pfaffian, quotient,
  protected integration, eight-word flags, and prior reports.
- `nl -ba main.tex | sed -n ...` reads of the O2 proposition,
  hybrid certificate, no-quotient-first corollary, D0 certificate, and
  Dirac-Igusa `(H_X)` clause.
- `sed -n` reads of fifth and prior O2/hybrid attack-heal reports.
- `python3 compute/verify_lattice.py`: passed.
- `python3 compute/verify_square_root.py`: passed.
- `rg -n -F "prop:o2-hybrid-compatibility-obstruction" main.tex
  notes/sixth_o2_hybrid_attack_heal_report.md`: passed.  An earlier
  over-escaped regex version failed before this fixed-string rerun.
- `git add -N notes/sixth_o2_hybrid_attack_heal_report.md`: used so
  `git diff --check` would include the new report without staging
  content.
- `git diff --check -- main.tex
  notes/sixth_o2_hybrid_attack_heal_report.md`: passed.
- `pdflatex -halt-on-error -interaction=nonstopmode
  -output-directory=/tmp/igusa-sixth-o2-hybrid-texcheck main.tex`:
  passed.  It was a one-pass syntax run and reported expected
  first-pass undefined references/citations, rerun warnings, and layout
  warnings; no fatal TeX error occurred.

## Files Changed

- `main.tex`
- `notes/sixth_o2_hybrid_attack_heal_report.md`
