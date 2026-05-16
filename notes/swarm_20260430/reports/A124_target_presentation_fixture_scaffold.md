# A124 -- Target Presentation Fixture Scaffold

## Changed Paths

- `compute/build_target_presentation_fixture.py`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/manifest.yaml`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/hashes.sha256`
- all A111 `target_*.csv` files

## Commands

```text
python3 -m py_compile compute/build_target_presentation_fixture.py
python3 compute/build_target_presentation_fixture.py --out certificates/targets/delta5_gn_kac/a071_target_presentation --force
python3 compute/build_target_presentation_fixture.py --out certificates/targets/delta5_gn_kac/a071_target_presentation --check
cd certificates/targets/delta5_gn_kac/a071_target_presentation && shasum -a 256 -c hashes.sha256
python3 compute/verify_square_root.py
git diff --check -- compute/build_target_presentation_fixture.py certificates/targets/delta5_gn_kac/a071_target_presentation
```

All passed.

## Mathematical Scope

The fixture is target-only. It encodes only the justified promoted rows:

- \(2a_{ij}:10|0\)
- \(C_{k,3}:29|93\)
- \(C_{k,4}:10|0\)
- \(C_{k,5}:0|0\)

\(C_{k,2}\) and \(2\delta_{123}\) are recorded as `signed_only_blocked`
and do not feed basis or PBW certification. No compact Hall
representatives, source pairings, source radicals, source PBW, or
no-extra theorem are supplied.
