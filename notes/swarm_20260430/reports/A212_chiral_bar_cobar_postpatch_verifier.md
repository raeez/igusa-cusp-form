# A212 Chiral-Bar-Cobar Postpatch Verifier

## Fatal Finding

`~/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex` still had
earlier synthesis remarks promoting Class-S/W/Frenkel--Kac data to
`\mathbf H_{\Delta_5}` recognition. Around line 5651 the text said the
VOA representation theory matches `\mathbf H_{\Delta_5}`; around
5691--5703 it said the K3 Fock vertex-operator closure is exactly
`\mathbf H_{\Delta_5}|_{\hbar\to0}` and then quantizes it. This
contradicts the later corrected theorem, which requires `(R1)`--`(R5)`
and otherwise proves only a completed character target.

## High Findings

None in `arithmetic_shadows.tex`, `feynman_diagrams.tex`, or the
product-exponent implementation. Checked anchors remained conditional,
scalar, or target-level.

## Medium Finding

`compute/tests/test_cy_bkm_algebra_engine.py` did not directly test the
new three-argument `borcherds_exponent(n0, ell, m0)` convention. The
code currently implements `N=n0*m0`, but a regression to the left
coordinate would not be caught by the existing tests.

## Checks

- `git diff --check -- <scoped files>` clean.
- `./.venv/bin/python -m unittest compute.tests.test_cy_bkm_algebra_engine`
  passed: 137 tests.
- Direct sanity sample:
  `borcherds_exponent(1,0,2)=1616`, matching
  `2*phi01_coeff(2,0)`.

## Status

Patch delegated to A215.

