# A202 Chiral Arithmetic/Feynman/Compute Follow-Up Patch

## Claim Attacked

Residual `~/chiral-bar-cobar` text and code still risked promoting
scalar Igusa/Humbert/Schur/Feynman data to BKM source recognition, and
the finite exponent helper documented the wrong product-index
convention.

## Patch

- `chapters/connections/arithmetic_shadows.tex` now frames
  Igusa/Humbert/H^2/Schur material as scalar or comparison targets with
  explicit upgrade criteria. The decisive-test/completed language was
  removed, and the `H^2` block was moved from `ProvedElsewhere` to
  conditional recognition.
- `chapters/connections/feynman_diagrams.tex` now says the K3 vertex
  closure maps to the denominator datum until root/parity/completion/PBW/
  no-extra-root comparisons are proved.
- `compute/lib/cy_bkm_algebra_engine.py` now documents and implements
  the product exponent through the Jacobi product index `N=n_0m_0` and
  `ell`. The two-argument `borcherds_exponent(n, ell)` remains
  backward-compatible as an already formed Jacobi-index lookup.

## Checks

- Targeted `rg` for the named residual phrases: no matches.
- `git diff --check --` on the three changed files passed.
- `./.venv/bin/python -m unittest compute.tests.test_cy_bkm_algebra_engine`
  passed: 137 tests OK.

## Status

Accepted pending A212 read-only verification over the combined A199/A202
chiral-bar-cobar patch surface.

