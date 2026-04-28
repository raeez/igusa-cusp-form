---
name: chriss-ginzburg-rectify
description: Use when a section, introduction, theorem lane, or proof region of the Igusa Square Root manuscript needs full structural fortification rather than a local patch. This is the Codex-native equivalent of `/chriss-ginzburg-rectify` from `CLAUDE.md`.
---

# Chriss-Ginzburg Rectify — Igusa cusp form

Use this when the text must be reimagined, not merely corrected.

## Load first

- `~/ecosystem/INVARIANTS.md`
- `CLAUDE.md`
- `AGENTS.md`
- `main.tex` — the full target region in context
- `proj.bib` — primary sources for any cited result
- `appendices/` (e.g., `boundary_compatibility_conditions.tex`)
- `notes/` — recent attack-heal traces and pattern logs
- `compute/verify_lattice.py`, `compute/verify_square_root.py` for numerical anchors
- the directly cited dependencies

## Five-phase loop

1. Diagnose the real organizing question of the region.
2. Find the unique survivor: the theorem, identity, or modular relation
   the section must actually carry — the Borcherds determinant of $\phi_{0,1}$,
   the BKM denominator identity, the $K3 \times E$ realization comparison,
   or the Igusa $\Delta_5$ square-root.
3. Rebuild the structure: move the first real coefficient computation
   earlier, cut decorative transitions, front-load lattice / Weyl-vector /
   multiplier prerequisites, weaken any sentence whose proof support is
   not yet there.
4. Rewrite from scratch where patching preserves bad architecture.
5. Run a hostile Beilinson audit and repeat until `CONVERGED` or `BLOCKED`.

## Convergent writing standard

For introductions, prefaces, and abstracts, use at least three passes.

For section openings and theorem lead-ins, use at least two passes.

Loop:

`WRITE -> REIMAGINE -> REWRITE -> BEILINSON AUDIT -> REIMAGINE AGAIN -> REWRITE AGAIN -> CONVERGE`

## Structural moves

Prefer:

- deficiency opening (the obstruction the section resolves)
- unique survivor (one theorem or identity, named)
- instant computation (a Fourier coefficient, a Weyl vector, a Borcherds exponent)
- forced transition (the next move follows from the present obstruction)
- decomposition table (lattice strata, Heegner divisors, Humbert surfaces)
- dichotomy (paramodular vs. orthogonal, BKM vs. Kac-Moody, weak vs. holomorphic)
- sentence-as-theorem

## Stop rule

Do not keep polishing a strong false sentence. Demote it, split it, or
fence it. A weakened true theorem ranks above a polished false one.
