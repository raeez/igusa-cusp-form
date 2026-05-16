# A215 Chiral Synthesis/Test Hardening Patch

## Claim Attacked

A212 found one remaining `w_algebras_deep.tex` fatal: early Class-S/W/
Frenkel--Kac synthesis remarks still promoted target data to
`\mathbf H_{\Delta_5}` recognition. A212 also found that the
three-argument Jacobi-index convention was not directly tested.

## Patch

- `~/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex` around
  5651 now frames the Class-S/W comparison as scalar, Schur-character,
  and classical K3 Fock-space target comparison conditional on `(R1)`--
  `(R5)`.
- The Frenkel--Kac closure around 5703 is now a classical target
  comparison with an explicit `(R1)`--`(R5)` upgrade path to
  `\mathbf H_{\Delta_5}` recognition.
- `~/chiral-bar-cobar/compute/tests/test_cy_bkm_algebra_engine.py`
  now directly tests
  `borcherds_exponent(1,0,2)=1616=2*phi01_coeff(2,0)` and that it
  differs from legacy two-argument `borcherds_exponent(1,0)=216`.

## Checks

- Targeted `rg` confirmed new recognition-conditional anchors.
- `git diff --check -- chapters/examples/w_algebras_deep.tex compute/tests/test_cy_bkm_algebra_engine.py`
  passed.
- `./.venv/bin/python -m unittest compute.tests.test_cy_bkm_algebra_engine`
  passed: 138 tests.

## Status

Actual `\mathbf H_{\Delta_5}` recognition remains conditional on
`(R1)`--`(R5)`, now explicitly stated in the early synthesis remarks.

