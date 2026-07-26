# The integrated monograph

`make` → `out/platonic.pdf` — **507 pages, 0 LaTeX errors, 0 undefined
references, 0 undefined citations.** This is the default target: a plain build
produces the current, merged monograph.

## This repository

**not a numbered volume**. *The Igusa Square Root* is a standalone monograph in its own space, with its own opening (`00_integral_igusa.tex`) and closing (`99_integral_closure.tex`) chapters, leading with its own subject. The programme volumes follow as background, not as a sequence this work belongs to.

## The programme, and what stands outside it

| | subject | repository |
|---|---|---|
| **I** | Ordered Chiral Geometry | `chiral-bar-cobar` |
| **II** | Mixed Holomorphic–Topological Deligne Theory | `mixed-holomorphic-topological-strings` |
| **III** | Calabi–Yau Quantum Groups | `calabi-yau-quantum-groups` |
| — | Universal Chiral BV and Einstein Completion | no repository yet |
| — | Igusa–Borcherds theory, *The Igusa Square Root* | `igusa-cusp-form`, standalone |

The upstream spine ships five files whose names run `Volume_I` …
`Volume_V`, with Igusa–Borcherds at `III` and Calabi–Yau at `IV`. Those
filenames are upstream identifiers and are **not** the programme numbering:
Calabi–Yau is Volume III, and the Igusa material belongs to a standalone
monograph rather than to the volume sequence. The filenames were left
untouched so that the files stay byte-identical across repositories; do not
renumber them.

## One spine

The five volume files, `platonic.sty`, `integrated_macros.tex`, and
`references.bib` are **byte-identical in every repository** (SHA-256
verified). Repositories differ only in their own opening and closing chapters
and in which volume they read first. Editing a volume file here forks it from
every other copy.

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
  $R(n+3)$; the shared discriminant carries no Drinfeld–Sokolov content.
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

The last is what retracts the $5\times5$ $\kappa$-matrix and the Universal
Trace Identity, rather than merely omitting them.

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
