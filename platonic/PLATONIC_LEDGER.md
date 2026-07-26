# Platonic-integrated deployment — The Igusa Square Root

`make platonic` → `out/platonic.pdf`, **501 pages, 0 LaTeX errors, 0
undefined references, 0 undefined citations.**

## What was deployed

The upstream source bundle, entire. This repository's home volume is
**Volume III**; its own opening and closing chapters are `00_integral_igusa.tex`, `99_integral_closure.tex`.

## The shared spine

Five volume files are **byte-identical** across the Calabi–Yau and Igusa
bundles — one canonical spine, 6,034 lines, verified by SHA-256:

| file | lines | repository whose subject it is |
|---|---:|---|
| `Volume_I_Ordered_Chiral_Geometry.tex` | 1552 | `chiral-bar-cobar` |
| `Volume_II_Mixed_HT_Deligne_Theory.tex` | 929 | `mixed-holomorphic-topological-strings` |
| `Volume_III_Igusa_Borcherds_Theory.tex` | 1427 | `igusa-cusp-form` |
| `Volume_IV_Calabi_Yau_Quantum_Groups.tex` | 1279 | `calabi-yau-quantum-groups` |
| `Volume_V_Universal_Chiral_BV_and_Einstein_Completion.tex` | 847 | no repository yet |

`platonic.sty`, `integrated_macros.tex`, and `references.bib` are likewise
identical between the two bundles. Editing a spine file here forks it from the
other repository's copy; the spine is shared, not owned.

## Typography

`newtxtext`/`newtxmath` (Times) → EB Garamond via
`raeez-math-template` with `localtheorems`, so `platonic.sty`'s fifteen
theorem environments stand unchanged. In `platonic.sty` the
`newtxtext`, `newtxmath`, `fontenc`, `inputenc`, `imakeidx`, and `bm`
loads are commented out and delegated to the template — `imakeidx` because
the template already loads `makeidx` and calls `\makeindex`, and `bm`
because the template's `newtxmath` leaves no room in LaTeX's sixteen-alphabet
budget. The duplicate `\makeindex` in `main.tex` is likewise disabled. No
mathematical content was touched.

## Mathematics audit

The spine is on the corrected framework, not the retracted one. Occurrence
counts across the five volume files:

| corrected-framework marker | count | | retracted-claim marker | count |
|---|---:|---|---|---:|
| `denominator` | 44 | | Beilinson tower | **0** |
| `aligned` | 34 | | Universal Trace Identity | **0** |
| `associative chiral` | 27 | | five-archetype | **0** |
| `distributive law` | 10 | | KSDual | **0** |
| `two associative` | 2 | | Theorem H | **0** |

Nothing keyed to the Open Beilinson tower, the $5\times5$ $\kappa$-matrix,
the five archetypes, or the Universal Trace Identity survives.

**Gap: `no-go` occurs 0 times.** The obstruction constitution present in
`chiral-bar-cobar/reconstruction/core/part5_audit.tex` has no counterpart
here. The retractions are therefore implicit in the spine rather than stated,
which is the same gap found in the 153-page and 246-page chiral witnesses.

## Cross-repository constant check

`Volume_III_Igusa_Borcherds_Theory.tex` and
`chiral-bar-cobar/reconstruction/core/part4_physics.tex` share the Igusa
normalization, and they agree:

- weight $f(0,0)/2 = 5$ with $f(0,0)=10$, $f(0,\pm1)=1$;
- $\Delta_5^{\theta} = 2^6\,\Delta_5^{\mathrm{mon}} = 64\,D_5$.

The spine is stronger on one point: it **derives** the 64 from the ten even
genus-two theta constants — four characteristics contributing 1 and six
contributing a factor 2, total exponent $(1/2,1/2,1/2)$ — where the chiral
volume quotes it as a normalization. That derivation has been cross-referenced
back into `chiral-bar-cobar`.
