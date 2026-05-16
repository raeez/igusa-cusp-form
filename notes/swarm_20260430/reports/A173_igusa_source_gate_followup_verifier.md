# A173 -- Igusa Source-Gate Follow-Up Verifier

## Result

Read-only verification found no verifier proof-status errors after the
main-thread source-gate wording patch.

## Findings

- `main.tex:12900`: current source packet supplies no schema-complete
  source-side payload and no compact Hall proof.
- `main.tex:15483`: `SCHEMA_COMPLETE` is only a schema/status/payload
  gate, not compact-source certification or external verification.
- `certificates/sources/k3e_compact_hall/README.md:31`: positive verifier
  result means schema/status/payload/target-firewall checks only, and
  `certified` is explicitly not proof status.
- `compute/verify_source_fixture.py:6`: code checks source kind,
  `empty_blocked`, target separation, payload, statuses, and target-label
  firewall; it does not consume `certified` as proof status.

## Legitimate Certificate Language

- `main.tex:12478` and `main.tex:12936` define
  primitive-recognition certificate/datum as source-side mathematical data.
- `main.tex:15440` says the target-only certificate is target-presentation
  arithmetic only and supplies no compact Hall representatives or source
  matrices.

## Checks

- Targeted `rg` over `main.tex`, `compute/verify_source_fixture.py`, and
  `certificates/sources/k3e_compact_hall/README.md`.
- `git diff --check -- main.tex compute/verify_source_fixture.py certificates/sources/k3e_compact_hall/README.md`
  passed.
- Runtime sanity check: `compute/verify_source_fixture.py --check` returns
  `BLOCKED`, `schema_complete: false`, due to `mock_empty_blocked` and
  absent mathematical payload rows.

## Residual Obligation

The compact Hall proof remains open: future artifacts must supply actual
compact-source provenance, matrices \(M,D,B,G,K,Q,A\), radical/no-extra/PBW
/ transition rows, and proof-mode certification.

