# The integrated monograph

`make` → `out/platonic.pdf` — **507 pages, 0 LaTeX errors, 0 undefined
references, 0 undefined citations.** This is the default target: a plain build
produces the current, merged monograph.

Home volume of this repository: **Volume III — Igusa–Borcherds Theory**, placed first.

## One spine, five volumes

| volume | lines | home repository |
|---|---:|---|
| I Ordered Chiral Geometry | 1552 | `chiral-bar-cobar` |
| II Mixed HT Deligne Theory | 929 | `mixed-holomorphic-topological-strings` |
| III Igusa–Borcherds Theory | 1427 | `igusa-cusp-form` |
| IV Calabi–Yau Quantum Groups | 1279 | `calabi-yau-quantum-groups` |
| V Universal Chiral BV, Einstein Completion | 847 | — |

The five volume files, `platonic.sty`, `integrated_macros.tex`, and
`references.bib` are **byte-identical in every repository** (SHA-256
verified). Editing one here forks it from every other copy. Each repository
differs only in its `00_home.tex` frame and the order of the volumes.

## Merged in — `Volume_I_audit_and_obstructions.tex`

The spine as shipped had no audit of the legacy planar tables and no
obstruction constitution: `Motzkin`, `Riordan`, `Goncharova`,
`pentagonal`, and `no-go` all occurred zero times across all five volumes.
Both are now merged in, in the spine's own notation:

- **Bar–Chevalley comparison** and the simple-Lie calculation:
  $\mathfrak{sl}_2 \to 1+t^3$, $\mathfrak{sl}_3 \to 1+t^3+t^5+t^8$,
  $\mathfrak g_2 \to 1+t^3+t^{11}+t^{14}$.
- **Pentagonal rigidity.** For the positive Witt algebra,
  $\dim H^n(\mathrm{Bar}^\perp U(L_1)) = 2$ for every $n\ge1$, in the
  weights $(3n^2\mp n)/2$, with Euler character $\prod_{n\ge1}(1-q^n)$
  saturating it degree by degree. Verified $n=1,2,3,4$.
- **The two sequences are one sequence.** $M(n)=R(n)+R(n+1)$, so the
  Virasoro sequence is $R(n+2)-R(n)$ and the $\mathfrak{sl}_2$ sequence is
  $R(n+3)$. The shared discriminant carries no Drinfeld–Sokolov content.
- **Carrier theorem**: neither planar sequence is the bar homology of the
  algebra it names, nor a bar chain count; they agree with the truth at
  $n=2$ alone.
- **Where a mixed distributive law can live**: only on the image of the
  aligned idempotent. Located, not constructed.
- **Seven obstruction theorems**: no quantum group from dimension loss, no
  modular object from topology alone, no bulk from a boundary centre, no
  classification by central charge, no identification of anomalies of
  different types, no unnamed comparison of bars, no homology from a scalar
  sequence.

The last of these is what retracts the $5\times5$ $\kappa$-matrix and the
Universal Trace Identity, rather than merely omitting them.

## Typography

EB Garamond via `raeez-math-template` with `localtheorems`, so
`platonic.sty`'s fifteen theorem environments stand. In `platonic.sty` the
`newtxtext`, `newtxmath`, `fontenc`, `inputenc`, `imakeidx`, and
`bm` loads are delegated to the template — `imakeidx` because the template
already calls `\makeindex`, `bm` because the template's `newtxmath`
exhausts LaTeX's sixteen-alphabet budget. No mathematical content was touched.

## Verification

`chiral-bar-cobar/compute/` carries two independent harnesses, cross-checked:
exact `Fraction` sparse elimination with $d^2=0$ asserted per space, and
sympy dense matrices. They share one claim, $H^*(\mathfrak{sl}_2)=1,0,0,1$,
and agree with no shared code, basis, sign convention, or backend. 23 tests.

## Still open

No $\lambda$ is constructed for any example, so the doubly noncommutative
object remains a definition without a model; the anticommutation of the two
edge-contraction differentials rests on determinant-line independence that no
witness proves; the genus-two-and-above analytic material is unported.
