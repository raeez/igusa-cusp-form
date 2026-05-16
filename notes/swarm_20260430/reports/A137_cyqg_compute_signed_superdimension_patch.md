# A137 -- CYQG Compute Signed-Superdimension Patch

## Claim Attacked

CYQG compute files retained stale assumptions that total root
multipity per level is \(24\), or that \(|c(D)|\) is a full ordinary
dimension.

## Patch

The owned compute and test files now treat \(c(D)\) and level sums as
signed Borcherds superdimension / character data. Ordinary dimensions
are gated by a parity fixture or target presentation; compact source
dimensions are gated by finite Hall--Borcherds recognition.

The compatibility alias `total_root_mult_per_level()` remains, but owned
tests now use `signed_root_superdimension_per_level()`.

## Verification

```text
pytest compute/tests/test_k3e_relative_chiral_algebra.py
pytest compute/tests/test_physical_k3_sigma_check.py
python3 -m py_compile compute/lib/k3e_relative_chiral_algebra.py compute/lib/physical_k3_sigma_check.py compute/tests/test_k3e_relative_chiral_algebra.py
git diff --check -- compute/lib/k3e_relative_chiral_algebra.py compute/lib/physical_k3_sigma_check.py compute/tests/test_k3e_relative_chiral_algebra.py
```

The pytest runs passed with `83 passed` and `73 passed`; compile and
diff checks passed.

## Residual Caveat

Ordinary root-space dimensions are still not computed. The patch records
signed character data and absolute coefficient sums as non-dimensional
statistics.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3e_relative_chiral_algebra.py`
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/physical_k3_sigma_check.py`
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_k3e_relative_chiral_algebra.py`
