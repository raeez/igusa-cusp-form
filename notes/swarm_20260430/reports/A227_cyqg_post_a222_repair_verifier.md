# A227 -- CYQG post-A222 repair verifier

## Result

The three-path verifier and local signed-character manuscript passage are
fixed. One stale docstring issue remained when A227 ran.

## Findings

Residual:

- `compute/lib/k3e_coha_structure.py` still said "via the DMVV formula +
  phi_{0,1}" and `_extract_rank_r_from_dmvv` still called the \(c(D)\)
  lane the DMVV product.

Cleared:

- Known discriminants are recorded even when path 1 is zero/missing.
- The test suite contains a deletion/missing-discriminant regression.
- The local constancy passage uses signed root-character
  \(\operatorname{sch}\).

## Integration

The main thread repaired the remaining stale docstrings and comments.

## Verification

After integration: stale-DMVV grep returned no hits; `99` CYQG tests
passed.
