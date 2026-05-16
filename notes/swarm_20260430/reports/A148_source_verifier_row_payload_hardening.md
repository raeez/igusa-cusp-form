# A148 -- Source Verifier Row-Payload Hardening

## Changed Paths

- `compute/verify_source_fixture.py`
- `certificates/sources/k3e_compact_hall/README.md`

## Patch

The source verifier now requires mathematical payload fields, not just
status or comment fields. Status-only rows, including
`check_status=verified`, do not supply a gate. Partial payload rows are
rejected with explicit missing-column diagnostics.

`degrees.csv` rows now require `source_block_status` in
`source_verified,source_admissible`. The README records this rule.

## Verification

```text
python3 -m py_compile compute/verify_source_fixture.py
python3 compute/verify_source_fixture.py --source certificates/sources/k3e_compact_hall --check
python3 compute/verify_source_fixture.py --source certificates/sources/k3e_compact_hall --target certificates/targets/delta5_gn_kac/a071_target_presentation --check
git diff --check -- compute/verify_source_fixture.py certificates/sources/k3e_compact_hall/README.md
```

Compile passed. Current packet checks returned `BLOCKED`.
Temporary probes with only `check_status=verified`, bad
`source_block_status`, and partial payload rows also returned `BLOCKED`.

## Residual Limitation

The current packet remains `mock_empty_blocked`, header-only, and
non-certifying. The verifier proves fail-closed behavior here; it does
not certify any compact Hall source stage.
