# A153 -- Source Verifier Hardening Verifier

## Result

The hardened source verifier remains fail-closed for the current packet
and rejects status-only, partial-payload, and bad-degree-status rows in
temporary probes.

## Checks

- `compute/verify_source_fixture.py` compiled under `python3` with
  bytecode redirected to `/tmp`.
- `certificates/sources/k3e_compact_hall` returned `BLOCKED` with and
  without the external target supplied.
- Temporary mutation tests confirmed:
  - status/comment-only rows block with "has no mathematical payload";
  - partial payload rows block with missing payload diagnostics;
  - bad `source_block_status` blocks and reports the expected
    `source_admissible,source_verified` statuses.

## Caveat

A synthetic `/tmp` fixture with all schema fields populated by dummy
payload strings and all statuses set to verified returned `CERTIFIED`.
This means the current verifier is a schema/status/payload gate, not an
independent mathematical validator.

## Files Changed By Agent

None.
