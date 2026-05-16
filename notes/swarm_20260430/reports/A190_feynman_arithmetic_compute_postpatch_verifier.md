# A190 -- Feynman / Arithmetic / Compute Postpatch Verifier

## Result

Read-only verification found one remaining feynman-diagrams Schur/Igusa
residue overclaim; other scoped lanes were clean.

## Finding

- Residual: `feynman_diagrams.tex:1732` still had an ungated
  Schur/Igusa-style Humbert-pole residue remark. The prior Schur paragraph
  was correctly conditional at `1707`, but the next remark said Nekrasov
  residues equal Jacobi coefficients and the Beem--Rastelli/Liouville
  character equals \((\Phi_{10}^{\mathrm{un}})^{-1}\) at `1749`.

## Passes

- `feynman_diagrams.tex:1171`, `1505`: \(\Delta_5\)/Feynman target is
  heuristic/conditional.
- `feynman_diagrams.tex:1571`: CoHA/Yangian distinction is explicit.
- `arithmetic_shadows.tex:13728`: Bruinier reciprocity no longer routes
  arbitrary Lie-bialgebra cocycles into chain recognition.
- `cy_bkm_algebra_engine.py:8`, `27`, `1238` and
  `test_cy_bkm_algebra_engine.py:1008`: compute docs separate finite
  model, signed Borcherds exponents, scalar shadow, K3 elliptic genus, and
  \(\phi_{-2,1}\) lane.

## Checks

- `git diff --check -- <target files>` passed.
- `.venv/bin/python -m pytest compute/tests/test_cy_bkm_algebra_engine.py`
  returned `138 passed in 7.24s`.
- Targeted `rg` found no arbitrary-cocycle/chain-recognition pipeline.

## Main-Thread Follow-Up

The main thread gated the Humbert-pole residue remark as a finite scalar
target comparison requiring finite Schur--Igusa recognition.

