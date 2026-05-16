# A130 -- K3 Chiral Algebra Signed-Dimension Patch

## Claim Attacked

`chapters/examples/k3_chiral_algebra.tex` asserted a constant total root
multiplicity per level and identified level multiplicities with
\(|c(D)|\).

## Patch

The stale proposition was replaced by a signed root character /
Hall-recognition-gate statement. The finite-check prose now describes
signed Borcherds coefficient extraction and keeps ordinary dimensions
behind parity fixture or finite Hall--Borcherds recognition data. The
later levelwise-24 claim in the BKM positive-part paragraph was removed.

## Verification

Targeted searches found no remaining `|mult|` hits. `|c(D)|` remains
only in asymptotic-growth contexts. The repaired statement contains
explicit `superdimension` language.

```text
git diff --check -- chapters/examples/k3_chiral_algebra.tex
```

passed.

## Residual Caveat

Stale compute/test assumptions remain in:

- `compute/lib/k3e_relative_chiral_algebra.py`
- `compute/lib/physical_k3_sigma_check.py`
- `compute/tests/test_k3e_relative_chiral_algebra.py`

These are assigned to A137.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_chiral_algebra.tex`
