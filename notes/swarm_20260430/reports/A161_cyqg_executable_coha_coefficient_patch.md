# A161 -- CYQG Executable CoHA Coefficient Patch

## Result

Patched executable CYQG CoHA/Hall coefficient code so signed Jacobi/Borcherds
coefficients are not exposed as ordinary dimensions without an explicit
parity-resolved fixture or source datum.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/elliptic_hall_hocolim.py`
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_elliptic_hall_hocolim.py`
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3e_coha_structure.py`
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_k3e_coha_structure.py`

## Changes

- Recast `abs(c(D))` APIs as signed-character / unsigned coefficient
  magnitude statistics.
- Made `coha_dimension` and local dimension APIs require an explicit
  parity-resolved fixture/source.
- Updated tests to assert unsourced dimensions raise, while sourced finite
  parity fixtures work.
- Preserved finite sanity checks for known \(\phi_{0,1}\) coefficients and
  magnitude totals.

## Checks

- `python3 -m py_compile compute/lib/elliptic_hall_hocolim.py compute/tests/test_elliptic_hall_hocolim.py compute/lib/k3e_coha_structure.py compute/tests/test_k3e_coha_structure.py`
- `pytest compute/tests/test_k3e_coha_structure.py compute/tests/test_elliptic_hall_hocolim.py`
  returned `175 passed in 6.67s`.
- `git diff --check -- compute/lib/elliptic_hall_hocolim.py compute/tests/test_elliptic_hall_hocolim.py compute/lib/k3e_coha_structure.py compute/tests/test_k3e_coha_structure.py`

## Caveat

`python3 -m pytest` was unavailable in that environment because system
`python3` had no `pytest`; direct `pytest` was available and passed.
Actual CoHA dimensions remain intentionally unavailable without
parity/source fixtures. The new test fixtures are finite executable
guards, not geometric dimension proofs.

