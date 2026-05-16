# A140 -- Source Verifier Hardening Patch

## Changed Paths

- `compute/verify_source_fixture.py`
- `certificates/sources/k3e_compact_hall/README.md`

## Patch

The verifier/report/help now states that it is check-only; `--check` is
a spelling of the default mode. The verifier rejects `--target == --source`
and rejects target paths lexically or resolved inside the source packet.
Target validation remains path metadata only: existence and directory
type. No target truth is read or derived.

## Verification

```text
python3 -m py_compile compute/verify_source_fixture.py
python3 compute/verify_source_fixture.py --source certificates/sources/k3e_compact_hall --check
python3 compute/verify_source_fixture.py --source certificates/sources/k3e_compact_hall --target certificates/targets/delta5_gn_kac/a071_target_presentation --check
python3 compute/verify_source_fixture.py --source certificates/sources/k3e_compact_hall --target certificates/targets/delta5_gn_kac/a071_target_presentation
git diff --check -- compute/verify_source_fixture.py certificates/sources/k3e_compact_hall/README.md
```

Compile passed. All verifier invocations blocked as expected. Same-path
and nested-target probes also blocked. Whitespace checks passed; because
the owned paths are untracked, no-index whitespace probes were also used.

## Residual Limitation

The current source packet remains `mock_empty_blocked` and certifies no
compact Hall source stage.
