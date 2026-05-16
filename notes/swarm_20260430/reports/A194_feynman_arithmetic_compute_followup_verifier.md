# A194 Feynman/Arithmetic/Compute Follow-Up Verifier

## Claim Attacked

Residual `~/chiral-bar-cobar` text might still identify scalar
Schur/Humbert/Bruinier data with the Igusa BKM object rather than with a
comparison target requiring recognition data.

## Findings

- `chapters/connections/arithmetic_shadows.tex` still had completed
  `H^2`/Igusa classification language and `\ClaimStatusProvedElsewhere`
  wrappers for Bruinier/Humbert/Lusztig/Schur identifications.
- `chapters/connections/feynman_diagrams.tex` still said a K3 vertex
  closure recovers `\mathfrak g_{\Delta_5}` too directly.
- `compute/lib/cy_bkm_algebra_engine.py` documented the finite product
  exponent as depending on the left product index `n` rather than on the
  Jacobi product index `N=n_0m_0` and `ell`.

## Recommendation

Patch these passages into scalar-target/recognition-gate statements and
correct the executable documentation.

## Status

Delegated to A202 with disjoint file ownership.

