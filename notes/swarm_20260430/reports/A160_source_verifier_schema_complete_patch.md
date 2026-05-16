# A160 -- Source Verifier Schema-Complete Semantics Patch

## Result

Implemented the A157 semantics correction: a positive source-fixture
verifier run now returns `SCHEMA_COMPLETE`, not `CERTIFIED`.

## Changed Paths

- `compute/verify_source_fixture.py`
- `certificates/sources/k3e_compact_hall/README.md`
- `main.tex`

## Changes

- Positive verifier status is `SCHEMA_COMPLETE`, with
  `schema_complete: true`.
- The manifest field `certified` is no longer trusted as proof status.
- Internal output variable names now use `schema_complete` rather than
  `certified`.
- The manuscript and source README state that the verifier is a
  schema/status/payload gate, not compact-source certification.

## Checks

- `PYTHONPYCACHEPREFIX=/tmp/igusa_pycache python3 -m py_compile compute/verify_source_fixture.py`
- Current mock packet without target reference returned `BLOCKED`.
- Current mock packet with target reference returned `BLOCKED`.
- Synthetic complete `/tmp` packet with `certified: false` returned
  `status: SCHEMA_COMPLETE` and no `CERTIFIED` output.
- Static TeX scan: 198 labels, 435 refs, 0 duplicate labels, 0 undefined
  refs.
- `git diff --check -- main.tex compute/verify_source_fixture.py certificates/sources/k3e_compact_hall/README.md`
- No-index diff diagnostics for the two untracked assigned files: 0.

## Limitation

The verifier remains a schema/status/payload gate. It does not parse
scalars, verify matrix identities, certify radical/no-extra/PBW equations,
or externally certify a compact Hall stage.

