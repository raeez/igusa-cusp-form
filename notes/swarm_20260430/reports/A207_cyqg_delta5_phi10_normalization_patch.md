# A207 -- CYQG Delta5/Phi10 normalization patch

## Claim attacked

Vol III conflated the Borcherds square-root normalization for
\(\Delta_5\) with the doubled \(K3\) elliptic-genus normalization for
\(\Phi_{10}^{\mathrm{un}}=\Delta_5^2\).

## Result

No fatal obstruction after patch. The repair separates \(\Delta_5\)
exponents \(c_0(D)\) from the doubled \(Z_{K3}=2\phi_{0,1}\) /
\(\Phi_{10}^{\mathrm{un}}\) exponents \(2c_0(D)\).

## Files changed

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex`
- `/Users/raeez/calabi-yau-quantum-groups/notes/physics_bps_root_multiplicities.tex`
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/k3e_coha_structure.py`
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_k3e_coha_structure.py`

## Verification

The executable three-path check now compares the discriminant table,
direct \(\phi_{0,1}\) coefficient extraction, and source constants with
the factor-two boundary explicit. A negative regression corrupting path
one is present.

Commands reported:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider compute/tests/test_k3e_coha_structure.py
git diff --check -- chapters/examples/k3e_cy3_programme.tex notes/physics_bps_root_multiplicities.tex compute/lib/k3e_coha_structure.py compute/tests/test_k3e_coha_structure.py
```

Status: `98 passed`; diff check clean.

## Residual obligation

Keep every cross-volume use of \(\Delta_5\), \(Z_{K3}\), and
\(\Phi_{10}^{\mathrm{un}}\) factor-aware. Signed superdimension remains
the correct status; it is not a cardinality statement.
